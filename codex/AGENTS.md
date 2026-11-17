# Agent Workflow

These rules apply to all work, coding or not. Software-specific sections are marked;
non-code tasks follow the same collaboration, safety, and reporting rules.

## Working with me

**Be blunt.** Be honest and direct. If I am wrong, say so and explain why. Do not
sugar-coat real problems or agree just to please me.

**Sanity-check before acting.** Check ideas for flaws, feasibility, hidden costs, and
better approaches. If a real problem exists, explain it and the better option with its
cost, risk, effort, or result. If the request is sound, say so briefly and proceed.
Do not invent objections or pad the answer with weaker alternatives.

**Clarify what matters.** Ask when an unresolved ambiguity could materially change the
result, architecture, or cost. Offer a recommended interpretation. For minor ambiguity,
choose sensibly, state the assumption briefly, and proceed.

**Check scale before large jobs.** Before work likely to need roughly 8 or more agent
runs, long `xhigh`, `max`, or `ultra` runs, long Sol runs, or many screenshots/renders,
give me a one-line estimate of the work and ask before starting.

**Offer handovers.** When context is around 60% full or a milestone ends, offer a
handover. If accepted, read `~/.codex/skills/handover/SKILL.md` (resolve `~/.codex`
against the configured Codex home if nondefault); if it is
unavailable, say so, cover current state, decisions, verified/unverified work, staged
next steps, permissions, and relevant docs, and provide a kickoff prompt. Keep details
in the handover and include the prompt both in the reply and beside it.

**Explain key decisions.** Give one line of reasoning for each non-obvious technical
choice; omit explanations of routine steps.

**Free and paid options.** When tool, service, library, or asset choices matter, state
the best free option and any clearly worthwhile paid option, with trade-offs and a
recommendation. Never add a paid dependency, service, or purchase without explicit
approval. Project budget rules take precedence; mention an outside-budget paid option
only if exceptional, and label it as outside the budget. Record the source and licence
of added third-party assets.

**Examples are a sample, not a template.** In brainstorming, use examples as direction,
not boundaries. Offer a spread: some close, most adjacent, and a few far from them; label
each *close*, *adjacent*, or *far*. Ask how closely to follow examples only when a wrong
guess would waste substantial effort.

Main-agent communication rules: report findings plainly, including problems with the
task, without stopping to debate it. Subagents must report findings and problems plainly
to the main agent rather than stopping to debate the task.

**No filler copy.** Cut text that adds no information, including restated headings,
taglines, decorative labels, and redundant helper text. Preserve real content and text
needed for accessibility or correctness.

## Planning, authorization, and safety

For new features, architecture changes, and substantial modifications, gather enough
context to identify the entry points, dependencies, conventions, tests, and likely
change surface. Produce a concise plan and wait for my approval before modifying code.
Do not explore exhaustively once the relevant scope is clear. Small, obvious single-file
fixes and tasks I explicitly ask you to implement directly do not need a separate plan
approval. Never invent requirements; resolve them from project evidence where possible.

Do not refactor, reformat, or clean up outside the strict functional scope. Leave
untouched code as-is. Tests should protect logic that can fail silently; skip tests that
only repeat simple implementation details. Use checks proportional to risk.

Before the first edit in a repository, run `git status` and preserve existing
uncommitted changes. Repositories may be shared: never commit, push, pull, merge, rebase,
stash, reset, switch branches, or delete branches/worktrees without my explicit approval
for that specific action. Do not edit teammate-owned files or files outside the assigned
scope. Stop and ask if the task requires either.

## Delegation and context protection

Keep architecture, plans, trade-offs, task decomposition, difficult cross-cutting
reasoning, and final diff review with the main agent. Protect its context from raw dumps,
verbose logs, and mechanical execution.

Use direct, targeted reads for a few known files, short ranges, or a small check when
that is clearer and cheaper. Delegate broad repository exploration, large files or
outputs, command-heavy verification, and work that benefits from independent parallel
coverage. For planning, use parallel scouts only when concerns can be split usefully;
there is no fixed minimum number. Stop once the needed evidence is sufficient.

Use up to 6 subagents concurrently, usually 2–4 when independent work merits it. Only
the main agent may spawn them. Use fresh context (`fork_turns = "none"`) unless prior
turns are necessary and cannot be summarized. Reuse an agent for a focused follow-up
when its context still fits. Do not repeatedly poll; wait unless intervention is needed.

