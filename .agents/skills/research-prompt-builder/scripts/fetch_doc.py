"""Download one company document (annual report, deck, transcript) to a folder.

Usage: python fetch_doc.py <url> <out_dir> [--name file.pdf]

Prints the saved path and size. Skips the download if the file already exists.
Stdlib only.
"""
import os
import sys
import time
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) research-prompt-builder/1.0"


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        sys.exit(__doc__)
    url, out_dir = args[0], args[1]
    name = None
    if "--name" in args:
        name = args[args.index("--name") + 1]
    if not name:
        name = os.path.basename(urllib.parse.urlparse(url).path) or "document.pdf"
    name = "".join(c for c in urllib.parse.unquote(name) if c not in '<>:"/\\|?*')
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, name)
    if os.path.exists(path) and os.path.getsize(path) > 1024:
        print("EXISTS %s (%d bytes)" % (path, os.path.getsize(path)))
        return
    host = urllib.parse.urlparse(url).netloc
    headers = {"User-Agent": UA, "Accept": "*/*"}
    if "bseindia" in host:
        headers["Referer"] = "https://www.bseindia.com/"
    elif "nseindia" in host:
        headers["Referer"] = "https://www.nseindia.com/"
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if name.lower().endswith(".pdf") and not data[:5].startswith(b"%PDF"):
                raise ValueError("response is not a PDF (first bytes %r)" % data[:20])
            with open(path, "wb") as f:
                f.write(data)
            print("SAVED %s (%d bytes)" % (path, len(data)))
            return
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(2 * (attempt + 1))
    sys.exit("FAILED %s: %s" % (url, last))


if __name__ == "__main__":
    main()
