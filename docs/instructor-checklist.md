# Instructor rehearsal and lab-safety checklist

This is a **public workshop repository**. Do not publish the working fix or an answer key here; keep any instructor-only solution outside the shared starter.

## Technical rehearsal

1. Clone the **published** repository into a clean folder. Use Python 3.10+ and install dependencies.
2. Check `python -m pytest -q tests/test_rooms.py`: **2 passed**.
3. Check `python -m pytest -q`: **7 passed, 3 failed**, with failures limited to `test_adjacent_to_booking_end_is_available`, `test_adjacent_to_booking_start_is_available`, and `test_timezone_offsets_represent_same_instant`.
4. Verify the API starts and `/docs` loads. Use the sample query from the README to show the initial incorrect result.
5. In a **separate scratch copy**, implement the contract-preserving bug fix without changing tests/fixtures/spec. The full suite should become **10 passed**.
6. Restore/reset the public starter to the intentionally failing state; verify no solution was committed.
7. Verify [GitHub Issue #1](https://github.com/rcalvom/agentic-coding-workshop/issues/1) and `docs/issue-01.md` describe the same expected behavior.

## Agentic rehearsal

- Choose one reference coding-agent client and verify it reads the repository, executes `pytest`, and produces a visible diff.
- Prepare one **read-only GitHub MCP** connection and demonstrate the *actual* issue-retrieval tool call; do not claim that a browser/local fixture is MCP.
- Rehearse how that client discovers `AGENTS.md` or its equivalent, and a newly created SKILL.md (client-specific paths in `docs/agent-compatibility.md`).
- Keep fallback screenshots/recorded tool traces for unavailable accounts, authentication failures and rate limits.
- Do not require students to grant agents push access or to paste tokens into prompts.

## Timeboxing (75 minutes)

- 00–05: one architecture/context diagram and API request.
- 05–21: AGENTS.md and one verified codebase-map edge.
- 21–37: MCP issue fetch; preconfigured access or instructor demonstration.
- 37–53: small SKILL.md and verify discovery (or label fallback).
- 53–69: targeted red test → minimal code fix → green test → full suite → diff.
- 69–75: synthesis and evidence-based exit question.

**Stop conditions:** Do not spend more than ~2 minutes troubleshooting setup live. Prioritize the four observable artifacts and passing tests; advanced hooks, graph databases, plan mode and subagents are optional extensions.

## Known pedagogical limitations

- The bug is intentionally small: one focused change can make tests pass. This teaches at least one *red → repair → green* feedback cycle; it does **not** guarantee multiple failed repair attempts.
- `docs/knowledge-map.md` is a lightweight graph of relationships, not a maintained graph database.
- Native skills and MCP are client-dependent; the fallback is conceptually useful but must not be represented as the real mechanism.
- Dependencies may evolve. Re-run the clean-install rehearsal shortly before class.
