PROGRAM PLC_PRG
VAR CONSTANT
    cInvBtn    : BOOL := FALSE;  // TRUE  if push-buttons read 0 when pressed
    cInvLB     : BOOL := TRUE;   // TRUE  if light barriers read 0 when beam is blocked
    cTimeout   : TIME := T#10S;  // max time for one movement step (then FAULT)
    cMillTime  : TIME := T#3S;   // milling duration
    cDrillTime : TIME := T#3S;   // drilling duration
END_VAR
VAR
    // ---- commands: change them online (double-click value, Ctrl+F7) ----
    bStart  : BOOL;                    // pulse TRUE to start (clears itself)
    bStop   : BOOL;                    // pulse TRUE to stop / acknowledge fault
    bManual : BOOL;                    // TRUE = manual test mode
    xMan    : ARRAY[1..10] OF BOOL;    // manual outputs Q1..Q10

    // ---- sequence ----
    iState, iPrevState, iFaultState : INT;
    bRun, bWatch : BOOL;
    tWatch, tMill, tDrill, tPause, tLoad : TON;

    // ---- inputs after polarity correction ----
    bS1Front, bS1Rear, bS2Front, bS2Rear : BOOL;                  // I1..I4 (pressed = TRUE)
    bLB_S1, bLB_Mill, bLB_Load, bLB_Drill, bLB_Exit : BOOL;       // I5, I6, I7, I8, I9 (blocked = TRUE)

    // ---- outputs ----
    qS1Back, qS1Fwd, qS2Back, qS2Fwd : BOOL;                      // Q1..Q4
    qFeed, qBeltMill, qMill, qBeltDrill, qDrill, qBeltExit : BOOL;// Q5..Q10
END_VAR


// ---------- 1. READ INPUTS ----------
bS1Rear   := GVL_IO.byBK_In.1  XOR cInvBtn;   // slider 1 rear button
bS1Front  := GVL_IO.byBK_In.0  XOR cInvBtn;   // slider 1 front button
bS2Rear   := GVL_IO.byBK_In.3  XOR cInvBtn;   // slider 2 rear button
bS2Front  := GVL_IO.byBK_In.2  XOR cInvBtn;   // slider 2 front button
bLB_S1    := GVL_IO.byBK_In.4  XOR cInvLB;    // light barrier slider 1
bLB_Mill  := GVL_IO.byBK_In.5  XOR cInvLB;    // light barrier milling
bLB_Load  := GVL_IO.byBK_In.6  XOR cInvLB;    // light barrier loading station
bLB_Drill := GVL_IO.byBK_In.7  XOR cInvLB;    // light barrier drilling
bLB_Exit  := GVL_IO.byDI16_1.0 XOR cInvLB;    // light barrier exit (I9)

// ---------- 2. TIMERS ----------
IF iState <> iPrevState THEN
    iPrevState := iState;
    bRun := FALSE;            // restart all timers after a state change
ELSE
    bRun := TRUE;
END_IF

bWatch := (iState <> 0) AND (iState <> 20) AND (iState <> 60)
          AND (iState <> 90) AND (iState <> 900);
