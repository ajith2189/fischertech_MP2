"""
Creates baseplate_workshop_drawing.pdf (2 pages, A3) from the layout in baseplate_v3_freecad.py.
Run:  python make_drawing.py     (needs matplotlib; keep both files in the same folder)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle, Circle

here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "baseplate_v3_freecad.py")).read().split("# PART 2")[0]
ns = {}
exec(src, ns)
L, W, T = ns["PLATE_L"], ns["PLATE_W"], ns["PLATE_T"]
HOLES = ns["HOLES"]
COL = {"A": "#c0392b", "B": "#2471a3", "C": "#1e8449", "D": "#7d3c98", "E": "#d35400"}
GROUP = {"A": "M6 plate-to-bench", "B": "M5 DIN rail", "C": "M4 machine (placeholder)",
         "D": "M2.5 Pi / FT I/O board", "E": "banana jack"}


def dim_h(ax, x0, x1, y, text):
    ax.annotate("", (x0, y), (x1, y), arrowprops=dict(arrowstyle="<->", lw=0.6))
    ax.text((x0 + x1) / 2, y + 3, text, ha="center", va="bottom", fontsize=7)


def dim_v(ax, x, y0, y1, text):
    ax.annotate("", (x, y0), (x, y1), arrowprops=dict(arrowstyle="<->", lw=0.6))
    ax.text(x - 4, (y0 + y1) / 2, text, ha="right", va="center", rotation=90, fontsize=7)


def title_block(fig, page, title):
    fig.text(0.03, 0.035, "Minimal baseplate - Fischertechnik 96790 + Pi + I/O board + Phoenix coupler | %s" % title,
             fontsize=8, weight="bold")
    fig.text(0.03, 0.015, "Material: 12 mm plywood or acrylic (TBD) | Units: mm | Datum: bottom-left corner | "
             "Tolerance: +/-1 mm (hand-cut) | PRELIMINARY | Page %d/2" % page, fontsize=6.5)


with PdfPages(os.path.join(here, "baseplate_workshop_drawing.pdf")) as pdf:
    fig = plt.figure(figsize=(16.54, 11.69))
    ax = fig.add_axes([0.05, 0.08, 0.60, 0.88])
    ax.add_patch(Rectangle((0, 0), L, W, fill=False, lw=1.6))
    for name, x0, y0, x1, y1 in ns["footprints"]():
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, ec="#555", lw=0.8, ls="--"))
        small = (x1 - x0) < 30
        ax.text((x0 + x1) / 2, (y0 + y1) / 2 if not small else y1 + 4, name.replace("_", " "),
                ha="center", va="center" if not small else "bottom",
                fontsize=7 if (x1 - x0) > 60 else 5.5, rotation=90 if small else 0)
    for rail, (x0, yc, rl) in ns["DIN_RAILS"].items():
        ax.add_patch(Rectangle((x0, yc - 17.5), rl, 35, fill=False, ec="#222", lw=0.8))
        ax.text(x0, yc - 22, "DIN rail TS35, %.0f mm" % rl, fontsize=6, va="top")
    ax.plot([ns["CX"]] * 2, [-12, W + 12], color="#888", lw=0.6, ls="-.")
    ax.text(ns["CX"], W + 14, "machine centre line (FT I/O board centred here)", fontsize=6, ha="center")
    for h in HOLES:
        ax.add_patch(Circle((h["x"], h["y"]), h["d"] / 2, fill=False, ec=COL[h["id"][0]], lw=1.0))
        ax.text(h["x"] + h["d"] / 2 + 2, h["y"] + h["d"] / 2 + 2, h["id"], fontsize=5.5, color=COL[h["id"][0]])
    dim_h(ax, 0, L, -24, "%.0f" % L)
    dim_v(ax, -14, 0, W, "%.0f" % W)
    ax.text(L / 2, 6, "FRONT / OPERATOR EDGE (Y = 0)", fontsize=6.5, style="italic", ha="center")
    ax.set_xlim(-30, L + 20)
    ax.set_ylim(-40, W + 30)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.text(0.68, 0.90, "LEGEND", fontsize=9, weight="bold")
    for i, (g, lab) in enumerate(GROUP.items()):
        fig.text(0.68, 0.87 - i * 0.025, "o  %s: %s" % (g, lab), fontsize=8, color=COL[g])
    fig.text(0.68, 0.72, "STRIP ORDER (left to right)", fontsize=9, weight="bold")
    for i, t in enumerate(["Banana jack", "Raspberry Pi", "Fischertechnik I/O board (centred)",
                           "Phoenix coupler + 2 extension modules"]):
        fig.text(0.68, 0.695 - i * 0.025, "%d. %s" % (i + 1, t), fontsize=8)
    title_block(fig, 1, "Top view with hole IDs")
    pdf.savefig(fig)
    plt.close(fig)

    fig = plt.figure(figsize=(16.54, 11.69))
    fig.text(0.03, 0.95, "HOLE SCHEDULE (datum: bottom-left corner, X right / Y up)", fontsize=11, weight="bold")
    fig.text(0.03, 0.92, "ID     X      Y      Dia    Purpose", fontsize=8, family="monospace", weight="bold")
    for r, h in enumerate(HOLES):
        fig.text(0.03, 0.895 - r * 0.0295, "%-4s %6.1f %6.1f  %4.1f   %s" % (h["id"], h["x"], h["y"], h["d"], h["note"]),
                 fontsize=8, family="monospace", color=COL[h["id"][0]])
    notes = [
        "NOTES",
        "1. Mark all holes from the datum corner using this schedule; check diagonals before drilling.",
        "2. Clamp a sacrificial board underneath; drill a pilot hole first, then final size.",
        "3. ACRYLIC: low speed, step bit, washers, do not overtighten. PLYWOOD: seal edges.",
        "4. DIN rail TS35 cut to length, deburr. Use through-bolts + washers.",
        "5. Banana jack hole (E1) is 8 mm placeholder: check the jack's datasheet and thread length.",
        "6. Machine mount holes (C-group) are PLACEHOLDERS: re-measure on the real machine.",
        "7. FT I/O board hole pattern assumed equal to Raspberry Pi (58 x 49): verify.",
        "8. Phoenix extension module width (12.2 mm) is an assumption: verify.",
        "9. No power supply on the plate: board is powered through the banana jack.",
    ]
    for i, n in enumerate(notes):
        fig.text(0.50, 0.92 - i * 0.03, n, fontsize=8, weight="bold" if i == 0 else None)
    title_block(fig, 2, "Hole schedule and notes")
    pdf.savefig(fig)
    plt.close(fig)

print("Wrote baseplate_workshop_drawing.pdf")
