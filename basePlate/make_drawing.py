"""
Creates baseplate_workshop_drawing.pdf (2 pages, A3) from the layout in baseplate_v2_freecad.py.
Run:  python make_drawing.py     (needs matplotlib; keep both files in the same folder)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle, Circle

here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "baseplate_v2_freecad.py")).read().split("# PART 2")[0]
ns = {}
exec(src, ns)
L, W, T = ns["PLATE_L"], ns["PLATE_W"], ns["PLATE_T"]
HOLES = ns["HOLES"]
COL = {"A": "#c0392b", "B": "#2471a3", "C": "#1e8449", "D": "#7d3c98"}
GROUP = {"A": "M6 plate-to-bench", "B": "M5 DIN rail", "C": "M4 accessories / machine / ducts", "D": "M2.5 Raspberry Pi"}


def dim_h(ax, x0, x1, y, text, off=0):
    ax.annotate("", (x0, y), (x1, y), arrowprops=dict(arrowstyle="<->", lw=0.6))
    ax.text((x0 + x1) / 2, y + off, text, ha="center", va="bottom", fontsize=7)


def dim_v(ax, x, y0, y1, text):
    ax.annotate("", (x, y0), (x, y1), arrowprops=dict(arrowstyle="<->", lw=0.6))
    ax.text(x - 6, (y0 + y1) / 2, text, ha="right", va="center", rotation=90, fontsize=7)


def title_block(ax_fig, page, of, title):
    ax_fig.text(0.03, 0.035, "Baseplate - Fischertechnik 96790 + electrical zone | %s" % title, fontsize=8, weight="bold")
    ax_fig.text(0.03, 0.015, "Material: 12 mm plywood or acrylic (TBD) | Units: mm | Datum: bottom-left corner | "
                "Tolerance: +/-1 mm (hand-cut) | PRELIMINARY - placeholder dims marked | Page %d/%d" % (page, of), fontsize=6.5)


with PdfPages(os.path.join(here, "baseplate_workshop_drawing.pdf")) as pdf:
    # ---------------- page 1: plan view ----------------
    fig = plt.figure(figsize=(16.54, 11.69))
    ax = fig.add_axes([0.06, 0.12, 0.90, 0.80])
    ax.add_patch(Rectangle((0, 0), L, W, fill=False, lw=1.6))
    for name, x0, y0, x1, y1 in ns["footprints"]():
        spare = name.startswith("SPARE")
        optional = "OPTIONAL" in name
        ls = ":" if spare or optional else "--"
        fc = "#f9e79f" if optional or spare else ("#d5d8dc" if name.startswith("Duct") else "none")
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=fc != "none", fc=fc, alpha=0.45,
                               ec="#555", lw=0.7, ls=ls))
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, name.replace("_", " "), ha="center", va="center",
                fontsize=5.5 if (x1 - x0) < 120 else 7, rotation=90 if (x1 - x0) < 50 and (y1 - y0) > 100 else 0)
    for rail, (x0, yc, rl) in ns["DIN_RAILS"].items():
        ax.add_patch(Rectangle((x0, yc - 17.5), rl, 35, fill=False, ec="#222", lw=0.8))
        ax.text(x0 + rl + 4, yc, "DIN " + rail, fontsize=6, va="center")
    for h in HOLES:
        ax.add_patch(Circle((h["x"], h["y"]), h["d"] / 2, fill=False, ec=COL[h["id"][0]], lw=1.0))
        ax.text(h["x"] + h["d"] / 2 + 2, h["y"] + h["d"] / 2 + 2, h["id"], fontsize=5, color=COL[h["id"][0]])
    ax.text(15, W + 12, "ELECTRICAL ZONE (mains/24 V at back, signal/network at front)", fontsize=8, weight="bold")
    ax.text(ns["MACHINE"][1], W + 12, "MACHINE ZONE", fontsize=8, weight="bold")
    ax.text(5, -48, "FRONT / OPERATOR EDGE (Y = 0)", fontsize=7, style="italic")
    dim_h(ax, 0, L, -18, "%.0f" % L)
    dim_v(ax, -18, 0, W, "%.0f" % W)
    _, mx, my, mL, mW, _ = ns["MACHINE"]
    dim_h(ax, mx, mx + mL, my - 12, "%.0f" % mL)
    dim_v(ax, mx - 8, my, my + mW, "%.0f" % mW)
    ax.set_xlim(-45, L + 25)
    ax.set_ylim(-60, W + 35)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.text(0.50, 0.075, "   ".join("o %s: %s" % (g, l) for g, l in GROUP.items()), fontsize=7)
    title_block(fig, 1, 2, "Top view with hole IDs")
    pdf.savefig(fig)
    plt.close(fig)

    # ---------------- page 2: hole schedule + notes ----------------
    fig = plt.figure(figsize=(16.54, 11.69))
    fig.text(0.03, 0.95, "HOLE SCHEDULE (datum: bottom-left corner, X right / Y up)", fontsize=11, weight="bold")
    half = (len(HOLES) + 1) // 2
    for col, chunk in enumerate((HOLES[:half], HOLES[half:])):
        x0 = 0.03 + col * 0.37
        fig.text(x0, 0.92, "ID     X      Y      Dia    Purpose", fontsize=7.5, family="monospace", weight="bold")
        for r, h in enumerate(chunk):
            fig.text(x0, 0.90 - r * 0.0265, "%-4s %6.1f %6.1f  %4.1f   %s" % (h["id"], h["x"], h["y"], h["d"], h["note"]),
                     fontsize=7, family="monospace", color=COL[h["id"][0]])
    notes = [
        "NOTES",
        "1. Mark all holes from the datum corner using this schedule; check diagonals before drilling.",
        "2. Clamp a sacrificial board underneath; drill pilot hole first, then final size.",
        "3. ACRYLIC: low drill speed, step bit, no overtightening, washers under screws.",
        "   PLYWOOD: seal or paint edges; use through-bolts + washers for DIN rails.",
        "4. DIN rail TS35: cut to length, deburr; electrical zone rails: PWR / IO / NET.",
        "5. Keep 24 V / mains wiring in the top duct and signal / network in the bottom duct.",
        "6. Hilscher board position is OPTIONAL: model not yet decided.",
        "7. Machine mounting holes (C-group, x = 525...950) are PLACEHOLDERS: re-measure.",
        "8. Mains wiring and commissioning only by qualified lab personnel.",
    ]
    for i, n in enumerate(notes):
        fig.text(0.76, 0.92 - i * 0.03, n, fontsize=7.5, weight="bold" if i == 0 else None)
    title_block(fig, 2, 2, "Hole schedule and notes")
    pdf.savefig(fig)
    plt.close(fig)

print("Wrote baseplate_workshop_drawing.pdf")
