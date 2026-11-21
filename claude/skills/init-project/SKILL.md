---
name: init-project
description: Create a project-level CLAUDE.md for a real, ongoing project that doesn't have one. Use after the user agrees to the offer, or when they ask to set up a project CLAUDE.md.
---

1. Ask the user for 3–5 lines of context the files can't tell you: what the project is,
   deadline and deliverable, constraints (budget, rules), shared with teammates or not,
   and what's off-limits.
2. Gather the rest with parallel scouts: exact commands (from package.json, Makefile, CI;
   never guessed), directory map, conventions, and existing docs with what each covers.
   For non-code projects, cover folder contents, source/evidence rules, and key documents.
   For visual projects (games, 3D scenes, sites), also find how to render fixed views
   and run an intersection or layout check, so the `reviewer` doesn't have to work it out.
3. Draft it (max ~100 lines): summary and constraints, commands, directory map,
   conventions, guardrails, and further reading with one line on when to read each doc.
   Link docs by path; don't copy or @-import them, except a short binding policy file
   like AGENTS.md (under ~150 lines). Leave out task status and plans, and anything
   already in the global CLAUDE.md.
4. Have a `worker` check each command against its definition and run only safe local
   checks (build, test, lint, typecheck, starting the dev server). Never run commands
   that deploy, publish, spend money, change shared state or data, or delete anything;
   mark those 'inspected, not run'. Show the user the draft before saving. In a shared
   git repo, add it to `.git/info/exclude` rather than committing it, unless the user
   says otherwise.
