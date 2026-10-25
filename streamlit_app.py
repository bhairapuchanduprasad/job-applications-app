"""Job Applications: phone-first app for the applications prepared by /apply and /job-scout.

Data comes from data/ (exported by scripts/build_meta.py and pushed by scripts/publish.sh).
Status changes ("Applied", "Interview", "Prepare anyway") are saved to status.json on the
`status` branch of the GitHub repo (or to state/status.json when running locally without a token).
The laptop merges them into applications/tracker.csv with scripts/pull_status.py.
"""
import base64
import csv
import hmac
import io
import json
import os
import time
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
import streamlit as st

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
LOCAL_STATE = Path(os.environ.get("JOBAPPS_STATE", HERE / "state" / "status.json"))
STATUSES = ["ready", "build-first", "applied", "interview", "offer", "rejected", "ghosted", "withdrawn"]
OPEN = {"ready", "build-first"}
ACTIVE = {"applied", "interview", "offer"}
CHANNELS = ["LinkedIn Easy Apply", "Company careers site", "Email", "Recruiter", "Other"]
ICON = {"ready": "🟢", "build-first": "🟠", "applied": "📨", "interview": "🗣️", "offer": "🎉",
        "rejected": "⚪", "ghosted": "👻", "withdrawn": "⏸️"}
FOLLOW_UP_DAYS = 14

st.set_page_config(page_title="Job Applications", page_icon="💼", layout="centered")
st.markdown("""<style>
/* keep columns side by side on phones (Streamlit stacks them below 640px) */
div[data-testid="stHorizontalBlock"] {flex-wrap: nowrap !important; gap: .4rem !important}
div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {min-width: 0 !important; width: auto !important; flex: 1 1 0 !important}
div[data-testid="stMetricValue"] {font-size: 1.5rem}
div[data-testid="stMetric"] label p {font-size: .8rem}
.stButton button, .stDownloadButton button, .stLinkButton a {padding: .35rem .4rem; min-height: 2.2rem}
div[data-testid="stVerticalBlockBorderWrapper"] {margin-bottom: .1rem}
.small {font-size: .85rem; opacity: .75}
.block-container {padding-top: 3.2rem; padding-left: .8rem; padding-right: .8rem}
</style>""", unsafe_allow_html=True)


# ---------- secrets / auth ----------
def secret(*keys, default=""):
    try:
        v = st.secrets
        for k in keys:
            v = v[k]
        return v
    except Exception:
        return default


def check_password() -> bool:
    expected = secret("password")
    if not expected or st.session_state.get("authed"):
        return True
    st.title("💼 Job Applications")
    with st.form("login"):
        pw = st.text_input("Password", type="password")
        if st.form_submit_button("Open", width="stretch"):
            if hmac.compare_digest(pw, expected):
                st.session_state.authed = True
                st.rerun()
            st.error("Wrong password")
    return False


# ---------- status store ----------
class Store:
    """status.json = {"apps": {folder: {...}}, "requests": {job_id: {...}}}"""

    def __init__(self):
        self.token = secret("github", "token")
        self.repo = secret("github", "repo")
        self.branch = secret("github", "branch", default="status")
        self.remote = bool(self.token and self.repo)

    @property
    def label(self) -> str:
        return f"GitHub ({self.repo})" if self.remote else "this computer"

    def _url(self):
        return f"https://api.github.com/repos/{self.repo}/contents/status.json"

    def _headers(self):
        return {"Authorization": f"Bearer {self.token}", "Accept": "application/vnd.github+json"}

    def load(self) -> tuple[dict, str | None]:
        if not self.remote:
            if LOCAL_STATE.exists():
                return json.loads(LOCAL_STATE.read_text()), None
            return {"apps": {}, "requests": {}}, None
        r = requests.get(self._url(), headers=self._headers(), params={"ref": self.branch}, timeout=15)
        if r.status_code == 404:
            return {"apps": {}, "requests": {}}, None
        r.raise_for_status()
        body = r.json()
        return json.loads(base64.b64decode(body["content"]).decode()), body["sha"]

    def save(self, data: dict, sha: str | None, message: str) -> None:
        text = json.dumps(data, ensure_ascii=False, indent=1)
        if not self.remote:
            LOCAL_STATE.parent.mkdir(parents=True, exist_ok=True)
            LOCAL_STATE.write_text(text)
            return
        payload = {"message": message, "content": base64.b64encode(text.encode()).decode(), "branch": self.branch}
        if sha:
            payload["sha"] = sha
        r = requests.put(self._url(), headers=self._headers(), json=payload, timeout=20)
        r.raise_for_status()

    def update(self, fn, message: str) -> None:
        """Read-modify-write with one retry if someone else wrote in between."""
        for attempt in range(2):
            data, sha = self.load()
            data.setdefault("apps", {})
            data.setdefault("requests", {})
            fn(data)
            try:
                self.save(data, sha, message)
                break
            except requests.HTTPError as e:
                if attempt == 1 or e.response is None or e.response.status_code != 409:
                    raise
        load_state.clear()


