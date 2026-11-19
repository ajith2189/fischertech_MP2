"""
Integrated baseplate v2: Fischertechnik 96790 + electrical zone (CODESYS / PROFINET demonstrator)
RUN IN FREECAD: Macro > Macros... > Create > paste > Execute.
Units: mm.  Datum: plate bottom-left corner (0,0). X = length, Y = depth (Y=0 is the operator/front edge).
Values marked  # CHECK  are placeholders: measure the real part and edit it. Everything else follows from them.
Outputs (home folder): baseplate_v2.FCStd (editable), baseplate_v2.step, baseplate_v2.stl (plate only).
"""
import math

# ======================================================================
# PART 1 - PARAMETERS AND LAYOUT (pure Python, also used by make_drawing.py)
# ======================================================================
PLATE_L, PLATE_W, PLATE_T = 1000.0, 560.0, 12.0   # 12 mm plywood or acrylic; change freely
CORNER_R = 10.0                                    # jigsaw-friendly radius (0 = sharp)
SHOW_COMPONENT_BOXES = True                        # translucent boxes for layout check

# hole diameters (from your spec)
D_BENCH, D_DIN, D_ACC, D_PI = 6.5, 5.5, 4.5, 2.8   # M6, M5, M4, M2.5

# --- Machine zone (right side) -------------------------------------------------
# name, x, y, L(x), W(y), H(z)
MACHINE = ("Fischertechnik_96790", 500.0, 55.0, 475.0, 450.0, 270.0)
MACHINE_HOLE_INSET = 25.0                          # CHECK: 6 holes are placeholders until you measure the machine

# --- Electrical zone (left side) -----------------------------------------------
# DIN rails (TS35, run along X):  name: (x_start, y_centre, length)
DIN_RAILS = {
    "PWR": (35.0, 470.0, 400.0),    # back: mains + 24 V generation
    "IO":  (35.0, 295.0, 400.0),    # middle: I/O, PROFINET, signal terminals
    "NET": (35.0, 140.0, 250.0),    # front: network switch, 5 V for Pi
}
DIN_HOLE_END_INSET, DIN_HOLE_PITCH = 15.0, 100.0   # max screw spacing

# Rail-mounted parts: name, rail, x_start, L(along rail), W(across rail), H(height above plate)
# SPARE_* = reserved space (not a real part). All sizes CHECK against datasheets.
RAIL_PARTS = [
    ("Circuit_Breaker_2P",      "PWR",  40.0,  36.0,  90.0,  70.0),
    ("Fuse_Holders",            "PWR",  85.0,  54.0,  80.0,  70.0),
    ("PSU_24V",                 "PWR", 150.0,  45.0, 130.0, 125.0),
    ("Terminals_24V_Power",     "PWR", 205.0, 120.0,  45.0,  40.0),
    ("Phoenix_IL_PN_BK",        "IO",   40.0,  80.0, 120.0,  72.0),
    ("SPARE_IO_Expansion",      "IO",  125.0,  80.0, 120.0,  72.0),
    ("Hilscher_OPTIONAL",       "IO",  215.0,  80.0,  60.0,  30.0),
    ("Terminals_Signal",        "IO",  305.0,  80.0,  45.0,  40.0),
    ("Network_Switch",          "NET",  40.0,  40.0,  90.0,  70.0),
    ("PSU_5V_for_Pi",           "NET",  90.0,  36.0,  90.0,  60.0),
]

# Screw-mounted parts: name, x, y (bottom-left), L, W, H, hole offsets, hole dia, hole group
PI_HOLES = [(3.5, 3.5), (61.5, 3.5), (3.5, 52.5), (61.5, 52.5)]   # Pi 3B 58 x 49 pattern
SCREW_PARTS = [
    ("Raspberry_Pi_3B",   100.0, 30.0, 85.0, 56.0, 20.0, PI_HOLES, D_PI, "D"),
    ("Emergency_Stop_Box", 360.0, 35.0, 80.0, 80.0, 60.0,
        [(10, 10), (70, 10), (10, 70), (70, 70)], D_ACC, "C"),
]

