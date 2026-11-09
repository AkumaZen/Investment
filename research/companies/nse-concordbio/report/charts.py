"""Dependency-free inline-SVG chart helpers for the Concord Biotech report.

Adapted from research/companies/nse-augmont/v3/charts.py with the validated teal palette.
Every function returns an <svg> string that scales to its container width.
Rules kept here: one y-axis per chart (no dual-axis helper), labelled values,
a <title> tooltip on every data mark, estimates hatched, guidance drawn as an outlined band.
"""
from html import escape

TEAL = "#0E5A63"      # brand: headings and bands only
PRIMARY = "#00849E"   # series 1 (thesis series)
SECOND = "#C77A1A"    # series 2
THIRD = "#7A68B5"     # series 3
FOURTH = "#5E9E3C"    # series 4
GREY = "#A9B1BD"      # context series
GREY_LT = "#E6E9EE"
AXIS = "#9AA3AE"
RED = "#B23A3A"
GREEN = "#2F7D5B"
INK = "#1F2733"
MUTED = "#5F6873"
FONT = "Calibri, Carlito, 'Segoe UI', Arial, sans-serif"
_ID = [0]


def _uid(p):
    _ID[0] += 1
    return f"{p}{_ID[0]}"


def _fmt(v, dec=0):
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    from decimal import Decimal, ROUND_HALF_UP
    q = Decimal(1).scaleb(-dec)
    s = f"{Decimal(str(abs(v))).quantize(q, rounding=ROUND_HALF_UP):,.{dec}f}"
    return ("-" if v < 0 else "") + s


def _svg(w, h, body, label):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" '
            f'style="width:100%;height:auto;display:block;font-family:{FONT}">'
            f'<title>{escape(label)}</title>{body}</svg>')


def _text(x, y, s, size=11, fill=INK, anchor="middle", weight="normal", italic=False):
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}"{st}>{escape(str(s))}</text>')


def _tip(s):
    return f"<title>{escape(s)}</title>"


def _nice_max(m):
    if m <= 0:
        return 1
    import math
    p = 10 ** math.floor(math.log10(m))
    for k in (1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10):
        if k * p >= m:
            return k * p
    return 10 * p


