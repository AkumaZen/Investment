"""Page-tagged text, page search and page images from a PDF.

Usage:
  python pdf_pages.py <pdf> --info
  python pdf_pages.py <pdf> --text [--pages 3-7,12] [--out file.txt]
  python pdf_pages.py <pdf> --find "capacity utilisation"
  python pdf_pages.py <pdf> --render --pages 12-14 --out <dir> [--zoom 2]

Uses PyMuPDF if installed, else pypdf for text. Rendering needs PyMuPDF.
"""
import os
import sys


def parse_pages(spec, total):
    if not spec:
        return list(range(1, total + 1))
    pages = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-", 1)
            pages.extend(range(int(a), int(b) + 1))
        elif part.strip():
            pages.append(int(part))
    return [p for p in pages if 1 <= p <= total]


def opt(args, flag, default=None):
    return args[args.index(flag) + 1] if flag in args else default


def page_texts(pdf, pages_spec):
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(pdf)
        pages = parse_pages(pages_spec, doc.page_count)
        return doc.page_count, [(p, doc[p - 1].get_text()) for p in pages]
    except ImportError:
        from pypdf import PdfReader
        r = PdfReader(pdf)
        pages = parse_pages(pages_spec, len(r.pages))
        return len(r.pages), [(p, r.pages[p - 1].extract_text() or "") for p in pages]


def main():
    args = sys.argv[1:]
    if not args or not os.path.exists(args[0]):
        sys.exit(__doc__)
    pdf = args[0]
    if "--info" in args:
        total, texts = page_texts(pdf, None)
        empty = [p for p, t in texts if len(t.strip()) < 40]
        print("pages: %d" % total)
        print("pages with little or no text (likely scans or charts, render these): %s" % (empty or "none"))
    elif "--find" in args:
        term = opt(args, "--find").lower()
        _, texts = page_texts(pdf, None)
        for p, t in texts:
            low = t.lower()
            i = low.find(term)
            if i >= 0:
                snippet = " ".join(t[max(0, i - 120): i + 160].split())
                print("p.%d: ...%s..." % (p, snippet))
    elif "--text" in args:
        _, texts = page_texts(pdf, opt(args, "--pages"))
        out = "\n".join("=== PAGE %d ===\n%s" % (p, t.strip()) for p, t in texts)
        target = opt(args, "--out")
        if target:
            with open(target, "w", encoding="utf-8") as f:
                f.write(out)
            print("Wrote %s" % target)
        else:
            sys.stdout.reconfigure(encoding="utf-8")
            print(out)
    elif "--render" in args:
        import fitz
        out_dir = opt(args, "--out", ".")
        zoom = float(opt(args, "--zoom", "2"))
        os.makedirs(out_dir, exist_ok=True)
        doc = fitz.open(pdf)
        stem = os.path.splitext(os.path.basename(pdf))[0]
        for p in parse_pages(opt(args, "--pages"), doc.page_count):
            pix = doc[p - 1].get_pixmap(matrix=fitz.Matrix(zoom, zoom))
            path = os.path.join(out_dir, "%s_p%03d.png" % (stem, p))
            pix.save(path)
            print(path)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
