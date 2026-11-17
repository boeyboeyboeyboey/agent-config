#!/usr/bin/env python3
"""List which slides or PDF pages contain visual content that text extraction misses.

Usage: python3 slide_inventory.py <file.pptx|file.pdf>

Prints one line per slide/page and a final list of pages to view as images.
A page is marked VIEW if it has little text, any non-template picture covering
at least MIN_AREA of the page, a chart, a diagram/SmartArt, or heavy vector drawing.
Pictures that repeat on most pages (logos, template backgrounds) are ignored.
"""
import hashlib
import sys
from collections import Counter

MIN_TEXT = 20        # chars; below this the page is treated as image-only
MIN_AREA = 0.03      # fraction of page area for a picture to count
VECTOR_HEAVY = 40    # curves + rects on a PDF page that suggest a drawn chart/diagram


def is_template(count, total):
    return total >= 3 and count / total > 0.5


def pptx_inventory(path):
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    from pptx.shapes.graphfrm import GraphicFrame

    prs = Presentation(path)
    page_area = prs.slide_width * prs.slide_height
    pages = []

    def walk(shapes, info):
        for sh in shapes:
            if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
                walk(sh.shapes, info)
                continue
            if sh.has_text_frame:
                info["text"] += len(sh.text_frame.text.strip())
            if getattr(sh, "has_table", False) and sh.has_table:
                for row in sh.table.rows:
                    for cell in row.cells:
                        info["text"] += len(cell.text.strip())
            if getattr(sh, "has_chart", False) and sh.has_chart:
                info["charts"] += 1
                continue
            image = None
            try:
                image = sh.image  # pictures and picture placeholders
            except Exception:
                pass
            if image is not None:
                area = (sh.width or 0) * (sh.height or 0) / page_area
                info["pics"].append((hashlib.sha1(image.blob).hexdigest(), area))
            elif isinstance(sh, GraphicFrame) and not sh.has_table:
                info["diagrams"] += 1  # SmartArt or embedded object
            elif sh.shape_type in (MSO_SHAPE_TYPE.EMBEDDED_OLE_OBJECT,
                                   MSO_SHAPE_TYPE.LINKED_OLE_OBJECT,
                                   MSO_SHAPE_TYPE.MEDIA):
                info["diagrams"] += 1

    for slide in prs.slides:
        info = {"text": 0, "pics": [], "charts": 0, "diagrams": 0, "vector": 0}
        walk(slide.shapes, info)
        pages.append(info)
    return pages


def pdf_inventory(path):
    import pdfplumber

    pages = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_area = float(page.width * page.height)
            info = {"text": len((page.extract_text() or "").strip()), "pics": [],
                    "charts": 0, "diagrams": 0,
                    "vector": len(page.curves) + len(page.rects)}
            for im in page.images:
                w, h = im["x1"] - im["x0"], im["bottom"] - im["top"]
                key = (round(im["x0"]), round(im["top"]), round(w), round(h),
                       im.get("srcsize"))
                info["pics"].append((str(key), w * h / page_area))
            pages.append(info)
    return pages


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    low = path.lower()
    if low.endswith(".pptx"):
        pages = pptx_inventory(path)
    elif low.endswith(".pdf"):
        pages = pdf_inventory(path)
    else:
        sys.exit("Unsupported file type: convert .ppt/.key to PDF first (see SKILL.md).")

    total = len(pages)
    seen = Counter()
    for p in pages:
        for key in {k for k, _ in p["pics"]}:
            seen[key] += 1

    to_view = []
    for i, p in enumerate(pages, 1):
        pics = [a for k, a in p["pics"] if not is_template(seen[k], total)]
        big = [a for a in pics if a >= MIN_AREA]
        reasons = []
        if p["text"] < MIN_TEXT:
            reasons.append("little text")
        if big:
            reasons.append(f"{len(big)} picture(s), largest {max(big):.0%}")
        if p["charts"]:
            reasons.append(f"{p['charts']} chart(s)")
        if p["diagrams"]:
            reasons.append(f"{p['diagrams']} diagram/object(s)")
        if p["vector"] >= VECTOR_HEAVY:
            reasons.append(f"vector drawing ({p['vector']} shapes)")
        verdict = "VIEW: " + "; ".join(reasons) if reasons else "text only"
        print(f"p{i}: text={p['text']} chars -> {verdict}")
        if reasons:
            to_view.append(i)

    ignored = sum(1 for k, c in seen.items() if is_template(c, total))
    print(f"\nPages to view as images ({len(to_view)}/{total}): "
          f"{','.join(map(str, to_view)) or 'none'}")
    if ignored:
        print(f"Ignored {ignored} repeated template image(s) (logos/backgrounds).")


if __name__ == "__main__":
    main()
