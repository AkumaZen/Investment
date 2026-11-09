"""Extract text of every raw PDF to docs/CONCORDBIO/text/<name>.txt with page markers; print an index."""
import fitz, os, sys, hashlib, json
RAW = "docs/CONCORDBIO/raw"; OUT = "docs/CONCORDBIO/text"
os.makedirs(OUT, exist_ok=True)
idx = []
for f in sorted(os.listdir(RAW)):
    p = os.path.join(RAW, f); d = fitz.open(p)
    parts = []; chars = 0
    for i, pg in enumerate(d):
        t = pg.get_text(); chars += len(t.strip())
        parts.append("\n\n=== PAGE %d ===\n%s" % (i + 1, t))
    open(os.path.join(OUT, f[:-4] + ".txt"), "w", encoding="utf-8").write("".join(parts))
    first = " ".join(d[0].get_text().split())[:220]
    h = hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]
    idx.append(dict(file=f, pages=len(d), chars=chars, sha=h, first=first))
json.dump(idx, open("data/doc-index.json", "w"), indent=1)
for r in idx: print(r["file"], r["pages"], r["chars"], r["sha"], "|", r["first"][:160])
