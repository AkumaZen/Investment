"""Small dependency-free SVG chart helpers for the Augmont v3 report.

Every function returns an inline <svg> string. Charts scale to their container width.
Palette is shared with the page CSS so charts and text read as one system.
"""
from html import escape

NAVY = "#14213D"
GOLD = "#C8962E"
GOLD_LT = "#E9D3A6"
SLATE = "#5B6B82"
GREY = "#A9B1BD"
GREY_LT = "#E6E9EE"
RED = "#B23A3A"
GREEN = "#2F7D5B"
INK = "#1F2733"
MUTED = "#6B7480"
FONT = "Calibri, Carlito, 'Segoe UI', Arial, sans-serif"


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
    return (
        f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" '
        f'style="width:100%;height:auto;display:block;font-family:{FONT}">{body}</svg>'
    )


def _text(x, y, s, size=11, fill=INK, anchor="middle", weight="normal", italic=False):
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}"{st}>{escape(str(s))}</text>')


def _nice_max(m):
    if m <= 0:
        return 1
    import math
    p = 10 ** math.floor(math.log10(m))
    for k in (1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10):
        if k * p >= m:
            return k * p
    return 10 * p


def bars(cats, vals, label, *, colors=None, dec=0, unit="", w=520, h=250, hatch=None,
         highlight=None, value_labels=None, ymin=None, axis_note=None, cagr=None):
    """Vertical bars. hatch: set of indices drawn as estimates (striped).
    value_labels overrides the printed value text. cagr: (i0, i1, text) arrow annotation."""
    hatch = hatch or set()
    pad_l, pad_r, pad_t, pad_b = 14, 14, 34 if cagr else 22, 34
    n = len(vals)
    lo = min(0, min(v for v in vals if v is not None)) if ymin is None else ymin
    hi = _nice_max(max(v for v in vals if v is not None) * 1.08)
    ph = h - pad_t - pad_b
    pw = w - pad_l - pad_r
    slot = pw / n
    bw = min(56, slot * 0.62)

    def y(v):
        return pad_t + ph * (hi - v) / (hi - lo)

    out = [f'<defs><pattern id="hatch{abs(hash(label))%9999}" width="6" height="6" patternUnits="userSpaceOnUse" '
           f'patternTransform="rotate(45)"><rect width="6" height="6" fill="{GOLD_LT}"/>'
           f'<line x1="0" y1="0" x2="0" y2="6" stroke="{GOLD}" stroke-width="2"/></pattern></defs>']
    hid = f"hatch{abs(hash(label))%9999}"
    out.append(f'<line x1="{pad_l}" x2="{w-pad_r}" y1="{y(0):.1f}" y2="{y(0):.1f}" stroke="{GREY}" stroke-width="1"/>')
    tops = []
    for i, (c, v) in enumerate(zip(cats, vals)):
        cx = pad_l + slot * (i + 0.5)
        if v is None:
            out.append(_text(cx, h - 14, c, 11.5 if slot > 58 else 9, MUTED))
            tops.append(None)
            continue
        col = (colors[i] if colors else (GOLD if highlight is not None and i == highlight else NAVY))
        fill = f"url(#{hid})" if i in hatch else col
        y0, y1 = sorted([y(0), y(v)])
        out.append(f'<rect x="{cx-bw/2:.1f}" y="{y0:.1f}" width="{bw:.1f}" height="{max(y1-y0,0.8):.1f}" fill="{fill}" rx="1.5"/>')
        lab = value_labels[i] if value_labels else _fmt(v, dec) + unit
        ty = y(v) - 5 if v >= 0 else y(v) + 13
        out.append(_text(cx, ty, lab, 12, INK, weight="bold"))
        out.append(_text(cx, h - 14, c, 11.5 if slot > 58 else 9, MUTED))
        tops.append(y(v))
    if cagr:
        i0, i1, txt = cagr
        x0 = pad_l + slot * (i0 + 0.5)
        x1 = pad_l + slot * (i1 + 0.5)
        yy = 14
        out.append(f'<line x1="{x0:.1f}" y1="{yy+6}" x2="{x1-6:.1f}" y2="{yy+6}" stroke="{GOLD}" stroke-width="1.6"/>'
                   f'<polygon points="{x1:.1f},{yy+6} {x1-7:.1f},{yy+2} {x1-7:.1f},{yy+10}" fill="{GOLD}"/>')
        out.append(_text((x0 + x1) / 2, yy + 1, txt, 11, GOLD, weight="bold"))
    if axis_note:
        out.append(_text(w - pad_r, h - 2, axis_note, 9.5, MUTED, anchor="end", italic=True))
    return _svg(w, h, "".join(out), label)


