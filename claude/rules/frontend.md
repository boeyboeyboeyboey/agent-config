---
paths:
  - "**/*.{html,htm,css,scss,sass,less}"
  - "**/*.{tsx,jsx,vue,svelte,astro}"
  - "**/*.{glsl,wgsl,vert,frag}"
  - "**/*.{gltf,glb,obj,fbx,babylon}"
---

# Frontend and 3D work

## UI copy (apps, web apps, websites)

Cut taglines, helper text, and secondary labels or descriptions that only restate what
the layout already shows. If a screen needs them to make sense, fix the layout
(hierarchy, grouping, order, affordances) instead of adding words. This applies to
interface chrome, not to real content: keep the copy a page exists to deliver
(marketing, editorial, product info), plus anything needed for accessibility or
correctness: form labels, `aria-*` text, error and validation messages, empty states,
and confirmations for destructive actions.

## Verification

Prefer deterministic checks before browser-based visual inspection. Use browser or
visual verification only when:

- Correctness depends on actual rendering, shaders, animations, or interaction
- A visual or responsive requirement changed
- Deterministic tests cannot establish the relevant behavior
- Browser reproduction is necessary to diagnose a bug

Delegate routine browser verification, responsive checks, console inspection, and UI
test execution to `worker`. Escalate to `senior` for visual polish, layout fidelity, or
shader output against reference mockups. The `reviewer` takes the single screenshot
pass for a change. Implementing agents use deterministic checks and take screenshots
only to debug a visual failure.

A single targeted browser verification pass is the default. If a defect is found, fix
it and perform one targeted re-check. Do not test multiple viewport sizes unless
responsiveness was directly modified. Escalate visual verification to the main agent
only when product/architectural judgment is required or the subagent reports an
ambiguous failure.

## Visual and spatial changes

A layout, styling or 3D change is done when it fits its surroundings, not just when it
matches the literal request.

- Before editing, note the spacing scale, sibling padding and margins, alignment and
  grid; for 3D, neighbouring meshes, attachment points, scale and ground level.
- After editing, measure against them: gaps and bounding boxes against siblings in the
  DOM, bounding-box or mesh intersection tests against existing parts in 3D.
- Then run the `reviewer` (see "Reviewing changes" in the global CLAUDE.md). Its review
  counts as the single visual verification pass above.
