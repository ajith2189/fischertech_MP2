"""
Minimal baseplate v3: Fischertechnik 96790 + Raspberry Pi + FT I/O board + Phoenix coupler (+2 extensions) + 1 banana jack
RUN IN FREECAD: Macro > Macros... > Create > paste > Execute.
Units: mm. Datum: plate bottom-left corner (0,0). X = length, Y = depth (Y=0 is the front/operator edge).
Layout, front strip left to right:  banana jack | Raspberry Pi | FT I/O board (centred under machine) | Phoenix on DIN rail
Values marked  # CHECK  are placeholders: measure and edit.
Outputs (home folder): baseplate_v3.FCStd (editable), baseplate_v3.step, baseplate_v3.stl (plate only).
"""
import math

# ======================================================================
# PART 1 - PARAMETERS AND LAYOUT (pure Python, also used by make_drawing.py)
# ======================================================================
MARGIN = 20.0                                   # plate edge to nearest component
PLATE_T = 12.0                                  # 12 mm plywood or acrylic
CORNER_R = 10.0
SHOW_COMPONENT_BOXES = True

D_BENCH, D_DIN, D_ACC, D_PI, D_BANANA = 6.5, 5.5, 4.5, 2.8, 8.0   # M6, M5, M4, M2.5, banana jack  # CHECK jack hole

# --- Machine (Fischertechnik 96790) ---------------------------------------------
M_L, M_W, M_H = 475.0, 450.0, 270.0
STRIP_DEPTH = 120.0                             # Phoenix is the deepest item in the strip (119.8 mm)
STRIP_GAP = 15.0                                # strip to machine
MACHINE_X, MACHINE_Y = MARGIN, MARGIN + STRIP_DEPTH + STRIP_GAP
MACHINE_HOLE_INSET = 25.0                       # CHECK: 4 placeholder holes until the machine is measured

PLATE_L = M_L + 2 * MARGIN
PLATE_W = MACHINE_Y + M_W + MARGIN
STRIP_YC = MARGIN + STRIP_DEPTH / 2.0           # centre line of the electronics strip
CX = MACHINE_X + M_L / 2.0                      # machine centre line (FT I/O board sits here)

# --- Boards (Pi and FT I/O board are the same size) ------------------------------
BOARD_L, BOARD_W, BOARD_H = 85.0, 56.0, 20.0
BOARD_HOLES = [(3.5, 3.5), (61.5, 3.5), (3.5, 52.5), (61.5, 52.5)]   # 58 x 49 pattern  # CHECK for FT board
GAP = 20.0
FT_X = CX - BOARD_L / 2.0
PI_X = FT_X - GAP - BOARD_L
BY = STRIP_YC - BOARD_W / 2.0

# --- Phoenix coupler + 2 extension modules on a short DIN rail -------------------
PHX_RAIL_X0 = FT_X + BOARD_L + GAP
PHX_BK_L, PHX_EXT_L = 80.0, 12.2                # CHECK extension module width
PHX_W, PHX_H = 120.0, 72.0                      # across rail / height above plate
PHX_RAIL_LEN = PHX_BK_L + 2 * PHX_EXT_L + 20.0  # 10 mm end clearance each side
DIN_RAILS = {"DIN": (PHX_RAIL_X0, STRIP_YC, PHX_RAIL_LEN)}   # TS35, 35 mm wide, runs along X
DIN_HOLE_END_INSET, DIN_HOLE_PITCH = 10.0, 110.0

# name, rail, x_start, L(along rail), W(across), H
RAIL_PARTS = [
    ("Phoenix_IL_PN_BK",  "DIN", PHX_RAIL_X0 + 10.0,                      PHX_BK_L,  PHX_W, PHX_H),
    ("Phoenix_Ext_1",     "DIN", PHX_RAIL_X0 + 10.0 + PHX_BK_L,           PHX_EXT_L, PHX_W, PHX_H),
    ("Phoenix_Ext_2",     "DIN", PHX_RAIL_X0 + 10.0 + PHX_BK_L + PHX_EXT_L, PHX_EXT_L, PHX_W, PHX_H),
]

# name, x, y (bottom-left), L, W, H, hole offsets, hole dia, hole group
SCREW_PARTS = [
    ("Raspberry_Pi_3B",       PI_X, BY, BOARD_L, BOARD_W, BOARD_H, BOARD_HOLES, D_PI, "D"),
    ("Fischertechnik_IO_Board", FT_X, BY, BOARD_L, BOARD_W, BOARD_H, BOARD_HOLES, D_PI, "D"),
    ("Banana_Jack",           PI_X - 30.0 - 6.0, STRIP_YC - 6.0, 12.0, 12.0, 25.0, [(6, 6)], D_BANANA, "E"),
]

