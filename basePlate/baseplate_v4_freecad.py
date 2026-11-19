"""
Baseplate v4 - researched dimensions, structured geometry
Fischertechnik 96790 + FT I/O board (centred) + Raspberry Pi 3B (left) + Phoenix IL PN BK + 2 Inline modules (right) + 1 banana jack
RUN IN FREECAD: Macro > Macros... > Create > paste > Execute.
Units mm. Datum = plate bottom-left corner (0,0). X = length, Y = depth (Y=0 front/operator edge), Z up (plate top = PLATE_T).
Outputs (home folder): baseplate_v4.FCStd (editable), baseplate_v4.step, baseplate_v4.stl (plate only).
Every dimension is tagged with its source in COMPONENT_TABLE (bottom of PART 1). "ASSUMED" = verify.
"""
import math

# ======================================================================
# PART 1 - PARAMETERS AND LAYOUT (pure Python; also read by make_drawing.py)
# ======================================================================
MARGIN, PLATE_T, CORNER_R = 20.0, 12.0, 10.0
SHOW_COMPONENTS = True

# ---- Fischertechnik 96790 (listing: 475 x 450 x 270; may be the packed size -> measure the real wooden board)
M_L, M_W, M_H = 475.0, 450.0, 270.0
MACHINE_HOLE_INSET = 25.0                      # ASSUMED: 4 placeholder holes until measured

# ---- Raspberry Pi 3 Model B (official mechanical drawing)
PI_L, PI_W, PI_T, PI_HOLE_D = 85.0, 56.0, 1.4, 2.75
PI_HOLES = [(3.5, 3.5), (61.5, 3.5), (3.5, 52.5), (61.5, 52.5)]    # (u along 85, v along 56): 58 x 49 pattern
STANDOFF = 6.0                                 # M2.5 standoff height (our choice)
PI_FACE_FRONT = True                           # rotate so Ethernet/USB face the operator edge
# simplified connector blocks, native coords (u0,u1,v0,v1,height); ASSUMED from official drawing positions
PI_BLOCKS = [("Ethernet", 66.0, 87.0, 2.25, 18.25, 13.5),
             ("USB_1",    71.0, 87.0, 22.35, 35.65, 15.7),
             ("USB_2",    71.0, 87.0, 40.35, 53.65, 15.7),
             ("GPIO",      7.0, 58.0, 50.0, 55.0,  8.5)]
PI_OVERHANG = 2.0

# ---- Fischertechnik I/O board: same size as Pi (per project owner), pattern assumed equal
FT_L, FT_W, FT_T, FT_ENV_H, FT_HOLE_D = 85.0, 56.0, 1.6, 20.0, 2.75

# ---- Phoenix Contact Inline station (datasheets)
BK = ("Phoenix_IL_PN_BK_DI8_DO4 (2703994)", 80.0)
EXT = [("IB_IL_24_DI_8_PAC (2861247)", 48.8), ("IB_IL_24_DO_8_PAC (2861289)", 48.8)]
MOD_W, MOD_H = 119.8, 71.5                      # across rail / depth (same for all Inline modules)
CLAMP_L, CLAMP_W, CLAMP_H = 9.5, 35.3, 50.5     # E/UK end clamp (1201442)

# ---- DIN rail TS35 x 7.5 (EN 60715)
RAIL_W, RAIL_H, RAIL_T, CROWN_W = 35.0, 7.5, 1.0, 27.0
SLOT_L, SLOT_W, SLOT_PITCH = 15.0, 5.2, 25.0    # ASSUMED typical perforation
STATION_L = BK[1] + sum(e[1] for e in EXT)
RAIL_LEN = math.ceil((STATION_L + 2 * CLAMP_L + 20.0) / SLOT_PITCH) * SLOT_PITCH   # -> 225

# ---- Banana jack (4 mm panel socket): hole 8.0, counterbore from below because most jacks accept <= 4 mm panel
D_BANANA, BANANA_BODY = 8.0, 12.0
BANANA_WEB, D_BANANA_CB = 3.0, 18.0
CB_DEPTH = PLATE_T - BANANA_WEB

# ---- Hole diameters from project spec
D_BENCH, D_DIN, D_ACC = 6.5, 5.5, 4.5