STORE = Store()


@st.cache_data(ttl=30, show_spinner=False)
def load_state() -> dict:
    try:
        return STORE.load()[0]
    except Exception as e:  # network trouble: show data without overrides
        st.session_state["store_error"] = str(e)
        return {"apps": {}, "requests": {}}


# ---------- data ----------
@st.cache_data(show_spinner=False)
def load_index(mtime: float) -> dict:
    return json.loads((DATA / "index.json").read_text())


@st.cache_data(show_spinner=False)
def load_meta(folder: str, mtime: float) -> dict:
    return json.loads((DATA / "apps" / folder / "meta.json").read_text())


def index() -> dict:
    p = DATA / "index.json"
    if not p.exists():
        st.info("No data yet. Run scripts/publish.sh on the laptop.")
        st.stop()
    return load_index(p.stat().st_mtime)


def meta(folder: str) -> dict:
    p = DATA / "apps" / folder / "meta.json"
    return load_meta(folder, p.stat().st_mtime)


def norm_status(s: str) -> str:
    return "applied" if s == "submitted" else s


def apps() -> list[dict]:
    """Index rows with app-side status changes applied (newer than the last laptop export)."""
    idx = index()
    state = load_state().get("apps", {})
    out = []
    for a in idx["apps"]:
        a = dict(a)
        a["status"] = norm_status(a["status"])
        s = state.get(a["folder"])
        if s and s.get("updated", 0) > idx["generated"]:
            for k in ("status", "applied_date", "applied_via", "note"):
                if s.get(k):
                    a[k] = s[k]
        out.append(a)
    return out


TZ = ZoneInfo("Europe/Berlin")


def today() -> date:
    return datetime.now(TZ).date()


def days_since(d: str) -> int | None:
    try:
        return (today() - date.fromisoformat(d[:10])).days
    except Exception:
        return None


def ago(d: str) -> str:
    n = days_since(d)
    return "" if n is None else ("today" if n == 0 else "yesterday" if n == 1 else f"{n} days ago")


