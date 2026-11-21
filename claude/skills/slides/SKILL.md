---
name: slides
description: Read or make slides. Use whenever you need to look at, search, summarise or cite a slide deck or lecture PDF (.pptx, .key, .pdf), and whenever you write or edit slides.
---

## Reading slides

"Look at the slides" always means: extract the text where there is any, and view the
page as an image where there isn't. "Image-only, no extractable text" is never a final
answer. It is the signal to render the page and look at it.

1. Extract text first.
   - `.pptx`: python-pptx, every shape's text plus speaker notes, per slide.
   - `.pdf`: pdfplumber (or pypdf), per page.
   - `.key`: export to PDF first (step 3), then treat it as a PDF.
2. Find every page with visual content by running
   `python3 ~/.claude/skills/slides/scripts/slide_inventory.py <file.pptx|file.pdf>`.
   It marks a page VIEW if it has little text, a picture over 3% of the page, a chart,
   SmartArt or an embedded object, or more drawn shapes or lines than the deck usually
   has (shape diagrams, flowcharts), including pages that are half text and half image.
   It ignores images whose content repeats on most pages (logos, backgrounds).
   Its list is the minimum you must view, not a guarantee. Also view:
   - every page, when the deck is 15 pages or fewer (the script says so);
   - any page whose extracted text reads like parts of a figure: short scattered labels,
     "as shown", "see diagram", arrows, axis or legend words;
   - any page where the task depends on visuals (diagrams, charts, layouts).
   If the script fails, view every page that has any picture, chart or drawing.
3. Render and view those pages.
   - `.pdf`: open it with Read and the `pages` parameter (up to 20 pages per call).
   - `.pptx`: `soffice --headless --convert-to pdf --outdir <scratch dir> <file>`, then
     Read the PDF pages.
   - `.key`: `osascript -e 'tell application "Keynote" to export (open POSIX file
     "<abs path>") to POSIX file "<scratch dir>/<name>.pdf" as PDF'`, then Read the PDF.
   Put converted files in the scratchpad, never next to the original.
4. If rendering fails, try the other route (for example, export .pptx through Keynote or
   PowerPoint). Report a page as unreadable only after rendering failed, with the error.
5. If there are too many image pages to view, view the ones relevant to the task and list
   the rest as unchecked by number.
6. In the report, mark content read from an image as "(from image)", and state coverage:
   which pages were read as text, viewed as images, or not checked.

## Making slides

One point per slide, and the headline states it. Cut kickers and subtitles that restate
or soften it; if needed, rewrite the headline or split the slide. A second line only for
a number, a source, or evidence. Explanations go in speaker notes. Section labels only on
divider slides.
