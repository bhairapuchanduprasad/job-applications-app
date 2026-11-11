# Project brief: Web Data Integrations Toolkit (repo: web-data-integrations-toolkit)
**Goal:** one CLI + client lib for a public REST API (e.g. a free public data/search API), shipped as PyPI + npm packages, with an MCP server (Claude Code / Cursor), a LangChain tool, and docs.
**Proves for JD:** Python, TypeScript/Node.js, SDK/CLI, PyPI/npm release, MCP, Claude Code, LangChain, REST auth/credentials, CI/CD, documentation.
**Scope (1-2 days):** Python client + Typer CLI; small TS client + MCP server (official TS MCP SDK); LangChain Tool wrapper; API key via env var / keychain, never logged; pytest + vitest; GitHub Actions publishing to TestPyPI/npm (dry-run if no account) with version tags.
**Stack:** Python, Typer, httpx, TypeScript, Node.js, MCP SDK, LangChain, GitHub Actions.
**Architecture:** API -> Python client -> CLI; API -> TS client -> MCP server; Python client -> LangChain tool. Shared OpenAPI spec for types.
**Milestones:** 1 Python client+CLI+tests; 2 TS client+MCP server; 3 LangChain wrapper; 4 CI release workflow; 5 README + setup guides for Claude Code/Cursor, examples.
**README outline:** what it is, install (pip/npm), auth, CLI usage, MCP config snippets, LangChain example, release process.
**Demo idea:** ask Claude Code a question and watch it call the MCP tool; same query through the CLI.
**CV bullet it must live up to:** Shared CLI and client library for a public REST API with token authentication, published as a Python package (PyPI) and an npm package, with an MCP server for Claude Code and Cursor, a LangChain tool wrapper, setup guides and runnable examples. Versioned releases, tests and CI/CD via GitHub Actions.
