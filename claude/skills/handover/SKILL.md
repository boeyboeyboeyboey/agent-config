---
name: handover
description: Write a handover file and a kickoff prompt so a fresh chat can continue the current work. Use when the user asks for a handover or accepts an offer of one (offers are made at about 60% context or when a milestone is finished).
---

Write the handover in the project's handover folder if it has one (e.g.
`.local-handover/`), otherwise in the working folder.

The handover file covers:
- Current state: what exists and works now.
- Decisions made and why.
- What's verified and what isn't.
- Open work, split into small stages, each with a pass criterion.
- The exact next step.

Write it so a fresh chat with no context can continue from it.

Alongside it, write a short kickoff prompt, both in your reply and saved next to the
handover. The kickoff says:
- read the handover file yourself (give its path) and delegate other reading;
- which repo docs to load;
- what's authorized and what isn't;
- the hard guardrails;
- what the first response should be.

Keep the details in the handover. The kickoff points to it rather than repeating it.
