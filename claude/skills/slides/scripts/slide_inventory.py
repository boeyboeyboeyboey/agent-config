#!/usr/bin/env python3
"""List which slides or PDF pages contain visual content that text extraction misses.

Usage: python3 slide_inventory.py <file.pptx|file.pdf>

Prints one line per slide/page and a final list of pages that must be viewed as images.
The list is a minimum, not a guarantee: see the slides skill for when to view more.

A page is marked VIEW if it has little text, a non-template picture covering at least
MIN_AREA of the page, a chart, a diagram/SmartArt/embedded object, or more drawn shapes
or lines than the deck's plainer slides (shape diagrams, flowcharts, annotated figures).
Pictures whose content repeats on most pages (logos, backgrounds) are ignored.
"""
import hashlib
import sys
from collections import Counter

MIN_TEXT = 20         # chars; below this the page is treated as image-only
MIN_AREA = 0.03       # fraction of page area for a picture to count
PPTX_EXTRA_SHAPES = 3 # drawn shapes above the deck baseline that suggest a diagram
PPTX_EXTRA_LINES = 1  # connectors/lines/freeforms above the deck baseline
PPTX_MIN_SHAPES = 3   # always flag this many drawn shapes...
PPTX_MIN_LINES = 1    # ...or any connector/line, whatever the rest of the deck does
PDF_EXTRA_VECTOR = 8  # rects+lines+curves above the deck baseline
PDF_MIN_VECTOR = 100  # always flag this much drawing (LibreOffice text pages ~54)
SHORT_DECK = 15       # at or below this many pages, view every page


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
            st = sh.shape_type
            if st == MSO_SHAPE_TYPE.GROUP:
                walk(sh.shapes, info)
                continue
            if sh.has_text_frame:
                info["text"] += len(sh.text_frame.text.strip())
            if st == MSO_SHAPE_TYPE.AUTO_SHAPE:
                info["shapes"] += 1
            elif st in (MSO_SHAPE_TYPE.LINE, MSO_SHAPE_TYPE.FREEFORM) or \
                    type(sh).__name__ == "Connector":
                info["lines"] += 1
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
            elif st in (MSO_SHAPE_TYPE.EMBEDDED_OLE_OBJECT,
                        MSO_SHAPE_TYPE.LINKED_OLE_OBJECT, MSO_SHAPE_TYPE.MEDIA):
                info["diagrams"] += 1

    for slide in prs.slides:
        info = {"text": 0, "pics": [], "charts": 0, "diagrams": 0,
                "shapes": 0, "lines": 0, "vector": 0}
        walk(slide.shapes, info)
        pages.append(info)
    return pages


def pdf_image_key(im):
    try:
        stream = im["stream"]
        raw_data = stream.get_rawdata()
        color_space = stream.get_any(("CS", "ColorSpace"))
    except (AttributeError, KeyError, OSError):
        return None
    if not raw_data:
        return None
    color_space_name = getattr(color_space, "name", None)
    device_names = {"DeviceGray", "DeviceRGB", "DeviceCMYK", "G", "RGB", "CMYK"}
    if color_space_name is not None and color_space_name not in device_names:
        # The same resource name can resolve differently on each page.
        return None
    # Palettes, decode settings, and masks can change the same raw pixels.
    return hashlib.sha1(raw_data).hexdigest(), repr(stream.attrs)


def pdf_inventory(path):
    import pdfplumber

    pages = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_area = float(page.width * page.height)
            info = {"text": len((page.extract_text() or "").strip()), "pics": [],
                    "charts": 0, "diagrams": 0, "shapes": 0, "lines": 0,
                    "vector": len(page.curves) + len(page.rects) + len(page.lines)}
            for im in page.images:
                w, h = im["x1"] - im["x0"], im["bottom"] - im["top"]
                info["pics"].append((pdf_image_key(im), w * h / page_area))
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
        for key in {k for k, _ in p["pics"] if k is not None}:
            seen[key] += 1
    # Baseline = lower quartile, so a deck where most slides are diagrams still
    # flags them (a median would make diagrams the norm and flag none).
    def lower_quartile(key):
        vals = sorted(p[key] for p in pages)
        return vals[len(vals) // 4] if vals else 0
    base = {k: lower_quartile(k) for k in ("shapes", "lines", "vector")}

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
        if (p["shapes"] - base["shapes"] >= PPTX_EXTRA_SHAPES
                or p["lines"] - base["lines"] >= PPTX_EXTRA_LINES
                or p["shapes"] >= PPTX_MIN_SHAPES or p["lines"] >= PPTX_MIN_LINES):
            reasons.append(f"drawn diagram ({p['shapes']} shapes, {p['lines']} lines)")
        if (p["vector"] - base["vector"] >= PDF_EXTRA_VECTOR
                or p["vector"] >= PDF_MIN_VECTOR):
            reasons.append(f"vector drawing ({p['vector']} shapes)")
        verdict = "VIEW: " + "; ".join(reasons) if reasons else "text only"
        print(f"p{i}: text={p['text']} chars -> {verdict}")
        if reasons:
            to_view.append(i)

    ignored = sum(1 for k, c in seen.items() if is_template(c, total))
    print(f"\nMust view as images ({len(to_view)}/{total}): "
          f"{','.join(map(str, to_view)) or 'none'}")
    if ignored:
        print(f"Ignored {ignored} repeated template image(s) (logos/backgrounds).")
    if 0 < total <= SHORT_DECK:
        print(f"Short deck ({total} pages): view every page.")


if __name__ == "__main__":
    main()