def _hatch(pid, color):
    return (f'<pattern id="{pid}" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            f'<rect width="6" height="6" fill="#fff"/><line x1="0" y1="0" x2="0" y2="6" stroke="{color}" stroke-width="2.2"/></pattern>')


def _legend_rows(items, x, w):
    """Number of rows the legend needs to fit inside width w."""
    rows, lx = 1, x
    for nm, _, _ in items:
        iw = 30 + len(nm) * 5.4
        if lx > x and lx + iw - 12 > w - 4:
            rows, lx = rows + 1, x
        lx += iw
    return rows


def _legend(items, x, y, w=None):
    """items: list of (name, color, kind) kind in {'box','hatch','line','dash','band'}.
    Wraps onto a new 14px row when an item would cross width w."""
    out, lx = [], x
    for nm, col, kind in items:
        iw = 30 + len(nm) * 5.4
        if w and lx > x and lx + iw - 12 > w - 4:
            lx, y = x, y + 14
        if kind == "line":
            out.append(f'<line x1="{lx}" x2="{lx+14}" y1="{y-4}" y2="{y-4}" stroke="{col}" stroke-width="2"/>')
        elif kind == "dash":
            out.append(f'<line x1="{lx}" x2="{lx+14}" y1="{y-4}" y2="{y-4}" stroke="{col}" stroke-width="2" stroke-dasharray="4,3"/>')
        elif kind == "band":
            out.append(f'<rect x="{lx}" y="{y-9}" width="14" height="10" fill="{col}" fill-opacity=".12" stroke="{col}" stroke-dasharray="3,2"/>')
        else:
            out.append(f'<rect x="{lx}" y="{y-9}" width="10" height="10" fill="{col}" rx="2"/>')
        out.append(_text(lx + 18, y, nm, 10.5, INK, anchor="start"))
        lx += iw
    return "".join(out)


def bars(cats, vals, label, *, colors=None, dec=0, unit="", w=520, h=240, hatch=None,
         highlight=None, value_labels=None, axis_note=None, notes=None, tips=None):
    """Vertical bars from a zero baseline. hatch: indices drawn as estimates.
    highlight: index (or set) drawn in PRIMARY, the rest GREY, when colors is not given.
    notes: {index: text} short annotation above the bar."""
    hatch = hatch or set()
    hl = highlight if isinstance(highlight, (set, list, tuple)) else ({highlight} if highlight is not None else None)
    pad_l, pad_r, pad_t, pad_b = 10, 10, 30 if notes else 20, 30
    n = len(vals)
    hi = _nice_max(max(v for v in vals if v is not None) * 1.1)
    ph, pw = h - pad_t - pad_b, w - pad_l - pad_r
    slot = pw / n
    bw = min(48, slot * 0.6)

    def y(v):
        return pad_t + ph * (hi - v) / hi

    pid = _uid("h")
    out = [f"<defs>{_hatch(pid, PRIMARY)}</defs>"]
    for i, (c, v) in enumerate(zip(cats, vals)):
        cx = pad_l + slot * (i + 0.5)
        fs = 11 if slot > 50 else 9.5
        out.append(_text(cx, h - 11, c, fs, MUTED))
        if v is None:
            out.append(_text(cx, y(0) - 6, "n/d", 9.5, MUTED, italic=True))
            continue
        col = colors[i] if colors else (PRIMARY if (hl is None or i in hl) else GREY)
        fill = f"url(#{pid})" if i in hatch else col
        stroke = f' stroke="{PRIMARY}" stroke-width="1"' if i in hatch else ""
        tip = tips[i] if tips else f"{c}: {_fmt(v, dec)}{unit}"
        out.append(f'<rect x="{cx-bw/2:.1f}" y="{y(v):.1f}" width="{bw:.1f}" height="{max(y(0)-y(v),0.8):.1f}" '
                   f'fill="{fill}"{stroke} rx="2">{_tip(tip)}</rect>')
        lab = value_labels[i] if value_labels else _fmt(v, dec) + unit
        out.append(_text(cx, y(v) - 5, lab, 11 if slot > 40 else 9.5, INK, weight="bold"))
        if notes and i in notes:
            out.append(_text(cx, y(v) - 18, notes[i], 9.5, SECOND, weight="bold"))
    out.append(f'<line x1="{pad_l}" x2="{w-pad_r}" y1="{y(0):.1f}" y2="{y(0):.1f}" stroke="{AXIS}" stroke-width="1"/>')
    if axis_note:
        out.append(_text(w - pad_r, 12, axis_note, 9.5, MUTED, anchor="end", italic=True))
    return _svg(w, h, "".join(out), label)


def grouped(cats, series, label, *, dec=0, unit="", w=520, h=240, hatch_series=None):
    """series: list of (name, values, color). hatch_series: names drawn hatched as estimates."""
    hatch_series = hatch_series or set()
    pad_l, pad_r, pad_t, pad_b = 10, 10, 34, 30
    pad_t += 14 * (_legend_rows([(nm, col, "box") for nm, _, col in series], pad_l, w) - 1)
    allv = [v for _, vs, _ in series for v in vs if v is not None]
    hi = _nice_max(max(allv) * 1.1)
    ph, pw = h - pad_t - pad_b, w - pad_l - pad_r
    slot = pw / len(cats)
    k = len(series)
    bw = min(30, slot * 0.76 / k)

    def y(v):
        return pad_t + ph * (hi - v) / hi

    defs, pats = [], {}
    for nm, _, col in series:
        if nm in hatch_series:
            pats[nm] = _uid("g")
            defs.append(_hatch(pats[nm], col))
    out = [f"<defs>{''.join(defs)}</defs>"]
    for i, c in enumerate(cats):
        cx = pad_l + slot * (i + 0.5)
        for j, (nm, vs, col) in enumerate(series):
            v = vs[i]
            x = cx - bw * k / 2 + j * bw
            if v is None:
                continue
            fill = f"url(#{pats[nm]})" if nm in pats else col
            stroke = f' stroke="{col}"' if nm in pats else ""
            out.append(f'<rect x="{x+1:.1f}" y="{y(v):.1f}" width="{bw-2:.1f}" height="{max(y(0)-y(v),0.8):.1f}" '
                       f'fill="{fill}"{stroke} rx="2">{_tip(f"{c}, {nm}: {_fmt(v, dec)}{unit}")}</rect>')
            if bw >= 15:
                out.append(_text(x + bw / 2, y(v) - 4, _fmt(v, dec) + unit, 9.5 if bw < 22 else 10.5, INK, weight="bold"))
        out.append(_text(cx, h - 11, c, 11 if slot > 50 else 9.5, MUTED))
    out.append(f'<line x1="{pad_l}" x2="{w-pad_r}" y1="{y(0):.1f}" y2="{y(0):.1f}" stroke="{AXIS}"/>')
    out.append(_legend([(nm, col, "box") for nm, _, col in series], pad_l, 14, w))
    return _svg(w, h, "".join(out), label)


def lines(cats, series, label, *, dec=0, unit="", w=520, h=240, band=None, ymin=None, ymax=None,
          end_labels=True, all_labels=False):
    """Line chart on one axis. series: list of (name, values, color, dashed).
    band: (lo, hi, text) drawn as an outlined guidance band [G]. None values leave gaps."""
    pad_l, pad_r, pad_t, pad_b = 34, 46 if end_labels else 14, 30, 30
    leg = [(s[0], s[2], "dash" if s[3] else "line") for s in series]
    if band:
        leg.append(("Guidance [G]", SECOND, "band"))
    pad_t += 14 * (_legend_rows(leg, pad_l, w) - 1)
    allv = [v for s in series for v in s[1] if v is not None] + (list(band[:2]) if band else [])
    lo = ymin if ymin is not None else 0
    hi = ymax if ymax is not None else _nice_max(max(allv) * 1.08)
    ph, pw = h - pad_t - pad_b, w - pad_l - pad_r
    n = len(cats)
    inset = 18 if all_labels else 10      # keep the first point's label clear of the y-axis ticks
    step = (pw - 2 * inset) / (n - 1) if n > 1 else pw

    def X(i):
        return pad_l + inset + step * i

    def Y(v):
        return pad_t + ph * (hi - v) / (hi - lo)

    out = []
    # gridlines: 4 steps
    for t in range(5):
        gv = lo + (hi - lo) * t / 4
        out.append(f'<line x1="{pad_l}" x2="{w-pad_r}" y1="{Y(gv):.1f}" y2="{Y(gv):.1f}" stroke="{GREY_LT}"/>')
        out.append(_text(pad_l - 5, Y(gv) + 3.5, _fmt(gv, 0) + unit, 9.5, MUTED, anchor="end"))
    if band:
        b0, b1, bt = band
        out.append(f'<rect x="{pad_l}" y="{Y(b1):.1f}" width="{pw:.1f}" height="{Y(b0)-Y(b1):.1f}" fill="{SECOND}" '
                   f'fill-opacity=".10" stroke="{SECOND}" stroke-dasharray="4,3" stroke-width="1">{_tip(bt)}</rect>')
        out.append(_text(pad_l + 4, Y(b1) - 4, bt, 9.5, "#8A520C", anchor="start", weight="bold"))
    for i, c in enumerate(cats):
        out.append(_text(X(i), h - 11, c, 10.5 if step > 50 else 9, MUTED))
    ends = []   # end labels, spread apart after all series are drawn
    for nm, vs, col, dashed in series:
        segs, cur = [], []
        for i, v in enumerate(vs):
            if v is None:
                if cur:
                    segs.append(cur)
                cur = []
            else:
                cur.append((X(i), Y(v)))
        if cur:
            segs.append(cur)
        da = ' stroke-dasharray="5,4"' if dashed else ""
        for sg in segs:
            if len(sg) > 1:
                out.append(f'<polyline fill="none" stroke="{col}" stroke-width="2"{da} points="'
                           + " ".join(f"{a:.1f},{b:.1f}" for a, b in sg) + '"/>')
        last = max((i for i, v in enumerate(vs) if v is not None), default=None)
        for i, v in enumerate(vs):
            if v is None:
                continue
            out.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="4" fill="#fff" stroke="{col}" stroke-width="2">'
                       f'{_tip(f"{cats[i]}, {nm}: {_fmt(v, dec)}{unit}")}</circle>')
            if all_labels:
                out.append(_text(X(i), Y(v) - 8, _fmt(v, dec) + unit, 10, INK, weight="bold"))
            elif end_labels and i == last:
                ends.append([Y(v) + 4, X(i) + 7, _fmt(v, dec) + unit])
    ends.sort()
    for k in range(1, len(ends)):          # keep end labels at least 12px apart
        if ends[k][0] - ends[k - 1][0] < 12:
            ends[k][0] = ends[k - 1][0] + 12
    for yy, ax, s in ends:
        out.append(_text(ax, yy, s, 10, INK, anchor="start", weight="bold"))
    out.append(_legend(leg, pad_l, 14, w))
    return _svg(w, h, "".join(out), label)