# Slotted PVC wiring ducts: name, x, y (bottom-left), extent_x, extent_y   (height DUCT_H)
DUCT_H = 25.0
DUCTS = [
    ("Duct_Power_24V_mains",     35.0, 360.0, 415.0, 40.0),
    ("Duct_Signal_network",      35.0, 190.0, 415.0, 40.0),
    ("Duct_Vertical_to_machine", 450.0, 190.0, 40.0, 210.0),   # use a duct with an internal divider
]
DUCT_HOLE_END_INSET, DUCT_HOLE_PITCH = 20.0, 150.0

# Cable strain-relief clamp points (M4): mains in (2), network in, machine cable
CLAMPS = [(18.0, 440.0, "Mains entry clamp"), (18.0, 500.0, "Mains entry clamp"),
          (18.0, 140.0, "Network entry clamp"), (470.0, 175.0, "Machine cable clamp")]


def line_points(start, length, inset, pitch):
    span = length - 2 * inset
    n = max(1, int(math.ceil(span / pitch)))
    return [start + inset + i * span / n for i in range(n + 1)]


def build_holes():
    raw = []   # (group, x, y, d, note)
    for x in (15.0, PLATE_L - 15.0):
        for y in (15.0, PLATE_W - 15.0):
            raw.append(("A", x, y, D_BENCH, "Plate to bench (corner)"))
    for y in (15.0, PLATE_W - 15.0):
        raw.append(("A", PLATE_L / 2.0, y, D_BENCH, "Plate to bench (mid-edge)"))
    for name, (x0, yc, L) in DIN_RAILS.items():
        for x in line_points(x0, L, DIN_HOLE_END_INSET, DIN_HOLE_PITCH):
            raw.append(("B", x, yc, D_DIN, "DIN rail " + name))
    for name, x, y, dx, dy in DUCTS:
        if dx >= dy:
            for px in line_points(x, dx, DUCT_HOLE_END_INSET, DUCT_HOLE_PITCH):
                raw.append(("C", px, y + dy / 2.0, D_ACC, name))
        else:
            for py in line_points(y, dy, DUCT_HOLE_END_INSET, DUCT_HOLE_PITCH):
                raw.append(("C", x + dx / 2.0, py, D_ACC, name))
    _, mx, my, mL, mW, _ = MACHINE
    i = MACHINE_HOLE_INSET
    for hx in (mx + i, mx + mL / 2.0, mx + mL - i):
        for hy in (my + i, my + mW - i):
            raw.append(("C", hx, hy, D_ACC, "Machine mount (PLACEHOLDER)"))
    for name, x, y, L, W, H, holes, d, g in SCREW_PARTS:
        for dx, dy in holes:
            raw.append((g, x + dx, y + dy, d, name))
    for x, y, note in CLAMPS:
        raw.append(("C", x, y, D_ACC, note))
    out, count = [], {}
    for g in "ABCD":
        for (gg, x, y, d, note) in raw:
            if gg == g:
                count[g] = count.get(g, 0) + 1
                out.append(dict(id="%s%d" % (g, count[g]), x=round(x, 1), y=round(y, 1), d=d, note=note))
    return out


def footprints():
    """Plan-view rectangles (name, x0, y0, x1, y1) for the overlap check and the drawing."""
    r = []
    for name, rail, x, L, W, H in RAIL_PARTS:
        _, yc, _ = DIN_RAILS[rail]
        r.append((name, x, yc - W / 2.0, x + L, yc + W / 2.0))
    for name, x, y, L, W, H, _, _, _ in SCREW_PARTS:
        r.append((name, x, y, x + L, y + W))
    for name, x, y, dx, dy in DUCTS:
        r.append((name, x, y, x + dx, y + dy))
    _, mx, my, mL, mW, _ = MACHINE
    r.append((MACHINE[0], mx, my, mx + mL, my + mW))
    return r