MACHINE = ("Fischertechnik_96790", MACHINE_X, MACHINE_Y, M_L, M_W, M_H)
DUCTS = []   # removed in the minimal design


def line_points(start, length, inset, pitch):
    span = length - 2 * inset
    n = max(1, int(math.ceil(span / pitch)))
    return [start + inset + i * span / n for i in range(n + 1)]


def build_holes():
    raw = []   # (group, x, y, d, note)
    for x in (12.0, PLATE_L - 12.0):
        for y in (12.0, PLATE_W - 12.0):
            raw.append(("A", x, y, D_BENCH, "Plate to bench (corner)"))
    for name, (x0, yc, L) in DIN_RAILS.items():
        for x in line_points(x0, L, DIN_HOLE_END_INSET, DIN_HOLE_PITCH):
            raw.append(("B", x, yc, D_DIN, "DIN rail (Phoenix)"))
    i = MACHINE_HOLE_INSET
    for hx in (MACHINE_X + i, MACHINE_X + M_L - i):
        for hy in (MACHINE_Y + i, MACHINE_Y + M_W - i):
            raw.append(("C", hx, hy, D_ACC, "Machine mount (PLACEHOLDER)"))
    for name, x, y, L, W, H, holes, d, g in SCREW_PARTS:
        for dx, dy in holes:
            raw.append((g, x + dx, y + dy, d, name))
    out, count = [], {}
    for g in "ABCDE":
        for (gg, x, y, d, note) in raw:
            if gg == g:
                count[g] = count.get(g, 0) + 1
                out.append(dict(id="%s%d" % (g, count[g]), x=round(x, 1), y=round(y, 1), d=d, note=note))
    return out


def footprints():
    r = []
    for name, rail, x, L, W, H in RAIL_PARTS:
        _, yc, _ = DIN_RAILS[rail]
        r.append((name, x, yc - W / 2.0, x + L, yc + W / 2.0))
    for name, x, y, L, W, H, _, _, _ in SCREW_PARTS:
        r.append((name, x, y, x + L, y + W))
    r.append((MACHINE[0], MACHINE_X, MACHINE_Y, MACHINE_X + M_L, MACHINE_Y + M_W))
    return r


def report():
    warn = []
    holes = build_holes()
    for h in holes:
        r = h["d"] / 2 + 3
        if not (r < h["x"] < PLATE_L - r and r < h["y"] < PLATE_W - r):
            warn.append("hole %s too close to edge" % h["id"])
    for i, a in enumerate(holes):
        for b in holes[i + 1:]:
            if math.hypot(a["x"] - b["x"], a["y"] - b["y"]) < 10:
                warn.append("holes %s and %s < 10 mm apart" % (a["id"], b["id"]))
    fp = footprints()
    for i, a in enumerate(fp):
        if a[1] < 0 or a[2] < 0 or a[3] > PLATE_L or a[4] > PLATE_W:
            warn.append("%s outside plate" % a[0])
        for b in fp[i + 1:]:
            if a[1] < b[3] - 1e-6 and b[1] < a[3] - 1e-6 and a[2] < b[4] - 1e-6 and b[2] < a[4] - 1e-6:
                warn.append("OVERLAP: %s / %s" % (a[0], b[0]))
    for w in warn:
        print("WARNING:", w)
    print("%d holes, plate %.1f x %.1f x %.0f mm - %s" % (len(holes), PLATE_L, PLATE_W, PLATE_T,
                                                          "OK" if not warn else "CHECK WARNINGS"))
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

    doc = App.newDocument("Baseplate_v3")
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
            ghost(name, x, yc - W / 2.0, L, W, H, (0.2, 0.5, 0.9))
        for name, x, y, L, W, H, _, _, _ in SCREW_PARTS:
            ghost(name, x, y, L, W, H, (0.2, 0.7, 0.3))
        n, mx, my, mL, mW, mH = MACHINE
        ghost(n, mx, my, mL, mW, mH, (0.9, 0.3, 0.3), 75)
        for rail, (x0, yc, L) in DIN_RAILS.items():
            ghost("DIN_rail", x0, yc - 17.5, L, 35.0, 7.5, (0.1, 0.1, 0.1), 0)

    doc.recompute()
    try:
        import FreeCADGui as Gui
        Gui.ActiveDocument.ActiveView.fitAll()
    except Exception:
        pass

    out = App.getUserHomeDir() + "baseplate_v3"
    doc.saveAs(out + ".FCStd")
    obj.Shape.exportStep(out + ".step")
    obj.Shape.exportStl(out + ".stl")
    App.Console.PrintMessage("Saved %s.FCStd / .step / .stl\n" % out)