def prepared_ago(a: dict) -> str:
    """'3 hours ago' for today's applications, otherwise 'yesterday' / 'N days ago'."""
    ts = a.get("prepared_at")
    if ts and days_since(a["date"]) == 0:
        mins = max(0, int((time.time() - ts) // 60))
        if mins < 60:
            return "just now" if mins < 2 else f"{mins} min ago"
        h = mins // 60
        return f"{h} hour{'s' if h > 1 else ''} ago"
    return ago(a["date"])


def day_label(d: str) -> str:
    n = days_since(d)
    if n == 0:
        return "Today"
    if n == 1:
        return "Yesterday"
    try:
        return date.fromisoformat(d[:10]).strftime("%a %d %b")
    except ValueError:
        return d


def shown_status(a: dict) -> str:
    return "ready" if a["status"] in OPEN else a["status"]


# ---------- actions ----------
def set_status(folder: str, status: str, via: str = "", note: str = "", applied: str = "") -> None:
    def fn(data):
        e = data["apps"].setdefault(folder, {})
        e.update(status=status, updated=time.time())
        if status == "applied":
            e["applied_date"] = applied or today().isoformat()
            e["applied_via"] = via
        if note:
            e["note"] = note
    STORE.update(fn, f"{folder}: {status}")


@st.dialog("Mark as applied")
def applied_dialog(a: dict):
    st.write(f"**{a['company']}** · {a['role']}")
    via = st.radio("Where did you apply?", CHANNELS, index=0)
    when = st.date_input("Date", value=today())
    note = st.text_input("Note (optional)", placeholder="e.g. used referral, salary 70k entered")
    if st.button("✓ Save", type="primary", width="stretch"):
        set_status(a["folder"], "applied", via, note, when.isoformat())
        st.session_state["toast"] = f"Marked {a['company']} as applied"
        st.rerun()


def open_app(folder: str):
    st.session_state["app"] = folder
    st.switch_page(PAGES["detail"])


def pdf_button(folder: str, doc: dict, key: str, label: str | None = None):
    p = DATA / "apps" / folder / doc["file"]
    if p.exists():
        st.download_button(label or ("📄 CV" if doc["kind"] == "cv" else "✉️ Letter"), p.read_bytes(),
                           file_name=doc["file"], mime="application/pdf", key=key, width="stretch")


def chip(a: dict) -> str:
    s = shown_status(a)
    bits = [f"{ICON.get(s, '•')} {s}"]
    if a.get("fit") is not None:
        bits.append(f"fit {a['fit']}")
    if a.get("ats") is not None:
        bits.append(f"ATS {a['ats']}%")
    return " · ".join(bits)


# ---------- pages ----------
def page_home():
    st.title("💼 To apply")
    rows = apps()
    pick = [a for a in rows if a["status"] in OPEN]
    week = [a for a in rows if a["status"] in ACTIVE and (days_since(a.get("applied_date", "")) or 99) <= 7]
    c1, c2, c3 = st.columns(3)
    c1.metric("To apply", len(pick))
    c2.metric("New today", sum(days_since(a["date"]) == 0 for a in pick))
    c3.metric("Applied 7d", len(week))
    if st.session_state.get("store_error"):
        st.warning("Couldn't reach the status store; showing the last export. " + st.session_state.pop("store_error"))

    # newest first, grouped by the day they were prepared
    pick.sort(key=lambda a: (a["date"], a.get("prepared_at") or 0), reverse=True)
    if not pick:
        st.success("Nothing waiting here. 🎉")
    last_day = None
    for a in pick:
        if a["date"] != last_day:
            last_day = a["date"]
            n = sum(x["date"] == last_day for x in pick)
            st.subheader(f"{day_label(last_day)} · {n}")
        m = meta(a["folder"])
        with st.container(border=True):
            st.markdown(f"**{a['company']}**  \n{a['role']}")
            where = a.get("city") or "—"
            src = "🔎 scout · " if a.get("found_by_scout") else ""
            st.markdown(f"<div class='small'>{chip(a)}<br>📍 {where} · {src}prepared {prepared_ago(a)}</div>",
                        unsafe_allow_html=True)
            b1, b2 = st.columns([3, 2])
            label = "Apply ↗" if m.get("apply_url_kind") == "posting" else "Find posting ↗"
            if m.get("apply_url"):
                b1.link_button(label, m["apply_url"], type="primary", width="stretch")
            if b2.button("Details", key=f"d-{a['folder']}", width="stretch"):
                open_app(a["folder"])
            docs = m.get("docs", [])
            b3, b4, b5 = st.columns(3)
            cv = next((d for d in docs if d["kind"] == "cv"), None)
            lt = next((d for d in docs if d["kind"] == "letter"), None)
            with b3:
                if cv:
                    pdf_button(a["folder"], cv, f"cv-{a['folder']}", "📄 CV")
            with b4:
                if lt:
                    pdf_button(a["folder"], lt, f"lt-{a['folder']}", "✉️ Letter")
            if b5.button("✓ Applied", key=f"ap-{a['folder']}", width="stretch"):
                applied_dialog(a)


def page_detail():
    rows = apps()
    by = {a["folder"]: a for a in rows}
    order = sorted(rows, key=lambda a: (a["status"] in OPEN, a["date"], a.get("prepared_at") or 0), reverse=True)
    folders = [a["folder"] for a in order]
    current = st.session_state.get("app") or st.query_params.get("app") or folders[0]
    if current not in by:
        current = folders[0]
    folder = st.selectbox("Application", folders, index=folders.index(current),
                          format_func=lambda f: f"{ICON.get(shown_status(by[f]), '•')} {by[f]['company']} · {by[f]['role']}")
    st.session_state["app"] = folder
    st.query_params["app"] = folder
    a, m = by[folder], meta(folder)

    st.header(a["company"])
    st.markdown(f"**{a['role']}**  \n📍 {a.get('city') or '—'} · prepared {a['date']} ({prepared_ago(a)})")
    c1, c2, c3 = st.columns(3)
    c1.metric("Fit", f"{a['fit']}/100" if a.get("fit") is not None else "—")
    c2.metric("ATS", f"{a['ats']}%" if a.get("ats") is not None else "—")
    c3.metric("Status", f"{ICON.get(shown_status(a), '')} {shown_status(a)}")
    if a.get("applied_date"):
        st.caption(f"Applied {a['applied_date']} via {a.get('applied_via') or '—'}"
                   + (f" · {a['note']}" if a.get("note") else ""))
    if m.get("verdict"):
        st.info(m["verdict"])
    if a["status"] == "build-first":
        st.caption(f"🛠️ The CV includes the project **{m.get('build') or 'from the Project tab'}**; "
                   "its brief is in the Project tab.")

    # Apply block
    with st.container(border=True):
        st.subheader("Apply")
        if m.get("apply_url"):
            label = "Open job posting ↗" if m.get("apply_url_kind") == "posting" else "Search posting on LinkedIn ↗"
            st.link_button(label, m["apply_url"], type="primary", width="stretch")
        if m.get("apply_hint"):
            st.caption(m["apply_hint"])
        elif m.get("source"):
            st.caption(f"Source: {m['source']}")
        if m.get("contact"):
            st.markdown(f"👤 Contact: **{m['contact']}**")
        cols = st.columns(max(1, len(m.get("docs", []))))
        for i, d in enumerate(m.get("docs", [])):
            with cols[i]:
                lang = " (DE)" if d.get("lang") == "de" else ""
                pdf_button(folder, d, f"dd-{i}", ("📄 CV" if d["kind"] == "cv" else "✉️ Letter") + lang)
        if a["status"] in OPEN:
            if st.button("✓ I applied", type="secondary", width="stretch"):
                applied_dialog(a)

    # Copy-paste answers
    if m.get("form_fields"):
        st.subheader("Copy-paste answers")
        st.caption("Tap the copy icon on a box.")
        for f in m["form_fields"]:
            st.markdown(f"**{f['label']}**")
            st.code(f["value"], language=None, wrap_lines=True)

    if m.get("gaps"):
        st.subheader("Gaps to be ready for")
        st.markdown("\n".join(f"- {g}" for g in m["gaps"]))
    if m.get("questions"):
        with st.expander("Likely interview questions"):
            for q in m["questions"]:
                st.markdown(f"**{q['q']}**  \n{q['a']}")

    # Status
    with st.expander("Change status"):
        with st.form("status"):
            cur = a["status"] if a["status"] in STATUSES else "ready"
            new = st.selectbox("Status", STATUSES, index=STATUSES.index(cur))
            note = st.text_input("Note", a.get("note", ""))
            if st.form_submit_button("Save", width="stretch"):
                set_status(folder, new, a.get("applied_via", ""), note, a.get("applied_date", ""))
                st.session_state["toast"] = "Saved"
                st.rerun()
        st.caption(f"Saved to {STORE.label}; the laptop copies it into tracker.csv on its next run.")

    # Documents
    base = DATA / "apps" / folder
    names = ["CV", "Letter", "Job", "Fit report", "Notes"] + (["Project"] if m.get("briefs") else [])
    tabs = st.tabs(names)
    for tab, kind in ((tabs[0], "cv"), (tabs[1], "letter")):
        with tab:
            docs = [d for d in m.get("docs", []) if d["kind"] == kind]
            if not docs:
                st.caption("No PDF.")
            for d in docs:
                if len(docs) > 1:
                    st.caption(d["file"])
                for i, png in enumerate(d["pages"], 1):
                    p = base / "preview" / png
                    if p.exists():
                        st.image(str(p), caption=f"Page {i}", width="stretch")
    for tab, fname in ((tabs[2], "job.md"), (tabs[3], "fit-report.md"), (tabs[4], "application-notes.md")):
        with tab:
            p = base / fname
            st.markdown(p.read_text(encoding="utf-8") if p.exists() else "_Not available._")
    if m.get("briefs"):
        with tabs[5]:
            for b in m["briefs"]:
                with st.expander(b.replace("project-brief-", "").replace(".md", "")):
                    st.markdown((base / b).read_text(encoding="utf-8"))


def page_pipeline():
    st.title("📊 Pipeline")
    rows = apps()
    counts = {s: sum(a["status"] == s for a in rows) for s in STATUSES}
    c = st.columns(4)
    c[0].metric("Open", counts["ready"] + counts["build-first"])
    c[1].metric("Applied", counts["applied"])
    c[2].metric("Interview", counts["interview"] + counts["offer"])
    c[3].metric("Closed", counts["rejected"] + counts["ghosted"] + counts["withdrawn"])

    follow = [a for a in rows if a["status"] == "applied" and (days_since(a.get("applied_date", "")) or 0) >= FOLLOW_UP_DAYS]
    if follow:
        st.subheader(f"Follow up? ({len(follow)})")
        st.caption(f"Applied {FOLLOW_UP_DAYS}+ days ago with no answer.")
        for a in follow:
            cols = st.columns([3, 1])
            cols[0].markdown(f"**{a['company']}** · {a['role']}  \napplied {a['applied_date']} ({ago(a['applied_date'])})")
            if cols[1].button("Open", key=f"f-{a['folder']}"):
                open_app(a["folder"])

    st.subheader("All applications")
    f1, f2 = st.columns(2)
    sel = f1.multiselect("Status", STATUSES)
    q = f2.text_input("Search", placeholder="company, role, city")
    shown = [a for a in rows if (not sel or a["status"] in sel)
             and (not q or q.lower() in f"{a['company']} {a['role']} {a.get('city', '')}".lower())]
    shown.sort(key=lambda a: a["date"], reverse=True)
    st.dataframe(
        [{"": ICON.get(a["status"], ""), "Company": a["company"], "Role": a["role"], "City": a.get("city", ""),
          "Fit": a.get("fit"), "Status": a["status"], "Prepared": a["date"], "Applied": a.get("applied_date", "")}
         for a in shown],
        hide_index=True, width="stretch")
    pick = st.selectbox("Open an application", [a["folder"] for a in shown], index=None,
                        format_func=lambda f: next(f"{a['company']} · {a['role']}" for a in shown if a["folder"] == f),
                        placeholder="Choose…")
    if pick:
        open_app(pick)


def page_scout():
    st.title("🔎 Scout")
    log = DATA / "scout" / "runs.log"
    if log.exists():
        lines = [l for l in log.read_text().splitlines() if l.strip()][-8:][::-1]
        st.subheader("Recent runs")
        st.code("\n".join(lines), language=None)
    seen = DATA / "scout" / "seen-jobs.csv"
    if not seen.exists():
        st.caption("No scout data yet.")
        return
    jobs = list(csv.DictReader(io.StringIO(seen.read_text(encoding="utf-8"))))
    requests_ = load_state().get("requests", {})
    kind = st.segmented_control("Show", ["Skipped", "Prepared", "All"], default="Skipped") or "Skipped"
    hide_title = st.toggle("Hide skipped by title filter (senior, student…)", value=True)
    q = st.text_input("Search", placeholder="company or title")
    rows = [j for j in jobs if (kind == "All" or j["status"] == kind.lower())
            and not (hide_title and j["reason"] in ("seniority/student title", "already in tracker"))
            and (not q or q.lower() in f"{j['company']} {j['title']}".lower())]
    rows.sort(key=lambda j: j["first_seen"], reverse=True)
    st.caption(f"{len(rows)} jobs")
    for j in rows[:80]:
        with st.container(border=True):
            st.markdown(f"**{j['title']}**  \n{j['company']} · 📍 {j['location'].replace(', Germany', '')} · {j['first_seen']}")
            if j["reason"]:
                st.caption(f"Reason: {j['reason']}")
            c1, c2 = st.columns(2)
            c1.link_button("Posting ↗", j["url"], width="stretch")
            if j["status"] == "skipped":
                if j["job_id"] in requests_:
                    c2.button("⏳ Queued", key=f"q-{j['job_id']}", disabled=True, width="stretch")
                elif c2.button("Prepare anyway", key=f"r-{j['job_id']}", width="stretch"):
                    def fn(data, j=j):
                        data["requests"][j["job_id"]] = {"url": j["url"], "title": j["title"], "company": j["company"],
                                                         "location": j["location"], "requested": time.time()}
                    STORE.update(fn, f"prepare anyway: {j['job_id']}")
                    st.session_state["toast"] = "Queued for the next scout run"
                    st.rerun()
            elif j["status"] == "prepared" and j.get("folder"):
                f = j["folder"].split("/")[-1]
                if c2.button("Open", key=f"o-{j['job_id']}", width="stretch"):
                    open_app(f)
    if len(rows) > 80:
        st.caption("Showing the newest 80. Use search to narrow down.")


def page_builds():
    st.title("🛠️ Build queue")
    st.caption("Planned projects that are on a CV but not built yet. Building one unlocks every application listed under it.")
    idx = index()
    by = {a["folder"]: a for a in apps()}
    builds = sorted(idx.get("builds", {}).items(), key=lambda kv: -len(kv[1]))
    if not builds:
        st.success("No pending builds.")
    for slug, folders in builds:
        open_ = [by[f] for f in folders if f in by and by[f]["status"] == "build-first"]
        if not open_:
            continue
        with st.container(border=True):
            st.markdown(f"### {slug}\nUnlocks **{len(open_)}** application{'s' if len(open_) > 1 else ''}")
            for a in sorted(open_, key=lambda a: -(a.get("fit") or 0)):
                cols = st.columns([3, 1])
                cols[0].markdown(f"{a['company']} · {a['role']}  \n<span class='small'>fit {a.get('fit')} · {a.get('city', '')}</span>",
                                 unsafe_allow_html=True)
                if cols[1].button("Open", key=f"b-{slug}-{a['folder']}"):
                    open_app(a["folder"])
            m = meta(open_[0]["folder"])
            brief = next((b for b in m.get("briefs", []) if slug in b), None) or (m.get("briefs") or [None])[0]
            if brief:
                with st.expander("Project brief"):
                    st.markdown((DATA / "apps" / open_[0]["folder"] / brief).read_text(encoding="utf-8"))


# ---------- main ----------
PAGES: dict = {}


def main():
    if not check_password():
        st.stop()
    PAGES.update({
        "home": st.Page(page_home, title="To apply", icon="🏠", default=True),
        "detail": st.Page(page_detail, title="Application", icon="📄", url_path="application"),
        "pipeline": st.Page(page_pipeline, title="Pipeline", icon="📊", url_path="pipeline"),
        "scout": st.Page(page_scout, title="Scout", icon="🔎", url_path="scout"),
        "builds": st.Page(page_builds, title="Build queue", icon="🛠️", url_path="builds"),
    })
    nav = st.navigation(list(PAGES.values()), position="top")
    if "toast" in st.session_state:
        st.toast(st.session_state.pop("toast"), icon="✅")
    gen = datetime.fromtimestamp(index()["generated"]).strftime("%d %b %H:%M")
    nav.run()
    st.caption(f"Data exported {gen} · statuses saved to {STORE.label}")


if __name__ == "__main__":
    main()