tWatch(IN := bRun AND bWatch,                   PT := cTimeout);
tMill (IN := bRun AND (iState = 60),            PT := cMillTime);
tDrill(IN := bRun AND (iState = 90),            PT := cDrillTime);
tPause(IN := bRun AND (iState = 110) AND NOT bLB_Exit, PT := T#1S);
tLoad (IN := (iState = 20) AND bLB_Load,        PT := T#500MS);

// ---------- 3. ALL OUTPUTS OFF BY DEFAULT ----------
qS1Back := FALSE;  qS1Fwd := FALSE;  qS2Back := FALSE;  qS2Fwd := FALSE;
qFeed := FALSE;    qBeltMill := FALSE;  qMill := FALSE;
qBeltDrill := FALSE;  qDrill := FALSE;  qBeltExit := FALSE;

// ---------- 4. LOGIC ----------
IF bManual THEN
    // manual test mode: outputs follow xMan[1..10]
    iState := 0;
    qS1Back := xMan[1];   qS1Fwd := xMan[2];
    qS2Back := xMan[3];   qS2Fwd := xMan[4];
    qFeed := xMan[5];     qBeltMill := xMan[6];  qMill := xMan[7];
    qBeltDrill := xMan[8]; qDrill := xMan[9];    qBeltExit := xMan[10];

ELSIF bStop THEN
    iState := 0;
    bStop := FALSE;

ELSIF tWatch.Q THEN
    iFaultState := iState;     // remember where it got stuck
    iState := 900;

ELSE
    CASE iState OF

    0:  // IDLE
        IF bStart THEN
            iState := 10;
            bStart := FALSE;
        END_IF

    10: // HOMING - both sliders back to the rear switch
        qS1Back := NOT bS1Rear;
        qS2Back := NOT bS2Rear;
        IF bS1Rear AND bS2Rear THEN iState := 20; END_IF

    20: // WAIT for a workpiece in the loading station
        IF tLoad.Q THEN iState := 30; END_IF

    30: // FEED belt until the workpiece reaches slider 1
        qFeed := TRUE;
        IF bLB_S1 THEN iState := 40; END_IF

    40: // SLIDER 1 forward - pushes the part onto the milling belt
        qS1Fwd := TRUE;
        qBeltMill := TRUE;
        IF bS1Front THEN iState := 50; END_IF

    50: // SLIDER 1 back, milling belt carries part to the milling position
        qS1Back := NOT bS1Rear;
        qBeltMill := NOT bLB_Mill;
        IF bS1Rear AND bLB_Mill THEN iState := 60; END_IF

    60: // MILLING
        qMill := TRUE;
        IF tMill.Q THEN iState := 70; END_IF

    70: // SLIDER 2 forward - pushes the part onto the drilling belt
        qS2Fwd := TRUE;
        qBeltDrill := TRUE;
        IF bS2Front THEN iState := 80; END_IF

    80: // SLIDER 2 back, drilling belt carries part to the drilling position
        qS2Back := NOT bS2Rear;
        qBeltDrill := NOT bLB_Drill;
        IF bS2Rear AND bLB_Drill THEN iState := 90; END_IF

    90: // DRILLING
        qDrill := TRUE;
        IF tDrill.Q THEN iState := 100; END_IF

    100: // part moves to the exit belt
        qBeltDrill := TRUE;
        qBeltExit := TRUE;
        IF bLB_Exit THEN iState := 110; END_IF

    110: // exit belt runs until the part has left the exit light barrier
        qBeltExit := TRUE;
        IF tPause.Q THEN iState := 20; END_IF

    900: // FAULT - everything off, set bStop to acknowledge
        ;

    ELSE
        iState := 0;
    END_CASE
END_IF

// ---------- 5. SAFETY INTERLOCKS (always active, also in manual mode) ----------
IF qS1Fwd AND qS1Back THEN qS1Fwd := FALSE; qS1Back := FALSE; END_IF   // never both directions
IF qS2Fwd AND qS2Back THEN qS2Fwd := FALSE; qS2Back := FALSE; END_IF
IF bS1Front THEN qS1Fwd  := FALSE; END_IF                              // never drive into the end switch
IF bS1Rear  THEN qS1Back := FALSE; END_IF
IF bS2Front THEN qS2Fwd  := FALSE; END_IF
IF bS2Rear  THEN qS2Back := FALSE; END_IF

// ---------- 6. WRITE OUTPUTS ----------
GVL_IO.byBK_Out.0 := qS1Fwd;   // Q1 -> OUT1  slider 1 forward
GVL_IO.byBK_Out.1 := qS1Back;  // Q2 -> OUT2  slider 1 backward
GVL_IO.byBK_Out.2 := qS2Fwd;   // Q3 -> OUT3  slider 2 forward
GVL_IO.byBK_Out.3 := qS2Back;  // Q4 -> OUT4  slider 2 backward

GVL_IO.byDO16_1.0 := qFeed;       // Q5  loading conveyor
GVL_IO.byDO16_1.1 := qBeltMill;   // Q6  conveyor after slider 1
GVL_IO.byDO16_1.2 := qMill;       // Q7  milling motor
GVL_IO.byDO16_1.3 := qBeltDrill;  // Q8  conveyor after the miller
GVL_IO.byDO16_1.4 := qDrill;      // Q9  drilling motor
GVL_IO.byDO16_1.5 := qBeltExit;   // Q10 exit conveyor
