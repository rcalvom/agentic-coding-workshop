# Exercise 1 — Context engineering and AGENTS.md

**Explain (6 minutes):** persistent project instructions vs. one-off prompts, context size, scoped guidance and validated engineering knowledge.

**Practice (10 minutes):**
1. Ask your agent to inspect `README.md`, `docs/api-spec.md`, `docs/architecture.md` and source files.
2. Generate a concise **`AGENTS.md`** describing verified run/test commands, where to find architecture information, conventions and constraints.
3. Manually remove redundant or incorrect statements; confirm one relationship in `docs/knowledge-map.md` against the actual source.
4. Ask the agent where booking-overlap logic lives and require a source path as evidence.

**Suggested prompt:** “Inspect this repository and draft a concise AGENTS.md with the verified architecture, setup commands, tests and non-negotiable constraints. Do not change application code or tests. Confirm at least one requirement → implementation → test relationship.”

**Done when:** the instruction file is accurate, short and the mapping was verified. **Not all agents load AGENTS.md automatically.** For native equivalents such as `CLAUDE.md` and `GEMINI.md`, see [compatibility](../docs/agent-compatibility.md). Do not fix the deliberate defect yet.