def grouped(cats, series, label, *, dec=0, unit="", w=520, h=250, legend=True):
    """series: list of (name, values, color)."""
    pad_l, pad_r, pad_t, pad_b = 14, 14, 30 if legend else 18, 34
    allv = [v for _, vs, _ in series for v in vs if v is not None]
    hi = _nice_max(max(allv) * 1.1)
    lo = min(0, min(allv)) * 1.15
    ph = h - pad_t - pad_b
    pw = w - pad_l - pad_r
    slot = pw / len(cats)
    k = len(series)
    bw = min(34, slot * 0.7 / k)

    def y(v):
        return pad_t + ph * (hi - v) / (hi - lo)

    out = [f'<line x1="{pad_l}" x2="{w-pad_r}" y1="{y(0):.1f}" y2="{y(0):.1f}" stroke="{GREY}"/>']
    for i, c in enumerate(cats):
        cx = pad_l + slot * (i + 0.5)
        for j, (nm, vs, col) in enumerate(series):
            v = vs[i]
            if v is None:
                continue
            x = cx - bw * k / 2 + j * bw
            y0, y1 = sorted([y(0), y(v)])
            out.append(f'<rect x="{x+1:.1f}" y="{y0:.1f}" width="{bw-2:.1f}" height="{max(y1-y0,0.8):.1f}" fill="{col}" rx="1.5"/>')
            out.append(_text(x + bw / 2, y(v) - 4 if v >= 0 else y(v) + 12, _fmt(v, dec) + unit, 10, INK, weight="bold"))
        out.append(_text(cx, h - 14, c, 11.5 if slot > 58 else 9, MUTED))
    if legend:
        lx = pad_l
        for nm, _, col in series:
            out.append(f'<rect x="{lx}" y="6" width="10" height="10" fill="{col}" rx="1.5"/>')
            out.append(_text(lx + 14, 15, nm, 10.5, INK, anchor="start"))
            lx += 22 + len(nm) * 5.6
    return _svg(w, h, "".join(out), label)


def stacked(cats, series, label, *, dec=0, w=520, h=260, totals=True, pct=False):
    """Stacked bars. series: list of (name, values, color). pct=True labels segment share."""
    pad_l, pad_r, pad_t, pad_b = 14, 120, 22, 34
    tot = [sum(v for _, vs, _ in series for v in [vs[i]] if v) for i in range(len(cats))]
    hi = _nice_max(max(tot) * 1.08)
    ph = h - pad_t - pad_b
    pw = w - pad_l - pad_r
    slot = pw / len(cats)
    bw = min(60, slot * 0.6)
    out = [f'<line x1="{pad_l}" x2="{pad_l+pw}" y1="{pad_t+ph}" y2="{pad_t+ph}" stroke="{GREY}"/>']
    for i, c in enumerate(cats):
        cx = pad_l + slot * (i + 0.5)
        acc = 0
        for nm, vs, col in series:
            v = vs[i] or 0
            y1 = pad_t + ph * (1 - (acc + v) / hi)
            hh = ph * v / hi
            out.append(f'<rect x="{cx-bw/2:.1f}" y="{y1:.1f}" width="{bw:.1f}" height="{hh:.1f}" fill="{col}"/>')
            if hh > 13:
                lab = f"{v/tot[i]*100:.0f}%" if pct else _fmt(v, dec)
                tc = "#fff" if col in (NAVY, SLATE, GOLD, RED, GREEN) else INK
                out.append(_text(cx, y1 + hh / 2 + 4, lab, 10, tc))
            acc += v
        if totals:
            out.append(_text(cx, pad_t + ph * (1 - tot[i] / hi) - 5, _fmt(tot[i], dec), 11, INK, weight="bold"))
        out.append(_text(cx, h - 14, c, 11.5 if slot > 58 else 9, MUTED))
    ly = pad_t + 4
    for nm, _, col in reversed(series):
        out.append(f'<rect x="{w-pad_r+14}" y="{ly}" width="10" height="10" fill="{col}" rx="1.5"/>')
        out.append(_text(w - pad_r + 28, ly + 9, nm, 10.5, INK, anchor="start"))
        ly += 18
    return _svg(w, h, "".join(out), label)