def hbars(cats, vals, label, *, dec=0, unit="", w=520, h=None, highlight=None, colors=None,
          max_v=None, track=False, lab_w=150, notes=None):
    """Horizontal bars. track=True draws a light 0-max_v track behind each bar (for utilisation)."""
    row = 28
    h = h or (len(cats) * row + 14)
    hl = highlight if isinstance(highlight, (set, list, tuple)) else ({highlight} if highlight is not None else None)
    labs = [(_fmt(v, dec) + unit if v is not None else "") + (f"  {notes[i]}" if notes and notes.get(i) else "")
            for i, v in enumerate(vals)]
    pw = w - lab_w - max(56, 12 + 6.6 * max(len(s) for s in labs))   # room for the widest value label
    hi = max_v or max(v for v in vals if v is not None)
    out = []
    for i, (c, v) in enumerate(zip(cats, vals)):
        y = 6 + i * row
        col = colors[i] if colors else (PRIMARY if (hl is None or i in hl) else GREY)
        out.append(_text(lab_w - 8, y + 15, c, 11, INK, anchor="end"))
        if track:
            out.append(f'<rect x="{lab_w}" y="{y+5}" width="{pw:.1f}" height="{row-12}" fill="{GREY_LT}" rx="2"/>')
        if v is None:
            out.append(_text(lab_w + 4, y + 15, "Not disclosed", 10.5, MUTED, anchor="start", italic=True))
            continue
        out.append(f'<rect x="{lab_w}" y="{y+5}" width="{max(pw*v/hi,1):.1f}" height="{row-12}" fill="{col}" rx="2">'
                   f'{_tip(f"{c}: {_fmt(v, dec)}{unit}")}</rect>')
        tx = lab_w + (pw if track else pw * v / hi) + 6
        out.append(_text(tx, y + 15, labs[i], 11, INK, anchor="start", weight="bold"))
    return _svg(w, h, "".join(out), label)


