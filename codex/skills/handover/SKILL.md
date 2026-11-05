---
name: handover
description: Write a context handover and kickoff prompt when a user accepts a handover offer at a milestone or near context limits.
---

# Handover

Use when the main agent offers a handover because context is around 60% full or a
milestone has finished, and the user accepts. Do not interrupt ordinary work to create
one without that trigger and acceptance.

## Write the handover

Use the project's established handover folder if one exists; otherwise use
`.local-handover/`. Make the handover useful to a fresh chat with no prior context. Cover:

- Current state and the user's objective
- Decisions made and why, including relevant constraints
- What is verified, how it was verified, and what remains unverified
- Open work split into small stages, each with observable pass criteria
- The exact next step
- What is authorized, what is not authorized, and hard guardrails
- Relevant project documents to load, linked by path with a short reason

Do not turn the handover into a transcript or repeat repository documentation. Keep
details in the handover so the kickoff prompt can stay short.

## Write the kickoff prompt

Save a concise prompt beside the handover and include it in the reply. Tell the next
agent to read the handover itself, delegate other reading when useful, load the named
project documents, respect the stated permissions and guardrails, and begin with the
specified first response or next step. Include the handover path in the prompt.

Do not imply that the next agent has permission for external or irreversible actions
unless the handover records that authorization.