def bar_line(cats, bar_vals, line_vals, label, *, bar_name, line_name, bar_dec=0, line_dec=1,
             line_unit="", w=520, h=260, bar_color=NAVY, line_color=GOLD, hatch=None):
    """Bars on the left scale, a line with dots on its own right scale."""
    hatch = hatch or set()
    pad_l, pad_r, pad_t, pad_b = 14, 14, 34, 34
    hi = _nice_max(max(bar_vals) * 1.12)
    lv = [v for v in line_vals if v is not None]
    lhi, llo = max(lv), min(lv)
    span = (lhi - llo) or abs(lhi) or 1
    l_top, l_bot = lhi + span * 0.25, llo - span * 0.9
    ph = h - pad_t - pad_b
    pw = w - pad_l - pad_r
    slot = pw / len(cats)
    bw = min(52, slot * 0.58)
    out = [f'<defs><pattern id="bl{abs(hash(label))%9999}" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
           f'<rect width="6" height="6" fill="#c9d0db"/><line x1="0" y1="0" x2="0" y2="6" stroke="{SLATE}" stroke-width="2"/></pattern></defs>']
    out.append(f'<line x1="{pad_l}" x2="{w-pad_r}" y1="{pad_t+ph}" y2="{pad_t+ph}" stroke="{GREY}"/>')
    pts = []
    for i, c in enumerate(cats):
        cx = pad_l + slot * (i + 0.5)
        v = bar_vals[i]
        yy = pad_t + ph * (1 - v / hi)
        fill = f"url(#bl{abs(hash(label))%9999})" if i in hatch else bar_color
        out.append(f'<rect x="{cx-bw/2:.1f}" y="{yy:.1f}" width="{bw:.1f}" height="{pad_t+ph-yy:.1f}" fill="{fill}" rx="1.5"/>')
        out.append(_text(cx, pad_t + ph - 6, _fmt(v, bar_dec), 10, "#fff" if i not in hatch else INK, weight="bold"))
        out.append(_text(cx, h - 14, c, 11.5 if slot > 58 else 9, MUTED))
        if line_vals[i] is not None:
            ly = pad_t + ph * (l_top - line_vals[i]) / (l_top - l_bot)
            pts.append((cx, ly, line_vals[i]))
    if pts:
        out.append('<polyline fill="none" stroke="%s" stroke-width="2.2" points="%s"/>'
                   % (line_color, " ".join(f"{x:.1f},{y:.1f}" for x, y, _ in pts)))
        for x, y, v in pts:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#fff" stroke="{line_color}" stroke-width="2"/>')
            out.append(_text(x, y - 9, _fmt(v, line_dec) + line_unit, 10.5, line_color, weight="bold"))
    out.append(f'<rect x="{pad_l}" y="6" width="10" height="10" fill="{bar_color}" rx="1.5"/>')
    out.append(_text(pad_l + 14, 15, bar_name, 10.5, INK, anchor="start"))
    lx = pad_l + 30 + len(bar_name) * 5.6
    out.append(f'<line x1="{lx}" x2="{lx+14}" y1="11" y2="11" stroke="{line_color}" stroke-width="2.2"/>'
               f'<circle cx="{lx+7}" cy="11" r="3" fill="#fff" stroke="{line_color}" stroke-width="2"/>')
    out.append(_text(lx + 19, 15, line_name, 10.5, INK, anchor="start"))
    return _svg(w, h, "".join(out), label)


def hbars(cats, vals, label, *, dec=0, unit="", w=520, h=None, highlight=None, colors=None, max_v=None):
    row = 26
    h = h or (len(cats) * row + 16)
    lab_w = 150
    pw = w - lab_w - 60
    hi = max_v or max(vals)
    out = []
    for i, (c, v) in enumerate(zip(cats, vals)):
        y = 8 + i * row
        col = colors[i] if colors else (GOLD if highlight is not None and i in (highlight if isinstance(highlight, (set, list, tuple)) else {highlight}) else NAVY)
        out.append(_text(lab_w - 8, y + 14, c, 11, INK, anchor="end"))
        out.append(f'<rect x="{lab_w}" y="{y+3}" width="{pw*v/hi:.1f}" height="{row-9}" fill="{col}" rx="1.5"/>')
        out.append(_text(lab_w + pw * v / hi + 5, y + 14, _fmt(v, dec) + unit, 11, INK, anchor="start", weight="bold"))
    return _svg(w, h, "".join(out), label)


