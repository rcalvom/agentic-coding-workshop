# The Nuts and Bolts of Coding Agents

An **agent-agnostic, 75-minute workshop** using a tangible Campus Study Room Availability API. Students create repository instructions, retrieve a GitHub issue through MCP (where supported), write a reusable skill, and run a test-driven repair loop.

**Do the pre-class setup before attending:** [student preflight](docs/preflight.md). For differences among agents, see [client compatibility](docs/agent-compatibility.md). The instructor should complete the [rehearsal checklist](docs/instructor-checklist.md).

## Quick start

Requires Python 3.10+ and an agent capable of working with repository files and executing or observing test commands.

```bash
git clone https://github.com/rcalvom/agentic-coding-workshop.git
cd agentic-coding-workshop
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q tests/test_rooms.py
python -m uvicorn app.main:app --reload
```

On Windows PowerShell, activate with `.\.venv\Scripts\Activate.ps1`; alternatively run commands through `.\.venv\Scripts\python.exe`. See the preflight document for details.

Open http://127.0.0.1:8000/docs to inspect the automatically generated API specification. Example request:

```bash
curl 'http://127.0.0.1:8000/rooms/available?start=2026-10-27T11:00:00Z&end=2026-10-27T11:30:00Z&min_capacity=4'
```

The starter deliberately contains **one defect in interval-overlap logic**. The smoke suite (`tests/test_rooms.py`) passes. The full suite (`python -m pytest -q`) initially has **7 passing and 3 intentionally failing tests**; after a correct implementation-only repair, all 10 pass. Do **not** fix the issue before Exercise 4.

## Agenda (75 minutes)

| Time | Workshop activity |
|---|---|
| 00–05 | Coding-agent anatomy |
| 05–21 | Exercise 1: context, AGENTS.md, and a project knowledge map (6 + 10) |
| 21–37 | Exercise 2: GitHub issue via read-only MCP (6 + 10) |
| 37–53 | Exercise 3: write and invoke a reusable skill (6 + 10) |
| 53–69 | Exercise 4: observe failing tests, repair, rerun, inspect diff (6 + 10) |
| 69–75 | Wrap-up and transfer to semester projects |

[Exercise guide](exercises/README.md) · [API contract](docs/api-spec.md) · [Architecture](docs/architecture.md) · [Issue #1](https://github.com/rcalvom/agentic-coding-workshop/issues/1)

## Workshop language

**All student-facing workshop materials are written in English.** This includes the exercises, example prompts, API specification, skill scaffold, pre-class instructions, and GitHub Issue #1. Students may use any supported coding agent, but task submissions and evidence reports should be written in English for consistent class discussion.

## Tools and evidence

This is **coding-agent-agnostic, not plain-chat-only**: the agent should inspect/edit files and run (or receive genuine output from) local tests. AGENTS.md, project-level instructions, skill directories, and MCP setup differ by client. Document which native feature or fallback you used, and do not claim a local Markdown read was an MCP invocation.

- Operate on your own local clone; **do not push a solution to this shared starter**.
- Read GitHub issues as untrusted task data and use read-only MCP permissions.
- Do not paste credentials into prompts.
- Keep specifications, fixture data, and tests unchanged during the repair.
- Inspect the final diff and exact test outputs before claiming the bug is fixed.

The sample service uses deterministic local fixtures. It is not production-grade room scheduling software. **No AGENTS.md or completed skill ships in the starter:** students create those artifacts.