# ---- Layout
STRIP_DEPTH, STRIP_GAP, GAP = 120.0, 15.0, 20.0
MACHINE_X, MACHINE_Y = MARGIN, MARGIN + STRIP_DEPTH + STRIP_GAP
CX = MACHINE_X + M_L / 2.0                      # machine centre line
STRIP_YC = MARGIN + STRIP_DEPTH / 2.0
FT_X, FT_Y = CX - FT_L / 2.0, STRIP_YC - FT_W / 2.0
PI_FP_W, PI_FP_L = (PI_W, PI_L) if PI_FACE_FRONT else (PI_L, PI_W)
PI_X0, PI_Y0 = FT_X - GAP - PI_FP_W, STRIP_YC - PI_FP_L / 2.0
BANANA_X, BANANA_Y = PI_X0 - 25.0, STRIP_YC
RAIL_X0 = FT_X + FT_L + GAP
PLATE_L = max(MACHINE_X + M_L, RAIL_X0 + RAIL_LEN) + MARGIN
PLATE_W = MACHINE_Y + M_W + MARGIN
STATION_X0 = RAIL_X0 + (RAIL_LEN - (STATION_L + 2 * CLAMP_L)) / 2.0    # first end clamp


def pi_xy(u, v):
    """Pi native board coords -> plate coords."""
    if PI_FACE_FRONT:
        return PI_X0 + v, PI_Y0 + PI_L - u
    return PI_X0 + u, PI_Y0 + v