def donut(parts, label, *, w=300, h=200, center=None, sub=None):
    """parts: list of (name, value, color). Legend on the right."""
    import math
    cx, cy, r, ri = 92, h / 2, 78, 48
    tot = sum(v for _, v, _ in parts)
    a = -math.pi / 2
    out = []
    for nm, v, col in parts:
        da = 2 * math.pi * v / tot
        a2 = a + da
        large = 1 if da > math.pi else 0
        x1, y1 = cx + r * math.cos(a), cy + r * math.sin(a)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        x3, y3 = cx + ri * math.cos(a2), cy + ri * math.sin(a2)
        x4, y4 = cx + ri * math.cos(a), cy + ri * math.sin(a)
        out.append(f'<path d="M{x1:.2f},{y1:.2f} A{r},{r} 0 {large} 1 {x2:.2f},{y2:.2f} L{x3:.2f},{y3:.2f} '
                   f'A{ri},{ri} 0 {large} 0 {x4:.2f},{y4:.2f} Z" fill="{col}" stroke="#fff" stroke-width="1.5"/>')
        a = a2
    if center:
        out.append(_text(cx, cy + 4, center, 17, NAVY, weight="bold"))
    if sub:
        out.append(_text(cx, cy + 20, sub, 9.5, MUTED))
    ly = cy - len(parts) * 11 + 6
    for nm, v, col in parts:
        out.append(f'<rect x="{cx+r+20}" y="{ly-9}" width="10" height="10" fill="{col}" rx="1.5"/>')
        out.append(_text(cx + r + 35, ly, f"{nm}  {_fmt(v, 1 if v < 10 else 1)}%" if tot > 99 and tot < 101 else f"{nm}  {_fmt(v,1)}", 10.5, INK, anchor="start"))
        ly += 22
    return _svg(w, h, "".join(out), label)


def waterfall(steps, label, *, dec=1, w=520, h=260):
    """steps: list of (name, value, kind) kind in {'total','up','down'}. Totals are absolute."""
    pad_l, pad_r, pad_t, pad_b = 14, 14, 22, 40
    run = 0
    tops = []
    for nm, v, k in steps:
        if k == "total":
            tops.append((0, v)); run = v
        elif k == "up":
            tops.append((run, run + v)); run += v
        else:
            tops.append((run - v, run)); run -= v
    hi = _nice_max(max(max(a, b) for a, b in tops) * 1.1)
    ph = h - pad_t - pad_b
    pw = w - pad_l - pad_r
    slot = pw / len(steps)
    bw = min(60, slot * 0.62)

    def y(v):
        return pad_t + ph * (1 - v / hi)

    out = [f'<line x1="{pad_l}" x2="{w-pad_r}" y1="{y(0):.1f}" y2="{y(0):.1f}" stroke="{GREY}"/>']
    prev = None
    for i, ((nm, v, k), (a, b)) in enumerate(zip(steps, tops)):
        cx = pad_l + slot * (i + 0.5)
        col = NAVY if k == "total" else (GREEN if k == "up" else RED)
        out.append(f'<rect x="{cx-bw/2:.1f}" y="{y(b):.1f}" width="{bw:.1f}" height="{max(y(a)-y(b),0.8):.1f}" fill="{col}" rx="1.5"/>')
        sign = "" if k == "total" else ("+" if k == "up" else "-")
        out.append(_text(cx, y(b) - 5, sign + _fmt(v, dec), 11, INK, weight="bold"))
        for j, part in enumerate(nm.split("|")):
            out.append(_text(cx, h - 24 + j * 12, part, 10, MUTED))
        if prev is not None:
            out.append(f'<line x1="{prev:.1f}" x2="{cx-bw/2:.1f}" y1="{y(b if k=="down" else (a if k=="up" else b)):.1f}" '
                       f'y2="{y(b if k=="down" else (a if k=="up" else b)):.1f}" stroke="{GREY}" stroke-dasharray="3,3"/>')
        prev = cx + bw / 2
    return _svg(w, h, "".join(out), label)


def diverging(cats, vals, label, *, unit="%", w=360, h=None):
    """Horizontal bars around a zero line; negatives red to the left, positives green to the right."""
    row = 30
    h = h or (len(cats) * row + 16)
    lab_w = 120
    mid = lab_w + (w - lab_w) / 2
    half = (w - lab_w) / 2 - 40
    hi = max(abs(v) for v in vals)
    out = [f'<line x1="{mid}" x2="{mid}" y1="4" y2="{h-4}" stroke="{GREY}"/>']
    for i, (c, v) in enumerate(zip(cats, vals)):
        y = 8 + i * row
        ln = half * abs(v) / hi
        x = mid - ln if v < 0 else mid
        col = RED if v < 0 else GREEN
        out.append(_text(lab_w - 8, y + 15, c, 11.5, INK, anchor="end"))
        out.append(f'<rect x="{x:.1f}" y="{y+4}" width="{ln:.1f}" height="{row-11}" fill="{col}" rx="1.5"/>')
        tx = x - 4 if v < 0 else x + ln + 4
        out.append(_text(tx, y + 15, ("+" if v > 0 else "") + _fmt(v, 0) + unit, 11.5, INK,
                         anchor="end" if v < 0 else "start", weight="bold"))
    return _svg(w, h, "".join(out), label)
