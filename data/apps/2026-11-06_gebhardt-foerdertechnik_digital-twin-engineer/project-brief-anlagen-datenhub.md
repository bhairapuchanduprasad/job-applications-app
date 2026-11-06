# Project brief: Anlagen-Datenhub (reuses planned "Spin-off Ecosystem Data Hub" pattern)
Goal: shared data basis for a (synthetic) conveyor plant, joining sources from engineering, electrical and SAP.
Proves (JD): Zusammenführung von Daten aus Konstruktion, Elektrotechnik, SAP; weniger Doppelerfassung; Digital Twin.
Scope (1-2 days): synthetic CSV exports (mechanical BOM, electrical equipment list, mock SAP order export) -> Python ETL -> PostgreSQL model (plant, component, source record, per-field provenance); matching of the same component across sources (rules, then embeddings) with a small labelled pair set; data quality checks; FastAPI read endpoints; Docker; pytest + GitHub Actions.
Milestones: 1 synthetic data + schema; 2 ETL + provenance; 3 matching + eval; 4 API + CI; 5 README.
CV bullet it must live up to: all of the above (no metrics, no link).