def waterfall(steps, label, *, dec=1, w=520, h=250):
    """steps: list of (name, value, kind) kind in {'total','up','down'}. Totals are absolute.
    Names may contain '|' for a second label line."""
    pad_l, pad_r, pad_t, pad_b = 10, 10, 20, 40
    run, tops = 0, []
    for nm, v, k in steps:
        if k == "total":
            tops.append((0, v)); run = v
        elif k == "up":
            tops.append((run, run + v)); run += v
        else:
            tops.append((run - v, run)); run -= v
    hi = _nice_max(max(max(a, b) for a, b in tops) * 1.08)
    ph, pw = h - pad_t - pad_b, w - pad_l - pad_r
    slot = pw / len(steps)
    bw = min(54, slot * 0.62)

    def y(v):
        return pad_t + ph * (1 - v / hi)

    out = []
    prev = None
    for i, ((nm, v, k), (a, b)) in enumerate(zip(steps, tops)):
        cx = pad_l + slot * (i + 0.5)
        col = PRIMARY if k == "total" else (FOURTH if k == "up" else GREY)
        sign = "" if k == "total" else ("+" if k == "up" else "-")
        out.append(f'<rect x="{cx-bw/2:.1f}" y="{y(b):.1f}" width="{bw:.1f}" height="{max(y(a)-y(b),0.8):.1f}" fill="{col}" rx="2">'
                   f'{_tip(nm.replace("|", " ") + ": " + sign + _fmt(v, dec))}</rect>')
        out.append(_text(cx, y(b) - 5, sign + _fmt(v, dec), 10.5, INK, weight="bold"))
        for j, part in enumerate(nm.split("|")):
            out.append(_text(cx, h - 26 + j * 12, part, 9.5 if slot < 60 else 10, MUTED))
        if prev is not None:
            lvl = y(b) if k in ("down", "total") else y(a)
            out.append(f'<line x1="{prev:.1f}" x2="{cx-bw/2:.1f}" y1="{lvl:.1f}" y2="{lvl:.1f}" stroke="{AXIS}" stroke-dasharray="3,3"/>')
        prev = cx + bw / 2
    out.append(f'<line x1="{pad_l}" x2="{w-pad_r}" y1="{y(0):.1f}" y2="{y(0):.1f}" stroke="{AXIS}"/>')
    return _svg(w, h, "".join(out), label)


