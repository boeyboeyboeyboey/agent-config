# Model routing and evidence

Reviewed 5 November 2026. These are task-routing choices for this setup, not a claim
that one model wins every task. Benchmark versions and effort settings matter; model
aliases can change. Recheck the actual model offered by the account before reuse.

## Codex

| Role | Choice | Reason and limit |
| --- | --- | --- |
| Narrow reconnaissance, commands, repeatable checks | Luna `high` | Keep bounded work on the smaller model. OpenAI recommends Luna for scoped tasks and triage. `high` is the local default, not a benchmark-derived optimum. |
| Scoped implementation and routine code review | Luna `xhigh` | A local escalation for harder bounded work. Review difficulty and evidence decide when to use Sol; the author's model alone does not. |
| Complex engineering, planning, difficult review | Sol `medium`/`high` | Matches OpenAI's guidance for complex technical work. Main-model configuration currently uses `xhigh`; delegated roles are separately scoped. |
| Images, screens, bounded app workflows | Terra `medium` | Officially supported visual reasoning and computer use; `medium` is the documented starting effort. Higher efforts remain bounded exceptions. |
| Longer drafts and revisions | Terra `medium` | Clear prose from a brief and relevant source material. The main agent owns analysis, decisions, and final fact-checking. |
| Exceptional read-only critique | Astra `low`, approval-only | A personal usage-control rule. No benchmark establishes that this is the universally best planning configuration. |

Sources: OpenAI's [model-selection guide](https://developers.openai.com/api/docs/guides/model-selection)
and [Terra model documentation](https://developers.openai.com/api/docs/models/gpt-6.1-terra).

Terra's launch evaluation covers professional app workflows in Agents' Last Exam,
desktop tasks in OSWorld 2.1, and image reasoning in MMMU-Pro. That supports using it
for interpreting screenshots, checking observable visual defects, and operating apps.
It does not directly establish superior aesthetic taste or general UI/UX judgment.
Exact chart-only scores were not visually verified here and are not reproduced.
[Terra launch and evaluations](https://openai.com/index/introducing-gpt-6-1-terra/)

For layout review, use explicit criteria: alignment, clipping, spacing, reference
fidelity, readable text, and task completion. Broader product and design decisions
remain judgments to assess against the user's goals.

Writing evidence reviewed 6 November 2026. OpenAI recommends Terra for concise
writing from supplied material. On ToneBench at `medium`, GPT-6.1 Terra scored
slightly higher on clarity than GPT-5.6 Terra and GPT-6.1 Sol. Both scored higher on
matching the author's voice and on the overall writing score. ToneBench uses ten
YouTube briefs in one creator's voice, so this setup treats Terra as a candidate
for drafting website copy, speaker notes, scripts, and reports. Medium is the
existing starting effort. [OpenAI writing guidance](https://developers.openai.com/api/docs/guides/model-selection#when-to-consider-gpt-61-terra)
· [ToneBench results](https://benchmark.towardsai.com/compare/family-openai.html)

## Claude Code

These files target Claude Code's user-level instructions and custom agents.

| Agent | Configured model and effort | Reason and limit |
| --- | --- | --- |
| `scout` | `haiku`, `medium` | Narrow reading, search, and summaries. Anthropic positions Haiku for fast, repeatable work. |
| `worker` | `haiku`, `medium` | Execution from a clear specification; stop or escalate when the task needs design decisions. |
| `senior` | `sonnet`, `high` | Bounded implementation or analysis requiring more judgment. Keep tasks small and checkable. |
| `reviewer` | `sonnet`, `high` | Independent review without editing. A stronger review default is a local policy, not proof that errors will always be caught. |

The live instruction files already declare these aliases and effort levels. Current
Anthropic guidance identifies Haiku 5.5 as the smaller model and Sonnet 5.5 as a
general coding/work model, with default efforts of `medium` and `high`, respectively.
Aliases and actual account availability can vary; benchmark results for version 5.5
do not prove which version a running session resolves.
[Model selection](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
and [Claude Code model configuration](https://code.claude.com/docs/en/model-config)

The main model is selected in Claude; the inspected settings do not pin one. The
public package preserves the existing restriction against Opus subagents. That is a
usage preference, not a claim that Sonnet outperforms Opus. Agent descriptions and
frontmatter guide delegation, but static files alone do not prove dispatch.
[Custom subagent configuration](https://code.claude.com/docs/en/sub-agents)

Budget: Claude Pro, with no additional paid usage authorized. Confirm models in the
account's picker and use the intended subscription login. API-key billing and
subscription allowance are different. Fable 5.1 uses paid usage credits outside
Pro's included limits, so it is not introduced into this setup.
[Claude Code model usage](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)
and [Fable plan billing](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)

## Independent benchmarks

| Source | Observed result | What it supports |
| --- | --- | --- |
| [Artificial Analysis Coding Agent Index](https://artificialanalysis.ai/agents/coding-agents/comparisons/claude-code-vs-codex) | Claude Code: Haiku 5.5 `max` 37, Sonnet 5.5 `max` 59, Opus 5.5 `max` 62. Codex: Luna `max` 31, Terra `medium` 42 / `max` 48, Sol `max` 54, Astra `max` 55. | Capability trade-offs on repository changes, terminal tasks, and repository questions. This measures model plus harness; most settings differ from this package's defaults. It does not isolate scouting, code-review quality, or visual critique. |
| [Artificial Analysis MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro) | Academic image-and-text reasoning across disciplines. | Evidence about multimodal reasoning. It is not a UI navigation or aesthetic-review test. |
| [FrontierCUA](https://frontiercua.com/) | On its 15-workflow v0 benchmark, Sol 6.1 `high` scored 46.7% pass@1 and Opus 5.5 `high` 36.0%. Terra was not listed in the reviewed comparison. | Evidence about screenshot-based GUI task completion. It cannot rank an absent model or establish design taste. |

The coding index combines FrontierCode, Terminal-Bench, and SWE-Atlas-QnA. Its
composite score is not a percentage of all coding tasks solved. See the
[index methodology](https://artificialanalysis.ai/methodology/coding-agents-benchmarking).
FrontierCUA's small task set and GUI-only constraints also limit generalization:
[methodology](https://frontiercua.com/methodology/).

Per-task API dollar estimates are not estimates of Claude Pro or Codex subscription
allowance. Do not compare those figures as if they were interchangeable.

## Practitioner review

[DanManREAL's three blind trials](https://danmanreal.com/tests/terra-vs-opus-three-blind-trials)
compared Terra and Opus at `max`. Terra had shorter run times; blind redesign
preferences favored Opus. Neither model met all acceptance criteria. This is a
small, self-run comparison, with one run per configuration
and a changed setup in the third trial. It tests generated output, not the ability
to critique a supplied design. Treat it as a useful counterexample to a universal
"best visual model" claim, not a leaderboard. The author's credentials were not
independently verified.

## Validation boundary

- Claude files: static configuration and policy, prepared from the existing setup.
  Native Claude execution and account model availability are unverified from this environment.
- Read-only roles express a policy. Tool denylists do not guarantee a read-only
  sandbox when a shell remains available.
- Codex Git rules: selected command prefixes, with recorded gaps in
  [the verification cases](../verification/git-policy-cases.json).
- No benchmark reruns, API calls, extra usage credits, or live settings changes.
- Revisit routing using representative tasks and explicit pass criteria; preserve
  the model version, effort, harness, failures, and elapsed time when comparing results.
