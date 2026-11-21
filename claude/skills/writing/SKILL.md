---
name: writing
description: Style rules for documents, pages, reports, slides, READMEs and UI copy. Use whenever you write or edit text longer than a chat reply, and when reviewing writing for AI-sounding patterns.
---

# Writing

Apply with the Writing section of `~/.claude/CLAUDE.md`. This file holds the full
phrase list, word list and examples.

Cut anything that adds no information:
- Descriptions that restate their heading or label.
- Taglines, mic-drop one-liners, and recap endings ("In summary", "Overall").
- Chatbot openers and closers ("Certainly!", "Great question", "You're absolutely
  right", "It's worth noting", "I hope this helps", "Let me know if"). End with a
  question only when a real decision is pending.
- Signposting and setups: "In this section we'll", "Let's dive in", "Below is a
  breakdown", "The catch?", "Here's the thing:", "Why this matters".
- Trailing "-ing" commentary (", highlighting its importance", ", ensuring",
  ", reflecting"). If the point matters, give it its own sentence with evidence.
- Inflated significance ("plays a vital role", "marks a pivotal moment", "reflects
  broader trends", "has shaped discussions about", "sets the stage for") and empty
  intensifiers (truly, incredibly, seamlessly, quietly).
- The challenges formula ("Despite these challenges", "Looking ahead"). Name a real
  problem with specifics or leave it out.
Test: if deleting a line loses no information, delete it. Keep real content and
anything needed for accessibility or correctness.

Don't define things by what they aren't when nobody said they were: no "It's not X,
it's Y", "not just X but also Y", decorative "Y rather than X", or unprompted "should
not be confused with". State Y directly.

Change reports (commits, PRs, "what I changed"): list the concrete changes. No
"refined", "enhanced", "streamlined", "improved clarity", "ensured", "while preserving".

Never leave placeholders ("[Your Name]", "(add link here)") in finished text. If
something is missing, ask or flag it at the top.

Plain words over impressive ones: "used", not "utilized"; "wrote", not "authored".
Avoid: delve, tapestry, testament, leverage, robust, seamless, elevate, unlock,
pivotal, landscape, crucial, enhance, foster, garner, showcase, underscore, highlight
(as a verb), bolster, intricate, interplay, meticulous, vibrant, multifaceted, align
with, and "Additionally" to open a sentence. Rewrite the sentence plainly instead of
swapping in a synonym. Exception: a word on this list is fine when it's the precise
technical term (a robust estimator, a landscape survey).