def report():
    warn = []
    holes = build_holes()
    for h in holes:
        if not (h["d"] / 2 + 3 < h["x"] < PLATE_L - h["d"] / 2 - 3 and h["d"] / 2 + 3 < h["y"] < PLATE_W - h["d"] / 2 - 3):
            warn.append("hole %s too close to edge" % h["id"])
    for i, a in enumerate(holes):
        for b in holes[i + 1:]:
            if math.hypot(a["x"] - b["x"], a["y"] - b["y"]) < 10:
                warn.append("holes %s and %s are < 10 mm apart" % (a["id"], b["id"]))
    fp = footprints()
    for i, a in enumerate(fp):
        if a[1] < 0 or a[2] < 0 or a[3] > PLATE_L or a[4] > PLATE_W:
            warn.append("%s outside plate" % a[0])
        for b in fp[i + 1:]:
            if a[1] < b[3] and b[1] < a[3] and a[2] < b[4] and b[2] < a[4]:
                warn.append("OVERLAP: %s / %s" % (a[0], b[0]))
    for rail, (x0, yc, L) in DIN_RAILS.items():
        used = sum(p[3] for p in RAIL_PARTS if p[1] == rail and not p[0].startswith("SPARE"))
        for p in RAIL_PARTS:
            if p[1] == rail and (p[2] < x0 or p[2] + p[3] > x0 + L):
                warn.append("%s exceeds rail %s" % (p[0], rail))
        spare = 100.0 * (1 - used / L)
        msg = "Rail %s: %.0f%% free" % (rail, spare)
        if spare < 20:
            warn.append(msg + " (< 20% target)")
        else:
            print(msg)
    for w in warn:
        print("WARNING:", w)
    print("%d holes, plate %.0f x %.0f x %.0f mm" % (len(holes), PLATE_L, PLATE_W, PLATE_T))
    return warn


HOLES = build_holes()
report()

# ======================================================================
# PART 2 - FREECAD MODEL
# ======================================================================
try:
    import FreeCAD as App
    import Part
    from FreeCAD import Vector as V
    IN_FREECAD = True
except ImportError:
    IN_FREECAD = False

if IN_FREECAD:
    plate = Part.makeBox(PLATE_L, PLATE_W, PLATE_T)
    if CORNER_R > 0:
        vert = [e for e in plate.Edges if abs(e.Vertexes[0].Z - e.Vertexes[1].Z) > 1e-6]
        plate = plate.makeFillet(CORNER_R, vert)
    cutters = [Part.makeCylinder(h["d"] / 2.0, PLATE_T + 2, V(h["x"], h["y"], -1)) for h in HOLES]
    plate = plate.cut(Part.makeCompound(cutters))

    doc = App.newDocument("Baseplate_v2")
    obj = doc.addObject("Part::Feature", "Baseplate")
    obj.Shape = plate

    def ghost(name, x, y, L, W, H, color, transp=60):
        g = doc.addObject("Part::Feature", "Ghost_" + name)
        g.Shape = Part.makeBox(L, W, H, V(x, y, PLATE_T))
        try:
            g.ViewObject.ShapeColor = color
            g.ViewObject.Transparency = transp
        except Exception:
            pass

    if SHOW_COMPONENT_BOXES:
        for name, rail, x, L, W, H in RAIL_PARTS:
            _, yc, _ = DIN_RAILS[rail]
            col = (0.9, 0.7, 0.2) if name.startswith(("SPARE", "Hilscher")) else (0.2, 0.5, 0.9)
            ghost(name, x, yc - W / 2.0, L, W, H, col, 80 if name.startswith("SPARE") else 55)
        for name, x, y, L, W, H, _, _, _ in SCREW_PARTS:
            ghost(name, x, y, L, W, H, (0.2, 0.7, 0.3))
        for name, x, y, dx, dy in DUCTS:
            ghost(name, x, y, dx, dy, DUCT_H, (0.6, 0.6, 0.6), 40)
        n, mx, my, mL, mW, mH = MACHINE
        ghost(n, mx, my, mL, mW, mH, (0.9, 0.3, 0.3), 75)
        for rail, (x0, yc, L) in DIN_RAILS.items():
            ghost("DIN_" + rail, x0, yc - 17.5, L, 35.0, 7.5, (0.1, 0.1, 0.1), 0)

    doc.recompute()
    try:
        import FreeCADGui as Gui
        Gui.ActiveDocument.ActiveView.fitAll()
    except Exception:
        pass

    out = App.getUserHomeDir() + "baseplate_v2"
    doc.saveAs(out + ".FCStd")
    obj.Shape.exportStep(out + ".step")
    obj.Shape.exportStl(out + ".stl")
    App.Console.PrintMessage("Saved %s.FCStd / .step / .stl\n" % out)
