# Agent config

Personal [Codex](codex/AGENTS.md) and [Claude Code](claude/CLAUDE.md) setup. [Model choices, benchmarks, and limits](docs/model-routing.md).

- **Working with me:** blunt feedback; challenge bad ideas; clarify ambiguity; explain decisions; cut filler.

- **Planning and safety:** approval before bigger changes; scoped edits; preserve existing work; explicit Git permissions.

- **Delegation:** keep the main chat focused; bounded subagent tasks; clear file ownership; small checks handled directly.

- **Codex routing:** Luna for routine work; Terra for visual work, app tasks, and longer drafts; Sol for complex engineering; Astra approval-only.

- **Claude routing:** Haiku/medium for scout and worker; Sonnet/high for senior and reviewer. Main model selected in Claude. Pro budget; no extra paid usage.

- **Review:** main agent checks delegated diffs; independent review for logic and visual changes; fix material findings.

- **Verification:** targeted searches; checks matched to risk; tests for logic that can break silently; unchecked areas called out.

- **Completion:** stop when verified; report uncertainty. Codex slide rules: one point per slide; explanations in speaker notes.

Codex files: [config example](codex/config.example.toml), [Git rules](codex/rules/default.rules), [skills](codex/skills/), [rule checks and gaps](verification/git-policy-cases.json).

Claude files: [install prompt](claude/install-prompt.md), [agents](claude/agents/), [frontend rule](claude/rules/frontend.md), [settings example](claude/settings.example.json).

- **Claude Git** — one chat approval per routine action. The settings example prompts for selected destructive commands. `git push origin main --force` falls outside those patterns and is covered by the prose rule. [Git safety](claude/CLAUDE.md#git-safety-all-agents)

## Claude skills

- [handover](claude/skills/handover/SKILL.md) — current state, checks, next steps, and a kickoff prompt for a fresh chat.
- [init-project](claude/skills/init-project/SKILL.md) — project `CLAUDE.md` with checked commands and repo conventions, shown for approval before saving.
- [citation-audit](claude/skills/citation-audit/SKILL.md) — match cited claims to exact source passages before graded or external submission.
- [slides](claude/skills/slides/SKILL.md) — write slides and review decks or PDFs. View every page for decks of 15 pages or fewer. For longer decks, use the inventory plus visual checks where the task depends on charts, diagrams, or layouts. Uses `python-pptx` and `pdfplumber`, LibreOffice for PowerPoint rendering, and Keynote on macOS for `.key` exports.

[MIT license](LICENSE).