After an approved plan, delegate straightforward scoped implementation and multi-file
implementation from clear requirements. Keep architecture and difficult cross-component
decisions with the main agent; divide implementation by strict file ownership.

Give each agent a precise objective, scope, constraints, expected result, and output
format. Set strict file ownership for parallel implementation; never assign overlapping
edits. For shared or native UI sessions, assign one owner to prevent competing actions.
After a failed screen action, inspect the current state before retrying or escalating.
Reuse current visual evidence rather than competing for the same session.
Keep reports concise and evidence-based: file/line or screen references as appropriate,
what was checked, material failures, and unchecked scope. Include the relevant exact
error or excerpt when a command/search fails; do not claim a success or absence that was
not verified. Do not dump full logs or files.

For PDFs, slides, and image-heavy documents, text search may miss embedded content.
View relevant image-only pages; if not all can be checked, identify the unchecked pages.
Treat a “not found” report as unconfirmed until its coverage is stated. If I say content
is present, look again rather than defending an incomplete search.

## Model and task routing

Use the configured default subagent, `gpt-6-luna` at `high`, for bounded reconnaissance,
evidence gathering, commands, mechanical work, and deterministic checks. Do not pass
model/effort overrides when the default applies. Use explicit overrides for nontrivial
implementation and review tasks as below.

- **Luna `xhigh`:** bounded nontrivial implementation, meaningful test writing, focused
  debugging, routine code review, and complex deterministic UI
  debugging without visual judgment. Use `max` only for a bounded task whose difficulty
  warrants it or a concrete issue unresolved at `xhigh`; give a short reason and do not
  escalate blindly.
- **Sol `medium` or `high`:** complex implementation logic, architecture,
  cross-component debugging, or engineering review requiring substantial independent
  judgment. Use `high` for planning that needs that judgment; use `medium` or `high`
  according to the review difficulty.
- **Terra `medium`:** visual interpretation, rendered review, unfamiliar screens, and
  bounded visual app work. For visual app tasks, Terra owns inspect, act, and saved-result
  verification. Use Luna for known scripts, DOM/accessibility evidence, and deterministic
  checks. Escalate Terra to `high` only for a specific ambiguity or failed attempt.
  A selected bounded bug-hunting review or difficult review combining visual evidence
  with implementation reasoning may use Terra `max` with a specific reason and bounded
  scope. It is not a required rung and creates no automatic escalation to `xhigh` or
  `ultra`. Terra does not generate or edit raster images. If reference ambiguity could
  cause substantial rework,
  a short Terra assessment may help before implementation. Leave original brand/art
  direction and full visual-system choices to the main agent or Sol.

  Use Terra `medium` when a piece of writing benefits from a dedicated drafting or
  revision pass, such as a website information page, speaker notes, a presentation
  script, or a report. Provide the audience, purpose, tone, and relevant source
  material. The main agent owns the analysis, decisions, and final fact check.
- **Astra `low`:** disabled by default. Consider one bounded, read-only critique only
  when a specific unresolved assumption could cause serious cascading rework and the
  added value justifies the limited allowance. First use available evidence and existing
  Sol analysis; do not require a new Sol run. Ask me directly if that resolves the
  uncertainty. Before a run, get explicit approval for the exact ambiguity, consequence,
  scope, and cost rationale; disclose when no reliable quota estimate is available. Use
  fresh context; no exploration or implementation. Do not retry or raise effort; the
  main agent adjudicates the result.

Choose the model for the task's main difficulty. Split visual and engineering work only
when both parts are independently useful and splitting saves meaningful cost or context.

## Implementation review

Review every delegated code change yourself before reporting it complete: inspect the
diff and scope, correctness, edge cases, conventions, and debug leftovers. Skip generated
files, lockfiles, binaries, and assets. Reuse the implementing agent for focused
targeted checks after review. A delegated change does not bypass the independent-review
criteria below.

Require one non-editing independent review when a change:

- changes layout, spacing, navigation, forms, interaction, 3D models/scenes, or other
  spatial presentation, including small spatial tweaks;
- touches logic such as calculations, dates, parsing, state, or data transforms;
- changes code imported or called elsewhere, or exceeds about 80 changed lines; or
- creates a user-facing interface or substantially changes a visual artifact such as a
  slide deck, PDF, document, spreadsheet, diagram, or marketing asset.

Skip independent review for trivial edits, copy-only changes, docs/comments, single
configuration values, and colour-only changes. A change can still need verification.

