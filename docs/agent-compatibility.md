# Coding-agent compatibility notes

This workshop is **conceptually agent-agnostic**. The ability to run/edit files is required for fully agentic practice; instruction discovery, skills, and MCP are not identical across clients. Verify behavior in your installed version.

## Persistent instructions (Exercise 1)

- **Codex:** repository-level `AGENTS.md` is a recognized instruction file.
- **Claude Code:** the default repository instruction file is `CLAUDE.md`. Students can generate `AGENTS.md` for the shared exercise and copy its verified content to `CLAUDE.md` (or explicitly point Claude at it).
- **Gemini CLI:** the default repository context file is `GEMINI.md`. Students can transfer relevant `AGENTS.md` content, or configure alternative context filenames if supported.
- **Other agents:** use their documented project-instruction facility or explicitly provide the file.

A file existing on disk does not prove the client has loaded it. Ask the agent to identify its active instruction sources; check the client's interface or logs when available.

## Skills (Exercise 3)

Use `SKILL.md` plus a clear YAML `name` and `description`. Place the file in a supported **project skill directory** if your client can discover skills:

| Client | Typical project skill location |
|---|---|
| OpenAI Codex | `.agents/skills/resolve-api-issue/SKILL.md` |
| Claude Code | `.claude/skills/resolve-api-issue/SKILL.md` |
| Gemini CLI | `.gemini/skills/resolve-api-issue/SKILL.md` or `.agents/skills/resolve-api-issue/SKILL.md` |
| VS Code / Copilot skills | `.github/skills/resolve-api-issue/SKILL.md`, `.agents/skills/...` or `.claude/skills/...` depending on configuration |

After writing the skill, **confirm it was discovered** (for example, via a skills listing or the agent's skill UI). Discovery does not guarantee the agent will invoke it. In Exercise 4, inspect the agent's behavior to see if it followed the documented steps. If your client has no native skill facility, store it at `skills/resolve-api-issue/SKILL.md` and explicitly provide its contents as a reusable procedure; label this as a **fallback**, not native skill activation.

## MCP (Exercise 2)

The official [GitHub MCP Server](https://github.com/github/github-mcp-server) can be configured for restricted toolsets and **read-only** operations, e.g. the `issues` toolset with read-only mode. The [server configuration guide](https://github.com/github/github-mcp-server/blob/main/docs/server-configuration.md) describes remote and local alternatives.

- A successful exercise involves observing a **real MCP tool call** and identifying the source and permissions.
- GitHub's regular website, a direct API call, and reading `docs/issue-01.md` are useful fallbacks but **not evidence of MCP integration**.
- Never embed a secret in a prompt or a repository file.

## Official references

- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Gemini CLI context files](https://geminicli.com/docs/cli/gemini-md/)
- [Gemini CLI skills](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md)
- [VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [GitHub MCP Server](https://github.com/github/github-mcp-server)
