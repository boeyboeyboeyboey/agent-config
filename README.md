# Agent config

My instructions, subagents and skills for [Claude Code](claude/CLAUDE.md) and [Codex](codex/AGENTS.md). I keep them here so I can send them to people, and so anyone curious can see how I run my AI agents.

## What the setup fixes

Most rules here exist because an agent got something wrong by default.

- Agents agree too easily. They're told to be blunt, sanity-check requests, and say so before building a bad idea.
- The main model is the expensive one. It plans, decides and reviews; cheaper subagents do the searching, reading, editing and test runs.
- Agents are bad judges of their own work. Delegated changes get read before they're reported done, and anything visual or logic-heavy goes to a separate reviewer.
- Agents make up what sources say. Any claim about a doc, brief or codebase needs an exact quote and location, and guesses are labelled as guesses.
- AI writing is padded. A writing section bans filler, stock phrases and the usual tells, and asks for the answer first.
- Agents act without asking. Every commit, push, merge or branch switch needs a yes in chat, and secrets never get printed or committed.

Both setups share these rules. They differ in which models do the work.

## Claude Code

| Agent | Model | Does |
| --- | --- | --- |
| Main | Your pick | Plans, makes decisions, reviews |
| `scout` | Haiku | Finds and reads files, docs and web pages |
| `worker` | Haiku | Edits from an exact spec, runs builds and tests |
| `senior` | Sonnet | Bounded work that needs judgment: UI polish, debugging, writing |
| `reviewer` | Sonnet | Reviews changes it didn't make; never edits |

Skills: [handover](claude/skills/handover/SKILL.md) (hand off to a fresh chat), [init-project](claude/skills/init-project/SKILL.md) (draft a project `CLAUDE.md`), [citation-audit](claude/skills/citation-audit/SKILL.md) (check citations before submitting), [slides](claude/skills/slides/SKILL.md) (read and write decks).

Also in [`claude/`](claude/): a [frontend rule](claude/rules/frontend.md) and a [settings example](claude/settings.example.json) that prompts before destructive Git commands. This runs on Claude Pro with no extra paid usage.

One known gap: a trailing force flag (`git push origin main --force`) gets past the settings patterns, so only the written rule catches it.

## Codex

| Agent | Model | Does |
| --- | --- | --- |
| Main | Terra `medium` | Plans, makes decisions, reviews |
| Subagents | Luna | Search, commands, scoped edits, routine review |
| | Terra | Visual and app work, longer drafts |
| | Sol | Complex engineering, architecture, hard review |
| | Astra | Rare read-only critique, only with approval |

Also in [`codex/`](codex/): a [config example](codex/config.example.toml), [Git rules](codex/rules/default.rules) with [test cases](verification/git-policy-cases.json), and [skills](codex/skills/).

## Using it

For Claude Code, paste [install-prompt.md](claude/install-prompt.md) into a session. It shows a plan and waits for your approval before writing anything.

Why each model and effort level was picked, with sources: [docs/model-routing.md](docs/model-routing.md).

[MIT license](LICENSE).