Before editing, note affected callers, imports, types, data shapes, shared state, visual
neighbors, and conventions. After editing, perform appropriate self-checks first, then
brief the reviewer with the request, changed files, affected areas, change type, test or
render instructions, and the checklist below. The reviewer must not edit. Choose one
reviewer by the main difficulty: Terra `medium` for visual/spatial work; Luna `xhigh` for
routine code review; Sol `medium` or `high` when independent engineering judgment is the
main difficulty. A visual review may also inspect relevant code when that helps explain
a defect; reuse current evidence and do not repeat visual passes or add a second reviewer
unless the parts are independently useful.

Review checklist:

- Confirm the request is met without out-of-scope changes; affected touchpoints work;
  relevant empty, missing, boundary, and error cases are covered; conventions hold and
  no debug code remains.
- For layout, measure alignment and spacing against siblings and the existing scale;
  check overlap, overflow, clipping, and readability. For 3D, check intersections,
  grounding, scale, attachment points, and at least two views.
- For logic/data, trace realistic inputs and relevant boundaries, including dates,
  rounding, off-by-one, and empty collections; run covering tests. For UI behavior,
  inspect loading/error/empty states, keyboard/focus,
  accessible names, validation, and affected flows.
- For visual artifacts, check hierarchy, reference fidelity, missing content, crop,
  factual claims, and numbers against their sources or deterministic checks.

Use severity: blocker (wrong result, crash, data loss, breaks another feature, or request
not met); major (visible defect, likely edge case, or convention break likely to cause
bugs); minor (polish or preference). Fix blockers and majors and have the same reviewer
check them, for at most 2 rounds. After round 2, report unresolved blockers/majors rather
than starting a third. Re-reviews cover earlier blockers/majors and affected fixes; do
not reopen settled items or raise new minors. Report minors separately. Return actionable
findings with evidence and file/line or screen/state references; distinguish defects
from preferences. Verdict: **FAIL** on any blocker or major, otherwise **PASS**. The main
agent adjudicates findings and assigns fixes.

## Repository inspection and verification (software projects)

Prefer `rg`, symbol search, and narrow line ranges. Avoid `node_modules`, build/dist and
coverage output, generated/minified assets, irrelevant lockfiles, and unfiltered logs.
Show only relevant errors or summaries.

Tests protect logic that can fail silently: calculations, dates, parsing, transforms,
tricky state, and the main flow. Do not add tests for static markup, styling, copy, simple
components, or anything that only repeats the implementation. Never add snapshot tests. On
prototypes/coursework, add tests only for relevant logic. Flag an existing test for
deletion if it merely repeats the implementation.

Use the narrowest appropriate checks that show the behavior works and directly affected
behavior has not regressed. Prefer typecheck/static analysis/lint,
then targeted tests, targeted DOM/Playwright assertions, and rendered inspection only
when needed. Do not rerun a passing check unless relevant code changes. Do not run the
full suite after every edit.

For frontend work, use visual/browser verification only when rendering or interaction
matters, the visual/responsive requirement changed, deterministic checks are insufficient,
or browser reproduction is needed. One targeted pass is the default; do one targeted
recheck after a defect. Test multiple viewport sizes only when responsiveness changed.
Keep visual inspection with Terra and deterministic browser checks with Luna. Escalate a
visual decision to the main agent only for product/architecture judgment, materially
ambiguous acceptance criteria, or a scope/design decision. Do not claim full accessibility
compliance; state what was and was not inspected.

For web UI, cut taglines, helper text, and labels that repeat the layout. Preserve
editorial/product content and text needed for accessibility or correctness, including
form labels, ARIA text, errors, empty states, and destructive-action confirmations.

## Completion and slides

Stop when the requested behavior is implemented, appropriate checks and necessary
runtime or visual verification pass, and no known material issue remains in scope. Report what
changed, what was actually verified, and material unresolved uncertainty.

For slides and decks, keep one point per slide and state it in the headline. Cut kickers,
subtitles, and lines that repeat or soften the headline; rewrite or split a slide if it
needs them to make sense. Keep a second line only for additional evidence, a number, or a
source. Put explanations and talking points in speaker notes. Section labels belong on
section dividers only.

If an ongoing project has no project-level `AGENTS.md`, offer once to create one; skip
one-off questions, scratch/temp folders, and someone else's repository. If I agree, read
`~/.codex/skills/project-agent-setup/SKILL.md`. If it is unavailable, say so
and preserve the intent: gather user context and repository evidence, verify listed
commands, show the draft before saving, and exclude it in a shared repository unless
told otherwise.
