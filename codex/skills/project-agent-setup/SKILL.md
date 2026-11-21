---
name: project-agent-setup
description: Create concise project-level AGENTS.md instructions for an ongoing project when the user agrees to set them up.
---

# Project agent setup

Use only when the working folder is an ongoing project, has no project-level
`AGENTS.md`, and the user agrees to create one. Do not apply to one-off questions,
scratch/temp folders, or someone else's repository.

## Gather project context

Ask the user for 3–5 lines that files cannot establish: what the project is, deadline
and deliverable, constraints such as budget or rules, whether teammates share it, and
what is off-limits. Continue independent read-only reconnaissance while awaiting input.

Use parallel Luna subagents for discovery, keeping each task bounded to independent
concerns. Collect:

- Exact project commands from `package.json`, `Makefile`, CI, or equivalent; never guess
- A concise directory map, conventions, and relevant existing documents with what each
  covers
- For non-code projects, folder contents, source/evidence rules, and key documents

Stop once the information needed for useful project instructions is clear. Ask only for
missing context that changes the instructions materially.

## Draft and save

Draft a file of about 100 lines maximum covering project purpose and constraints,
verified commands, directory map, conventions, guardrails, and further reading. Link
existing docs by path and say when each should be read; do not copy their contents. Omit
task status, plans, and anything already covered by global instructions.

Have a subagent check each command against its definition and run only safe local
checks (build, test, lint, typecheck, starting the dev server). Never run commands that
deploy, publish, spend money, change shared state or data, or delete anything; mark
those "inspected, not run". Mark any failures; do not report a failure as a pass. Show
the draft to the user before saving it. In a shared git repository, add the new
`AGENTS.md` to `.git/info/exclude` rather than committing it, unless the user says
otherwise. Do not commit or make other repository changes without
specific authorization.
