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

Claude files: [install prompt](claude/install-prompt.md), [agents](claude/agents/), [frontend rule](claude/rules/frontend.md), [skills](claude/skills/), [settings example](claude/settings.example.json).

- **Citation audit** — match cited claims to source passages before graded or external submission. [Skill](claude/skills/citation-audit/SKILL.md)
- **Slides** — flag pages for visual review with `python-pptx` and `pdfplumber`. Render PowerPoint with LibreOffice (`soffice`) and export `.key` files with Keynote on macOS. Check diagrams built from shapes and PDFs with recurring picture layouts manually. The script can miss both. [Skill](claude/skills/slides/SKILL.md)
- **Claude Git** — one chat approval per routine action. The settings example prompts for selected destructive commands. `git push origin main --force` falls outside those patterns and is covered by the prose rule. [Git safety](claude/CLAUDE.md#git-safety-all-agents)

[MIT license](LICENSE).
