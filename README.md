# Agent config

Personal instructions and skills for [Codex](codex/AGENTS.md) and [Claude Code](claude/CLAUDE.md). [Model choices, benchmarks, and limits](docs/model-routing.md).

## Workflow

- Give direct feedback, question weak ideas, and clarify ambiguity that affects the outcome.
- Plan larger changes before editing. Keep changes scoped, preserve existing work, and get permission for Git actions.
- Delegate bounded tasks with clear ownership. Keep decisions and final review with the main agent.
- Review delegated changes, use independent review for logic and visual work, and match checks to the risk. Report anything left unchecked.
- Ground source claims in exact quotes and locations. Label inference and state gaps. [Codex rules](codex/AGENTS.md#grounding-all-agents) · [Claude rules](claude/CLAUDE.md#grounding-all-agents)
- Write plainly and cut filler. Keep one point per slide, with explanations in speaker notes. [Codex writing](codex/AGENTS.md#writing-all-agents) · [Claude writing](claude/CLAUDE.md#5-writing-all-agents)

## Model routing

| Work | Model |
| --- | --- |
| Routine Codex tasks | Luna |
| Visual work, app tasks, and longer drafts | Terra |
| Complex engineering | Sol |
| Exceptional read-only critique | Astra, with approval |
| Claude scouting and execution | Haiku at medium effort |
| Claude senior work and review | Sonnet at high effort |

The Claude main model is selected in Claude. This setup uses Claude Pro, with no extra paid usage.

## Setup files

- Codex includes a [config example](codex/config.example.toml), [Git rules](codex/rules/default.rules), [skills](codex/skills/), and [rule checks and gaps](verification/git-policy-cases.json).
- Claude includes a [paste-in install prompt](claude/install-prompt.md), [agents](claude/agents/), a [frontend rule](claude/rules/frontend.md), and a [settings example](claude/settings.example.json).

One chat approval per routine Git action, with settings prompts for selected destructive commands. A trailing force flag, as in `git push origin main --force`, slips past those patterns and relies on the [prose rule](claude/CLAUDE.md#git-safety-all-agents).

## Claude skills

| Skill | Purpose |
| --- | --- |
| [handover](claude/skills/handover/SKILL.md) | Save the current state, checks, next steps, and a kickoff prompt. |
| [init-project](claude/skills/init-project/SKILL.md) | Draft a project `CLAUDE.md` with checked commands and conventions, then show it for approval. |
| [citation-audit](claude/skills/citation-audit/SKILL.md) | Match cited claims to source passages before graded or external submission. |
| [slides](claude/skills/slides/SKILL.md) | Write slides and review visual content in decks and PDFs. |

Slide review covers every page in decks of 15 pages or fewer. For longer decks, start with the inventory and check additional pages where visuals matter. Uses `python-pptx` and `pdfplumber`, LibreOffice for PowerPoint rendering, and Keynote on macOS for `.key` exports.

[MIT license](LICENSE).
