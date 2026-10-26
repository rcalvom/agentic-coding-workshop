# Exercise 3 — Skills: a reusable API-development procedure

**Explain (6 minutes):** on-demand procedures vs. persistent repository guidance, discovery, skill frontmatter and progressive disclosure.

**Practice (10 minutes):**
1. Start from `templates/SKILL.template.md`; **fill its TODO sections rather than merely copying the file**, creating a skill named `resolve-api-issue`.
2. The procedure should read the spec and issue, plan, run tests **before** editing, make only minimal implementation changes, iterate based on test output (up to three attempts), check the full suite and inspect the diff.
3. Save `SKILL.md` in **your client's project skill directory** (not just an arbitrary folder): for Codex `.agents/skills/resolve-api-issue/`, for Claude Code `.claude/skills/resolve-api-issue/`, for Gemini CLI `.gemini/skills/resolve-api-issue/`. See [compatibility](../docs/agent-compatibility.md) for other clients and fallbacks.
4. Confirm that your agent discovers the skill (through its skill listing/UI, if available). Ask it to outline a plan for Issue #1, **without implementing yet**.
5. If native discovery is unsupported, provide the SKILL.md contents explicitly as task context; state that this is a fallback.

**Done when:** you have a reusable skill with name, description, steps and verification evidence, and you know whether it was actually discovered. The real implementation belongs in Exercise 4.
