# Student preflight — complete before the 75-minute workshop

The hands-on blocks are ten minutes each, so **repository setup and agent authentication must happen before class**. No paid product or specific model is prescribed by the repository; access limits and available clients may differ.

## 1. Clone and install

Use **Python 3.10+**, Git, and a Python environment. In macOS/Linux or WSL:

```bash
git clone https://github.com/rcalvom/agentic-coding-workshop.git
cd agentic-coding-workshop
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q tests/test_rooms.py
```

If your system uses `python3` instead of `python`, substitute `python3`. On Windows PowerShell:

```powershell
git clone https://github.com/rcalvom/agentic-coding-workshop.git
cd agentic-coding-workshop
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q tests/test_rooms.py
```

**Required preflight result:** the two smoke tests pass. You may run the full suite to see its three intentional failures, but **do not fix the bug yet**.

## 2. Verify local API access

Run `python -m uvicorn app.main:app --reload` (or the virtual-environment Python equivalent) from the repository root. Open http://127.0.0.1:8000/docs. Stop the server after verifying it loads.

## 3. Select and test a coding agent

A suitable client should be able to **read code, propose/edit files, and execute or inspect terminal commands**. In the repository root, ask it to locate the `/rooms/available` endpoint **without changing any code**. If it is a chat-only model, you will need to execute commands manually and pass the actual output; this is a human-in-the-loop fallback, not equivalent automated tool use.

For persistent project guidance and skill-file locations by client, see [compatibility](agent-compatibility.md). Do not assume an unfamiliar client automatically reads AGENTS.md or discovers arbitrary SKILL.md paths.

## 4. Check MCP availability before class

The MCP activity uses [GitHub Issue #1](https://github.com/rcalvom/agentic-coding-workshop/issues/1). You will need a **client with an MCP connection capable of reading GitHub issues**, ideally the official GitHub MCP Server restricted to `issues` and read-only access.

The official GitHub MCP Server supports read-only mode; see [server configuration](https://github.com/github/github-mcp-server/blob/main/docs/server-configuration.md) and [installation options](https://github.com/github/github-mcp-server). Your agent host may require OAuth/login or separate server registration. **Never put access tokens in a prompt, configuration committed to Git, or screenshots.**

Test that your client can list its available MCP tools and read Issue #1 **before class**. If it cannot, pair with someone whose setup works or watch the instructor's live MCP demonstration. You can read [the offline issue fixture](issue-01.md) to continue the other exercises, but that alone does **not** complete the MCP learning objective.

## Before class, confirm

- [ ] Python dependencies installed and smoke tests pass.
- [ ] API documentation loads at `/docs`.
- [ ] Coding agent can inspect this local repository.
- [ ] MCP can fetch a GitHub issue, or a fallback/pair is arranged.
- [ ] You have **not** fixed the deliberate overlap bug.