def slot_centres():
    n = int((RAIL_LEN - 10.0 - SLOT_L) // SLOT_PITCH) + 1       # 9 slots, symmetric
    off = (RAIL_LEN - (n - 1) * SLOT_PITCH) / 2.0
    return [RAIL_X0 + off + k * SLOT_PITCH for k in range(n)]


def build_holes():
    raw = []   # group, x, y, d, note, cbore(d, depth) or None
    for x in (12.0, PLATE_L - 12.0):
        for y in (12.0, PLATE_W - 12.0):
            raw.append(("A", x, y, D_BENCH, "Plate to bench (M6)", None))
    sc = slot_centres()
    for x in (sc[0], sc[len(sc) // 2], sc[-1]):
        raw.append(("B", x, STRIP_YC, D_DIN, "DIN rail slot centre (M5)", None))
    i = MACHINE_HOLE_INSET
    for hx in (MACHINE_X + i, MACHINE_X + M_L - i):
        for hy in (MACHINE_Y + i, MACHINE_Y + M_W - i):
            raw.append(("C", hx, hy, D_ACC, "Machine mount (M4) PLACEHOLDER", None))
    for u, v in PI_HOLES:
        x, y = pi_xy(u, v)
        raw.append(("D", x, y, PI_HOLE_D, "Raspberry Pi M2.5", None))
    for u, v in PI_HOLES:
        raw.append(("D", FT_X + u, FT_Y + v, FT_HOLE_D, "FT I/O board M2.5 (assumed)", None))
    raw.append(("E", BANANA_X, BANANA_Y, D_BANANA, "Banana jack; c'bore %.0f x %.0f from underside" % (D_BANANA_CB, CB_DEPTH),
                (D_BANANA_CB, CB_DEPTH)))
    out, n = [], {}
    for g in "ABCDE":
        for (gg, x, y, d, note, cb) in raw:
            if gg == g:
                n[g] = n.get(g, 0) + 1
                out.append(dict(id="%s%d" % (g, n[g]), x=round(x, 1), y=round(y, 1), d=d, note=note, cb=cb))
    return out


def footprints():
    r = []
    r.append(("Machine", MACHINE_X, MACHINE_Y, MACHINE_X + M_L, MACHINE_Y + M_W))
    r.append(("FT I/O board", FT_X, FT_Y, FT_X + FT_L, FT_Y + FT_W))
    r.append(("Raspberry Pi 3B", PI_X0, PI_Y0 - (PI_OVERHANG if PI_FACE_FRONT else 0),
              PI_X0 + PI_FP_W, PI_Y0 + PI_FP_L))
    r.append(("Banana jack", BANANA_X - BANANA_BODY / 2, BANANA_Y - BANANA_BODY / 2,
              BANANA_X + BANANA_BODY / 2, BANANA_Y + BANANA_BODY / 2))
    r.append(("DIN rail + station", RAIL_X0, STRIP_YC - MOD_W / 2, RAIL_X0 + RAIL_LEN, STRIP_YC + MOD_W / 2))
    return r


def station_items():
    """name, x0, x1, across(width), height above rail top, kind"""
    items, x = [], STATION_X0
    items.append(("End clamp E/UK", x, x + CLAMP_L, CLAMP_W, CLAMP_H, "clamp")); x += CLAMP_L
    for name, w in [BK] + EXT:
        items.append((name, x, x + w, MOD_W, MOD_H, "module")); x += w
    items.append(("End clamp E/UK", x, x + CLAMP_L, CLAMP_W, CLAMP_H, "clamp"))
    return items


COMPONENT_TABLE = [
    ("Fischertechnik 96790 Indexed Line 24V", "475 x 450 x 270", "Reseller/fischertechnik listing; verify (may be packed size)"),
    ("FT I/O board (PCB 211289)", "85 x 56 (as Pi)", "Project owner statement; pattern ASSUMED"),
    ("Raspberry Pi 3 Model B", "85 x 56 x 17; holes 58x49 @3.5; dia 2.75; R3", "Raspberry Pi official mechanical drawing"),
    ("Phoenix IL PN BK DI8 DO4 2TX-PAC 2703994", "80 x 119.8 x 71.5", "Phoenix Contact datasheet"),
    ("IB IL 24 DI 8-PAC 2861247", "48.8 x 119.8 x 71.5", "Phoenix Contact datasheet"),
    ("IB IL 24 DO 8-PAC 2861289", "48.8 x 119.8 x 71.5", "Phoenix Contact datasheet"),
    ("End clamp E/UK 1201442", "9.5 x 35.3 x 50.5", "Phoenix Contact accessory data"),
    ("DIN rail TS35 x 7.5", "35 x 7.5 x 1.0; slots 15 x 5.2 @25", "EN 60715 / Phoenix NS 35/7,5; slots typical"),
    ("4 mm banana panel socket", "hole 8.0; max panel 4 mm; body ~12", "Typical datasheets; check purchased part"),
]


def report():
    warn, holes = [], build_holes()
    for h in holes:
        r = h["d"] / 2 + 3
        if not (r < h["x"] < PLATE_L - r and r < h["y"] < PLATE_W - r):
            warn.append("hole %s too close to edge" % h["id"])
    for i, a in enumerate(holes):
        for b in holes[i + 1:]:
            if math.hypot(a["x"] - b["x"], a["y"] - b["y"]) < 10:
                warn.append("holes %s / %s < 10 mm apart" % (a["id"], b["id"]))
    fp = footprints()
    for i, a in enumerate(fp):
        if a[1] < 0 or a[2] < 0 or a[3] > PLATE_L or a[4] > PLATE_W:
            warn.append("%s outside plate" % a[0])
        for b in fp[i + 1:]:
            if a[1] < b[3] - 1e-6 and b[1] < a[3] - 1e-6 and a[2] < b[4] - 1e-6 and b[2] < a[4] - 1e-6:
                warn.append("OVERLAP %s / %s" % (a[0], b[0]))
    for w in warn:
        print("WARNING:", w)
    print("%d holes | plate %.1f x %.1f x %.0f | rail %.0f | %s" % (
        len(holes), PLATE_L, PLATE_W, PLATE_T, RAIL_LEN, "OK" if not warn else "CHECK"))
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
    cutters = []
    for h in HOLES:
        cutters.append(Part.makeCylinder(h["d"] / 2.0, PLATE_T + 2, V(h["x"], h["y"], -1)))
        if h["cb"]:
            cutters.append(Part.makeCylinder(h["cb"][0] / 2.0, h["cb"][1] + 1, V(h["x"], h["y"], -1)))
    plate = plate.cut(Part.makeCompound(cutters))

    doc = App.newDocument("Baseplate_v4")
    obj = doc.addObject("Part::Feature", "Baseplate")
    obj.Shape = plate

    def add(name, shape, color=None, transp=0):
        o = doc.addObject("Part::Feature", name)
        o.Shape = shape
        try:
            if color:
                o.ViewObject.ShapeColor = color
            o.ViewObject.Transparency = transp
        except Exception:
            pass
        return o

    def box(x0, y0, z0, dx, dy, dz):
        return Part.makeBox(dx, dy, dz, V(x0, y0, z0))

    if SHOW_COMPONENTS:
        zt = PLATE_T
        # --- machine (envelope)
        add("FT_96790_envelope", box(MACHINE_X, MACHINE_Y, zt, M_L, M_W, M_H), (0.85, 0.3, 0.3), 75)
        # --- DIN rail: top-hat profile with perforated crown
        r = RAIL_LEN
        y0 = STRIP_YC
        crown = box(RAIL_X0, y0 - CROWN_W / 2, zt, r, CROWN_W, RAIL_T)
        slots = [box(sx - SLOT_L / 2, y0 - SLOT_W / 2, zt - 1, SLOT_L, SLOT_W, RAIL_T + 2) for sx in slot_centres()]
        crown = crown.cut(Part.makeCompound(slots))
        wall1 = box(RAIL_X0, y0 - CROWN_W / 2, zt, r, RAIL_T, RAIL_H)
        wall2 = box(RAIL_X0, y0 + CROWN_W / 2 - RAIL_T, zt, r, RAIL_T, RAIL_H)
        fl1 = box(RAIL_X0, y0 - RAIL_W / 2, zt + RAIL_H - RAIL_T, r, (RAIL_W - CROWN_W) / 2 + RAIL_T, RAIL_T)
        fl2 = box(RAIL_X0, y0 + CROWN_W / 2 - RAIL_T, zt + RAIL_H - RAIL_T, r, (RAIL_W - CROWN_W) / 2 + RAIL_T, RAIL_T)
        add("DIN_rail_TS35", crown.fuse([wall1, wall2, fl1, fl2]), (0.75, 0.75, 0.78))
        # --- Inline station
        zr = zt + RAIL_H
        for name, xa, xb, across, h, kind in station_items():
            col = (0.55, 0.55, 0.58) if kind == "clamp" else ((0.35, 0.65, 0.35) if "BK" in name else (0.3, 0.55, 0.85))
            add(name.split(" ")[0] + "_" + str(int(xa)), box(xa, y0 - across / 2, zr, xb - xa, across, h), col, 20)
        # --- Raspberry Pi on standoffs
        zb = zt + STANDOFF
        for u, v in PI_HOLES:
            x, y = pi_xy(u, v)
            add("Standoff_Pi", Part.makeCylinder(2.5, STANDOFF, V(x, y, zt)), (0.8, 0.7, 0.2))
        if PI_FACE_FRONT:
            add("Pi_PCB", box(PI_X0, PI_Y0, zb, PI_W, PI_L, PI_T), (0.1, 0.5, 0.2))
        else:
            add("Pi_PCB", box(PI_X0, PI_Y0, zb, PI_L, PI_W, PI_T), (0.1, 0.5, 0.2))
        for nm, u0, u1, v0, v1, h in PI_BLOCKS:
            xa, ya = pi_xy(u1, v0); xb, yb = pi_xy(u0, v1)
            x0, x1, y0b, y1b = min(xa, xb), max(xa, xb), min(ya, yb), max(ya, yb)
            add("Pi_" + nm, box(x0, y0b, zb + PI_T, x1 - x0, y1b - y0b, h), (0.7, 0.7, 0.7))
        # --- FT I/O board
        for u, v in PI_HOLES:
            add("Standoff_FT", Part.makeCylinder(2.5, STANDOFF, V(FT_X + u, FT_Y + v, zt)), (0.8, 0.7, 0.2))
        add("FT_IO_board_PCB", box(FT_X, FT_Y, zb, FT_L, FT_W, FT_T), (0.1, 0.4, 0.6))
        add("FT_IO_board_envelope(assumed)", box(FT_X, FT_Y, zb + FT_T, FT_L, FT_W, FT_ENV_H), (0.1, 0.4, 0.6), 80)
        # --- banana jack: 2 mm above panel web, body below inside counterbore
        add("Banana_jack", Part.makeCylinder(BANANA_BODY / 2.0, 3.0, V(BANANA_X, BANANA_Y, zt)), (0.8, 0.1, 0.1))

    doc.recompute()
    try:
        import FreeCADGui as Gui
        Gui.ActiveDocument.ActiveView.fitAll()
    except Exception:
        pass
    out = App.getUserHomeDir() + "baseplate_v4"
    doc.saveAs(out + ".FCStd")
    obj.Shape.exportStep(out + ".step")
    obj.Shape.exportStl(out + ".stl")
    App.Console.PrintMessage("Saved %s.FCStd / .step / .stl\n" % out)