def value_range(rows, price, label, *, w=520, h=None, lo=0, hi=None, unit="Rs "):
    """rows: list of (name, value, color, note). Dots on one rupee axis with the price as a vertical line."""
    row = 34
    h = h or (len(rows) * row + 52)
    lab_w, pad_r = 96, 30
    hi = hi or _nice_max(max(v for _, v, _, _ in rows) * 1.1)
    pw = w - lab_w - pad_r

    def X(v):
        return lab_w + pw * (v - lo) / (hi - lo)

    out = []
    for t in range(6):
        gv = lo + (hi - lo) * t / 5
        out.append(f'<line x1="{X(gv):.1f}" x2="{X(gv):.1f}" y1="18" y2="{h-26}" stroke="{GREY_LT}"/>')
        out.append(_text(X(gv), h - 12, unit + _fmt(gv, 0), 9.5, MUTED))
    out.append(f'<line x1="{X(price):.1f}" x2="{X(price):.1f}" y1="14" y2="{h-26}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="4,3"/>')
    out.append(_text(X(price), 11, f"Price {unit}{_fmt(price, 0)}", 10.5, INK, weight="bold"))
    for i, (nm, v, col, note) in enumerate(rows):
        yy = 30 + i * row
        out.append(_text(lab_w - 8, yy + 4, nm, 11.5, INK, anchor="end", weight="bold"))
        out.append(f'<line x1="{X(price):.1f}" x2="{X(v):.1f}" y1="{yy}" y2="{yy}" stroke="{col}" stroke-width="3"/>')
        out.append(f'<circle cx="{X(v):.1f}" cy="{yy}" r="6.5" fill="{col}" stroke="#fff" stroke-width="2">'
                   f'{_tip(f"{nm}: {unit}{_fmt(v, 0)} ({note})")}</circle>')
        right = X(v) > X(price)
        s = f"{unit}{_fmt(v, 0)}  {note}"
        if right and X(v) + 11 + 6.2 * len(s) > w - 2:
            # no room right of the dot: put the label above it, ending at the dot
            out.append(_text(X(v) + 6, yy - 10, s, 10.5, INK, anchor="end"))
        else:
            out.append(_text(X(v) + (11 if right else -11), yy + 4, s, 10.5, INK, anchor="start" if right else "end"))
    return _svg(w, h, "".join(out), label)
