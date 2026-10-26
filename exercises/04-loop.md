# Exercise 4 — Loop engineering: observe, fix, verify

**Explain (6 minutes):** plan → act → test → observe → repair, independent evidence and stop conditions.

**Practice (10 minutes):**
1. Summarize the issue and give the agent an explicit acceptance criterion.
2. Run `pytest -q tests/test_availability.py` **before edits**.
3. Ask the agent for a short plan and let it change the smallest implementation region.
4. Rerun targeted tests and iterate based on real output; limit repairs to three attempts.
5. **Never modify tests, fixtures or requirements.**
6. Run `pytest -q`, inspect `git diff`, report exact evidence.

**Suggested prompt:** “Follow AGENTS.md and the API-fix skill. First run targeted tests, then plan and fix Issue #1. Do not change tests or the contract. Iterate on real failures up to three attempts, then run the full suite and inspect the diff. Report exactly what passed.”

**Done when:** the failure is corrected with a focused diff and passing tests, or the agent reports a real blocker.

**Optional:** Instructor demonstrates a preconfigured hook blocking changes to tests; no live hook setup required.
