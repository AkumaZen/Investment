"""Screenshot the v3 report with headless Edge, a few pages at a time.

Run:  python -I qa_shots.py [desktop|mobile] [first_page] [last_page]
Writes PNGs into qa/. Pages outside the range are hidden with injected CSS,
because a single headless screenshot cannot exceed ~16k px.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
mode = sys.argv[1] if len(sys.argv) > 1 else "desktop"
a = int(sys.argv[2]) if len(sys.argv) > 2 else 1
b = int(sys.argv[3]) if len(sys.argv) > 3 else 23
width, height = (1200, 7600) if mode == "desktop" else (390, 7600)

src = open(os.path.join(HERE, "augmont-report.html"), encoding="utf-8").read()
hide = "".join(f"#p{n}{{display:none}}" for n in range(1, 40) if not (a <= n <= b))
os.makedirs(os.path.join(HERE, "qa"), exist_ok=True)
tmp = os.path.join(HERE, "qa", "_tmp.html")
open(tmp, "w", encoding="utf-8").write(src.replace("</style>", hide + "</style>", 1))
if mode == "mobile":  # headless Edge has a minimum window width, so frame the page at a true 390px
    frame = os.path.join(HERE, "qa", "_frame.html")
    open(frame, "w", encoding="utf-8").write(
        '<html><body style="margin:0;background:#888"><iframe src="_tmp.html" style="width:390px;height:7600px;border:0;background:#fff"></iframe></body></html>')
    tmp = frame
    width = 600
out = os.path.join(HERE, "qa", f"{mode}-p{a:02d}-{b:02d}.png")
subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                f"--window-size={width},{height}", f"--screenshot={out}", "file:///" + tmp.replace("\\", "/")],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(out)
