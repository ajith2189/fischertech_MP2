# IL PN BK DI8 DO4 2TX-PAC — Data Sheet
**PROFINET bus coupler, 8 inputs, 24 V DC, 4 outputs, 24 V DC, 500 mA, complete with I/O connectors**  
**Document ID:** `7410_en_12`  
**Manufacturer:** PHOENIX CONTACT (2017-07-24)

---

## 1. Description

This description applies to firmware version **2.30 or later**.

The bus coupler is the link between a PROFINET network and the Inline installation system. In addition, it is used to acquire and output digital signals.

Up to 61 Inline devices can be connected at any point to an existing PROFINET network using the bus coupler. The bus coupler and the Inline devices form a station with a maximum of 63 local bus devices. Here, the inputs and outputs of the bus coupler together form the first local bus device.

### Features
* 2 x Ethernet twisted pair according to 802.3 with auto negotiation and auto crossover
* Transmission speed of 100 Mbps
* IP parameter setting using the PROFINET controller
* Connection to the PROFINET network via 8-pos. RJ45 socket
* Electrical isolation between Ethernet interface and logic
* Ethernet TCP/IP (100 Base-TX, Management via SNMP)
* Connection of up to 61 other Inline devices
* Connection of a maximum of 16 PCP devices
* Supported protocols: SNMPv1, TFTP, PROFINET, LLDP and MRP (from firmware 3.21)
* PROFINET IRT (Firmware 4.00 or later)
* Conformance with PROFINET specification V2.3 (Firmware 4.00 or later)
* PROFINET Netload Class III (Firmware 4.00 or later)
* 8 digital inputs, 4 digital outputs
* Automatic detection of the transmission speed in the local bus (500 kbps or 2 Mbps)
* Diagnostic and status indicators
* **Hardware version 02 or later:** Approved for use in zone 2 potentially explosive areas

> **WARNING: Explosion hazard when used in potentially explosive areas**  
> When using the terminal in potentially explosive areas, observe the corresponding notes.

> **Note:** This data sheet is only valid in association with the `IL SYS INST UM E` user manual. Make sure you always use the latest documentation. It can be downloaded from the product at `phoenixcontact.net/products`. Here you will also find the current GSDML file.

---

## 2. Table of Contents

1. Description (p. 1)
2. Table of contents (p. 2)
3. Ordering data (p. 3)
4. Technical data (p. 5)
5. Internal circuit diagram (p. 10)
6. Local status and diagnostic indicators (p. 11)
7. Diagnostic indicators for PROFINET (p. 12)
8. Connection of PROFINET, power supply, actuators, and sensors (p. 13)
   * 8.1 Connecting PROFINET (p. 13)
   * 8.2 Terminal point assignment of the Inline connectors (p. 14)
9. Connection example (p. 14)
10. Instructions on using the bus coupler in the potentially explosive area (p. 15)
11. Mapping inputs and outputs to PROFINET (p. 15)
12. Process data (p. 15)
    * 12.1 Terminal point assignment of local outputs to the OUT process data (p. 15)
    * 12.2 Terminal point assignment of the local inputs to the IN process data (p. 15)
13. Startup (p. 16)
14. Parameterization (p. 16)
15. Firmware update (p. 17)
16. Physical Device - PDev (p. 17)
17. Link Layer Discovery Protocol - LLDP (p. 17)
18. Device replacement (p. 17)
19. Applicative system redundancy for process data (p. 18)
20. Failsafe behavior (p. 18)
21. Acyclic PROFINET communication (p. 18)
22. Mailbox communication (p. 18)
23. Byte rotation for 16 and 32-channel Inline terminals with a SIMATIC S7 controller (p. 19)
    * 23.1 Byte rotation for IB IL 24 DI 16... and IB IL 24 DO 16... terminals (p. 19)
    * 23.2 Byte rotation for IB IL 24 DI 32... and IB IL 24 DO 32... terminals (p. 20)

---

## 3. Ordering Data

### Bus Coupler
| Description | Type | Order No. | Pcs./Pkt. |
| :--- | :--- | :--- | :--- |
| PROFINET bus coupler, 8 inputs, 24 V DC, 4 outputs, 24 V DC, 500 mA, complete with I/O connectors | `IL PN BK DI8 DO4 2TX-PAC` | `2703994` | 1 |

### Accessories
| Description | Type | Order No. | Pcs./Pkt. |
| :--- | :--- | :--- | :--- |
| Quick mounting end clamp for NS 35/7,5 DIN rail or NS 35/15 DIN rail, with marking option, width: 9.5 mm, color: gray (Assembly) | `CLIPFIX 35` | `3022218` | 50 |
| Insert strip, Sheet, white, unlabeled, can be labeled with: Office printing systems: Laser printer, Mounting type: Insert, Lettering field: $62 \times 46\text{ mm}$ (Marking) | `ESL 62X46` | `0809502` | 5 |
| Labeling field, width: $48.8\text{ mm}$ (Marking) | `IB IL FIELD 8` | `2727515` | 10 |
| Insert strip, Sheet, white, unlabeled, can be labeled with: Office printing systems: Laser printer, Mounting type: Insert, Lettering field: $62 \times 10\text{ mm}$ (Marking) | `ESL 62X10` | `0809492` | 1 |
| Labeling field, width: $12.2\text{ mm}$ (Marking) | `IB IL FIELD 2` | `2727501` | 10 |
| RJ45 connector, shielded, with bend protection sleeve, 2 pieces, gray for straight cables, for assembly on site. For connections that are not crossed, it is recommended that you use the connector set with gray bend protection sleeve. (Connector/Adapter) | `FL PLUG RJ45 GR/2` | `2744856` | 1 |
| RJ45 connector, shielded, with bend protection sleeve, 2 pieces, green for crossed cables, for assembly on site. For connections that are crossed, it is recommended that the connector set with green bend protection sleeves is used. (Connector/Adapter) | `FL PLUG RJ45 GN/2` | `2744571` | 1 |
| CAT5-SF/UTP cable ($\text{J-02YS(ST)C HP } 2 \times 2 \times 24\text{ AWG}$), heavy-duty installation cable, $2 \times 2 \times 0.22\text{ mm}^2$, solid conductor, shielded, outer sheath: $7.8\text{ mm}$ diameter, inner sheath: $5.75\text{ mm} \pm 0.15\text{ mm}$ diameter (Cable/conductor) | `FL CAT5 HEAVY` | `2744814` | 1 |
| CAT5-SF/UTP cable ($\text{J-LI02YS(ST)CH } 2 \times 2 \times 26\text{ AWG}$), light-duty, flexible installation cable $2 \times 2 \times 0.14\text{ mm}^2$ stranded, shielded, outer sheath: $5.75\text{ mm} \pm 0.15\text{ mm}$ diameter (Cable/conductor) | `FL CAT5 FLEX` | `2744830` | 1 |
| Crimping pliers, for assembling the RJ45 plugs FL PLUG RJ45..., for assembly on site (Tools) | `FL CRIMPTOOL` | `2744869` | 1 |
| End clamp, Width: $9.5\text{ mm}$, Height: $35.3\text{ mm}$, Length: $50.5\text{ mm}$, Color: gray (Assembly) | `E/UK` | `1201442` | 50 |
| Connector set, for Inline bus coupler with I/Os mounted in rows (Connector/Adapter) | `IL BKDIO-PLSET` | `2878599` | 1 |

### Documentation
| Description | Type | Order No. | Pcs./Pkt. |
| :--- | :--- | :--- | :--- |
| User manual, English, Automation terminals of the Inline product range | `IL SYS INST UM E` | — | — |
| Quick start guide, English, for PC Worx | `UM QS EN PC WORX` | — | — |
| Quick Start Guide, English, for planning INTERBUS devices in a PROFINET network | `UM QS EN PROFINET PROXY IB` | — | — |
| User manual, English, for the Modular Managed Switch System | `FL SWITCH MM HS UM E` | — | — |
| Application note, English, Inline terminals for use in zone 2 potentially explosive areas | `AH EN IL EX ZONE 2` | — | — |
| Application note, German/English, I/O modules at bus couplers | `AH IL BK IO LIST` | — | — |
| User manual, English, PROFINET basics | `UM EN PROFINET SYS` | — | — |
| User manual, English, Installation and operation of the PC Worx Firmware Updater software | `UM EN PC WORX FIRMWARE UPDATER` | — | — |

---

## 4. Technical Data

### Dimensions (nominal sizes in mm)
* **Width:** $80\text{ mm}$
* **Height:** $119.8\text{ mm}$
* **Depth:** $71.5\text{ mm}$
* **Note on dimensions:** Specifications with connectors

### General Data
* **Color:** green
* **Weight:** $340\text{ g}$ (with connectors)
* **Ambient temperature (operation):** $-25^\circ\text{C} \dots 55^\circ\text{C}$ (observe derating)
* **Ambient temperature (storage/transport):** $-40^\circ\text{C} \dots 85^\circ\text{C}$
* **Permissible humidity (operation):** $10\% \dots 95\%$ (according to DIN EN 61131-2)
* **Permissible humidity (storage/transport):** $10\% \dots 95\%$ (according to DIN EN 61131-2)
* **Air pressure (operation):** $70\text{ kPa} \dots 106\text{ kPa}$ (up to $3000\text{ m}$ above sea level)
* **Air pressure (storage/transport):** $70\text{ kPa} \dots 106\text{ kPa}$ (up to $3000\text{ m}$ above sea level)
* **Degree of protection:** IP20
* **Protection class:** III, IEC 61140, EN 61140, VDE 0140-1

### Connection Data
* **Designation:** Inline connector
* **Connection method:** Spring-cage connection
* **Conductor cross section solid / stranded:** $0.08\text{ mm}^2 \dots 1.5\text{ mm}^2$ / $0.08\text{ mm}^2 \dots 1.5\text{ mm}^2$
* **Conductor cross section [AWG]:** $28 \dots 16$
* **Stripping length:** $8\text{ mm}$

### Connection Data for UL Approvals
* **Designation:** Inline connector
* **Connection method:** Spring-cage connection
* **Conductor cross section solid / stranded:** $0.2\text{ mm}^2 \dots 1.5\text{ mm}^2$ / $0.2\text{ mm}^2 \dots 1.5\text{ mm}^2$
* **Conductor cross section [AWG]:** $24 \dots 16$
* **Stripping length:** $8\text{ mm}$

### Interface PROFINET
* **Number:** 2
* **Connection method:** RJ45 socket, auto negotiation
* **Transmission speed:** $100\text{ Mbps}$ (acc. to PROFINET standard)
* **Transmission physics:** Ethernet in RJ45 twisted pair
* **Transmission length:** max. $100\text{ m}$

### Interface Inline Local Bus
* **Connection method:** Inline data jumper
* **Transmission speed:** $500\text{ kbps}$ / $2\text{ Mbps}$ (Automatic detection, no combined system)

### System Limits
* **Amount of process data:** max. $488\text{ Byte}$ (Max. $244\text{ bytes}$ IN - max. $244\text{ bytes}$ OUT)
* **IN process data for I/O modules that can be aligned:** $244\text{ Byte}$
* **OUT process data for I/O modules that can be aligned:** $244\text{ Byte}$
* **Number of supported devices:** max. 63 (per station)
* **Number of local bus devices that can be connected:** max. 61 (on board I/Os are two devices)
* **Number of devices with parameter channel:** max. 16
* **Number of supported branch terminals with remote bus branch:** 0

> **Note:** Observe the logic current consumption of each device when configuring an Inline station! It is specified in every terminal-specific data sheet. The current consumption can differ depending on the individual terminal. The permissible number of devices that can be connected therefore depends on the specific station structure.

### PROFINET
* **Device function:** PROFINET device
* **Update rate:** min. $1\text{ ms}$ (depending on the size of the bus system)
* **Protocols supported:** PROFINET, PDev, TFTP, ICMP, LLDP

### Power Supply for Module Electronics
* **Connection method:** Spring-cage connection
* **Designation:** Bus coupler supply $U_{BC}$: Communications power $U_{L}$ ($7.5\text{ V}$) and the analog supply $U_{ANA}$ ($24\text{ V}$) are generated from the bus coupler supply.
* **Supply voltage:** $24\text{ V DC}$ (via Inline connector)
* **Supply voltage range:** $19.2\text{ V DC} \dots 30\text{ V DC}$ (including all tolerances, including ripple)
* **Supply current:** $138\text{ mA}$
* **Current consumption:** typ. $138\text{ mA}$ (from $U_{BK}$), max. $0.91\text{ A DC}$ (from $U_{BK}$)
* **Power dissipation:** typ. $3\text{ W}$ (entire device)

### Power Consumption
> **NOTE: Electronics may be damaged when overloaded**  
> Provide external fuses for the $24\text{ V}$ areas $U_{BK}$, $U_{M}$, and $U_{S}$. The power supply unit must be able to supply four times the nominal current of the external fuse, to ensure that it trips in the event of an error.

* **Main circuit supply $U_{M}$:** $24\text{ V DC} -15\%/+20\%$ (acc. to EN 61131-2)
* **Supply voltage range $U_{M}$:** $19.2\text{ V DC} \dots 30\text{ V DC}$ (including all tolerances, including ripple)
* **Power supply at $U_{M}$:** max. $8\text{ A DC}$ (Sum of $U_{M} + U_{S}$; $4\text{ A}$, maximum, when used in potentially explosive areas.)
* **Current consumption from $U_{M}$:** max. $8\text{ A DC}$
* **Segment circuit supply $U_{S}$:** $24\text{ V DC} -20\%/+20\%$ (acc. to EN 61131-2)
* **Supply voltage range $U_{S}$:** $19.2\text{ V DC} \dots 30\text{ V DC}$ (including all tolerances, including ripple)
* **Power supply at $U_{S}$:** max. $8\text{ A DC}$ (Sum of $U_{M} + U_{S}$; $4\text{ A}$, maximum, when used in potentially explosive areas.)
* **Current consumption from $U_{S}$:** max. $8\text{ A DC}$
* **Communications power $U_{L}$:** $7.5\text{ V DC} \pm 5\%$
* **Power supply at $U_{L}$:** max. $0.8\text{ A DC}$ (observe derating)
* **I/O supply voltage $U_{ANA}$:** $24\text{ V DC} -15\%/+20\%$
* **Supply voltage range $U_{ANA}$:** $19.2\text{ V DC} \dots 30\text{ V DC}$ (including all tolerances, including ripple)
* **Power supply at $U_{ANA}$:** max. $0.5\text{ A DC}$ (observe derating)

### Power Dissipation
* **Maximum power dissipation for nominal condition:** max. $3.3\text{ W}$

### Digital Inputs
* **Number of inputs:** 8
* **Connection method:** Inline connector
* **Connection technology:** 2, 3-wire
* **Description of the input:** EN 61131-2 type 1
* **Input characteristic curve:** IEC 61131-2 type 1
* **Nominal input voltage:** $24\text{ V DC}$
* **Nominal input current:** typ. $3\text{ mA}$
* **Current flow:** Limited to $3\text{ mA}$, maximum
* **Input voltage range "0" signal:** $-30\text{ V DC} \dots 5\text{ V DC}$
* **Input voltage range "1" signal:** $15\text{ V DC} \dots 30\text{ V DC}$
* **Delay at signal change from 0 to 1:** typ. $5\text{ ms}$
* **Delay at signal change from 1 to 0:** typ. $5\text{ ms}$
* **Permissible conductor length to the sensor:** $100\text{ m}$
* **Polarity protection diode:** Reverse polarity protection

### Digital Outputs
* **Number of outputs:** 4
* **Connection method:** Inline connector
* **Connection technology:** 2, 3-wire
* **Nominal output voltage:** $24\text{ V DC}$
* **Voltage difference with nominal current:** $< 1\text{ V}$
* **Maximum output current per channel:** $500\text{ mA}$
* **Maximum output current per device:** $2\text{ A}$
* **Nominal load, ohmic:** $12\text{ W}$
* **Nominal load, inductive:** $12\text{ VA}$ ($1.2\text{ H}$, $48\ \Omega$)
* **Nominal load, lamp:** $12\text{ W}$
* **Signal delay:** typ. $1.2\text{ ms}$
* **Signal delay when switching on an ohmic nominal load:** max. $50\ \mu\text{s}$ (in the case of $0.5\text{ A}$ load)
* **Signal delay when switching off an ohmic nominal load:** max. $250\ \mu\text{s}$ (in the case of $0.5\text{ A}$ load)
* **Maximum operating frequency with inductive nominal load:** $0.5\text{ Hz}$ ($1.2\text{ H}$, $48\ \Omega$)
* **Reaction time with short-circuit:** $1.2\text{ ms}$
* **Behavior at voltage switch-off:** The output follows the power supply without delay
* **Limitation of the voltage induced on circuit interruption:** approx. $-30\text{ V}$
* **Output current when switched off:** max. $10\ \mu\text{A}$ (When not loaded, a voltage can be measured even at an output that is not set.)
* **Behavior with overload:** Auto restart
* **Behavior with inductive overload:** Output can be destroyed
* **Reverse voltage resistance to short pulses:** Reverse voltage proof
* **Resistance to permanent reverse voltage:** max. $2\text{ A}$
* **Overcurrent shut-down:** min. $0.7\text{ A}$
* **Short-circuit and overload protection:** Free running circuit in output driver

### Error Messages to the Higher Level Control or Computer System
* **Short-circuit/overload of the digital outputs:** Yes
* **Sensor supply failure:** Yes
* **Failure of the actuator supply:** Yes

### Protective Circuit
* **Surge protection, protection against polarity reversal of the supply voltage:** $35\text{ V}$ suppressor diode

### Mechanical Tests
* **Vibration resistance in acc. with EN 60068-2-6 / IEC 60068-2-6:** $5g$
* **Shock in acc. with EN 60068-2-27 / IEC 60068-2-27:** Operation: $25g$, $11\text{ ms}$ duration, semi-sinusoidal shock impulse

### Conformance with EMC Directive 2014/30/EU
* **Noise immunity test in accordance with EN 61000-6-2:**
  * **Electrostatic discharge (ESD) EN 61000-4-2 / IEC 61000-4-2:** Criterion B, $6\text{ kV}$ contact discharge, $8\text{ kV}$ air discharge
  * **Electromagnetic fields EN 61000-4-3 / IEC 61000-4-3:** Criterion A, Field intensity: $10\text{ V/m}$
  * **Fast transients (burst) EN 61000-4-4 / IEC 61000-4-4:** Criterion A, all interfaces $1\text{ kV}$; Criterion B, all interfaces $2\text{ kV}$
  * **Transient overvoltage (surge) EN 61000-4-5 / IEC 61000-4-5:** Criterion B, supply lines DC: $0.5\text{ kV}/0.5\text{ kV}$ (symmetrical/asymmetrical), fieldbus cable shield $1\text{ kV}$
  * **Conducted interference EN 61000-4-6 / IEC 61000-4-6:** Criterion A; Test voltage $10\text{ V}$
* **Noise emission test as per EN 61000-6-4:**
  * **EN 55011:** Class A

### Approvals
For the latest approvals, please visit `phoenixcontact.net/products`.

### Mounting Position and Derating (Figure 1)
* **Curve 1 (Mounting on a horizontal DIN rail):** $100\%$ power dissipation $P\ [\%]$ across $0^\circ\text{C}$ to $55^\circ\text{C}$.
* **Curve 2 (Different mounting position):** $100\%$ power dissipation $P\ [\%]$ from $0^\circ\text{C}$ to $50^\circ\text{C}$, derating linearly down to $50\%$ at $55^\circ\text{C}$.

**Operational Results:**
* **When used at $55^\circ\text{C}$ (on horizontal DIN rail):** When mounted on a horizontal DIN rail, you can operate the bus coupler at $55^\circ\text{C}$ and $24\text{ V}$ without any limitation.
* **When used at $55^\circ\text{C}$ (different mounting position):** With a different mounting position, you can operate the bus coupler at $55^\circ\text{C}$ and $24\text{ V}$ with a maximum load of $50\%$.

The specifications refer to a supply voltage of $24\text{ V}$. When you are working with a voltage from the upper voltage range (e.g., $30\text{ V}$), the percentage values increase. In this case, multiply the percentage values with $1.25$ ($30\text{ V} / 24\text{ V} = 1.25$).

The various bus coupler functions have different percentage shares of the power dissipation:

| Function | Percentage shares of power dissipation in % |
| :--- | :--- |
| Inputs | 25 |
| Outputs | 16 |
| $U_{M}$ | 24 |
| $U_{ANA}$ | 3 |
| $U_{L}$ | 32 |

---

## 5. Internal Circuit Diagram (Figure 2)

The internal wiring separates the device into three electrically isolated areas (represented by gray areas in Figure 2):
* **Area A: Ethernet interface** (`2 TX ETH`, Ethernet switch with electrical isolation transformers)
* **Area B: Logic** (Microprocessor $\mu\text{P}$, Protocol chip `IB`, Local bus connection, DC/DC power conversion generating $7.5\text{ V}$ $U_{L}+$ and $24\text{ V}$ $U_{ANA}$ from $U_{BK}$)
* **Area C: I/O** (Optocouplers separating logic from field I/O: $4\times\text{DO}$ with PNP transistors for `DO1...4` supplied by $U_{S}$, and $8\times\text{DI}$ for `DI1...8` supplied by $U_{M}$)

> **Note:** Explanation for other used symbols has been provided in the `IL SYS INST UM E` user manual.

---

## 6. Local Status and Diagnostic Indicators (Figure 3)

The indicators are grouped across four front sections:
* **ETH:** `LNK1` (green), `ACT1` (yellow), `LNK2` (green), `ACT2` (yellow)
* **PWR:** `UL` (green), `US` (green), `UM` (green), `D` (green), `BF` (red), `SF` (red)
* **O1:** `E` (red), `D` (green), Output LEDs `1`, `2`, `3`, `4` (yellow)
* **I1 / I2:** Input LEDs `1`, `2`, `3`, `4` on I1 (yellow) and `5`, `6`, `7`, `8` on I2 (yellow)

| Designation | Color | Meaning | State | Description |
| :--- | :--- | :--- | :--- | :--- |
| **LNK 1/2** | green | Link port 1/2 | ON | Connection via Ethernet to a module via port 1/2 established |
| | | | flashing | PROFINET module identification ("flashing") |
| | | | OFF | No connection established via port 1/2 |
| **ACT 1/2** | yellow | Activity port 1/2 | ON | Transmission or reception of Ethernet telegrams at port 1/2 |
| | | | OFF | No transmission or reception of Ethernet telegrams at port 1/2 |
| **BF** | red | Communication error (Bus Fault) | ON | No link status available |
| | | | flashing | Link status available, no communication connection to the PROFINET controller |
| | | | OFF | A PROFINET controller has established an active communication connection to the PROFINET device. |
| **SF** | red | System failure (PROFINET) | ON | PROFINET diagnostics available |
| | | | OFF | PROFINET diagnostics not available |
| **UL** | green | $U_{Logic}$ | ON | $24\text{ V}$ bus coupler supply/$7.5\text{ V}$ communications power present |
| | | | OFF | $24\text{ V}$ bus coupler supply/$7.5\text{ V}$ communications power not present |
| **US** | green | $U_{Segment}$ | ON | $24\text{ V}$ segment circuit supply present |
| | | | OFF | $24\text{ V}$ segment circuit supply not present |
| **UM** | green | $U_{Main}$ | ON | $24\text{ V}$ main circuit supply/internal communications power present |
| | | | OFF | $24\text{ V}$ main circuit supply/internal communications power not present |
| **D** | green | Diagnostics | ON | Data transmission active within the station |
| | | | flashing | Data transmission not active within the station |
| **E** | red | Error | ON | I/O error, short-circuit/overload of outputs |
| | | | OFF | No I/O error |
| **1 ... 4** | yellow | O1 | ON/OFF | Output is set/not set. |
| **1 ... 8** | yellow | I1, I2 | ON/OFF | Input is set/not set. |

---

## 7. Diagnostic Indicators for PROFINET

### States During Operation
| LED | Meaning |
| :--- | :--- |
| **SF OFF / BF flashing** | PROFINET device is waiting for communication with the PROFINET controller. |
| **SF OFF / BF OFF** | PROFINET controller was able to establish communication without errors. |

### States in the Event of an Error
| LED | Meaning | Measure/remedy in the event of an error |
| :--- | :--- | :--- |
| **SF OFF / BF flashing** | The logic communication connection has been interrupted. The PROFINET controller can no longer be accessed. | Check the connection between the PROFINET controller and the PROFINET device. Make sure that the PROFINET device name of the PROFINET device is identical with the configuration. |
| **SF OFF / BF flashing** | The PROFINET device is not assigned a PROFINET device name. | Assign the PROFINET device name using the relevant tool. |
| **SF OFF / BF ON** | The physical communication path has been interrupted. The PROFINET controller can no longer be accessed. | Restore the physical connection between the PROFINET controller and the PROFINET device. |
| **SF ON / BF OFF** | Diagnostic data is available. | Read the diagnostic message using the relevant tool. |
| **SF flashing / BF flashing** | Hardware watchdog has been triggered. | — |

---

## 8. Connection of PROFINET, Power Supply, Actuators, and Sensors

### 8.1 Connecting PROFINET (Figure 4)
Connect PROFINET to the bus coupler via an 8-pos. RJ45 connector.

Only one twisted pair cable with an impedance of $100\ \Omega$ may be connected to each Ethernet interface in RJ45 format. The data transmission speed is $100\text{ Mbps}$. The 100Base-TX port of the bus coupler is able to detect a pair of incorrectly connected receive cables ($RD+/RD-$) and to correct them using the auto polarity correction function.

#### Pin Assignment of the Ethernet Socket (RJ45)
| Pin | Assignment |
| :--- | :--- |
| **1** | TxD+ (transmit data +) |
| **2** | TxD- (transmit data -) |
| **3** | RxD+ (receive data +) |
| **4** | Reserved |
| **5** | Reserved |
| **6** | RxD- (receive data -) |
| **7** | Reserved |
| **8** | Reserved |

> **Auto crossover:** Both Ethernet interfaces are provided with the auto crossover function.

> **Shielding:** The shielding ground of the connected twisted pair cables is electrically connected with the socket. When connecting network segments, avoid ground loops, potential transfers, and voltage equalization currents via the braided shield.

> **Observe bending radii:** The housing dimensions specified under "Dimensions" refer to the bus coupler with I/O connectors without Ethernet connection. When installing the bus coupler in a control box, observe the bending radii of the Ethernet cables and the connectors used (e.g., `FL CAT5 FLEX`: $30\text{ mm}$ for fixed installation and `FL CAT5 HEAVY`: $30\text{ mm}$ without outer sheath and $45\text{ mm}$ with outer sheath). If required, use angled RJ45 connectors to maintain these bending radii.

### 8.2 Terminal Point Assignment of the Inline Connectors (Figure 5)

#### Terminal Point Assignment of the Power Plug PWR (1)
| Terminal point | Assignment | Terminal point | Assignment |
| :--- | :--- | :--- | :--- |
| **1.1** | $U_{S}$ | **2.1** | $U_{M}$ |
| **1.2** | $U_{BK}$ | **2.2** | $U_{M}$ |
| **1.3** | GND $U_{BK}$ | **2.3** | GND $U_{M}, U_{S}$ |
| **1.4** | Functional earth ground (FE) | **2.4** | Functional earth ground (FE) |

> **NOTE: Malfunction**  
> The module is designed exclusively for SELV operation according to IEC 950/EN 60950/VDE 0805. For information on the power supplies, please refer to the `IL SYS INST UM E` user manual.

> **Note:** If you want to use the same reference potential for communications power and segment voltage, you can bridge the terminal points `1.3` and `2.3` on the connector.

#### Terminal Point Assignment of the Output Plug O1 (2)
| Terminal point | Assignment | Terminal point | Assignment |
| :--- | :--- | :--- | :--- |
| **1.1** | OUT1 | **2.1** | OUT2 |
| **1.2** | GND | **2.2** | GND |
| **1.3** | FE | **2.3** | FE |
| **1.4** | OUT3 | **2.4** | OUT4 |

#### Terminal Point Assignment of the Input Plug I1 (3)
| Terminal point | Assignment | Terminal point | Assignment |
| :--- | :--- | :--- | :--- |
| **1.1** | IN1 | **2.1** | IN2 |
| **1.2** | $U_{M}$ | **2.2** | $U_{M}$ |
| **1.3** | GND | **2.3** | GND |
| **1.4** | IN3 | **2.4** | IN4 |

#### Terminal Point Assignment of the Input Plug I2 (4)
| Terminal point | Assignment | Terminal point | Assignment |
| :--- | :--- | :--- | :--- |
| **3.1** | IN5 | **4.1** | IN6 |
| **3.2** | $U_{M}$ | **4.2** | $U_{M}$ |
| **3.3** | GND | **4.3** | GND |
| **3.4** | IN7 | **4.4** | IN8 |

---

## 9. Connection Example (Figure 6)

Figure 6 demonstrates typical field wiring across the four connectors (`1: PWR`, `2: DO4`, `3: DI4`, `4: DI4`):
* **Power Plug (1):**
  * $24\text{ V DC}$ ($U_{S}$) connected to `1.1` ($+$) and `2.3` ($-$)
  * $24\text{ V DC}$ ($U_{M}$) connected to `2.1` ($+$) and `2.3` ($-$)
  * $24\text{ V DC}$ ($U_{BK}$) connected to `1.2` ($+$) and `1.3` ($-$), with bridge `B` connecting `1.3` and `2.3`
  * Functional earth ground (FE) connected to `1.4`
* **Output Plug (2 - DO4):**
  * Actuator `OUT3` wired between `1.4` (signal) and `1.2` (GND $\perp$)
  * Actuator `OUT2` wired between `2.1` (signal) and `2.2` (GND $\perp$)
* **Input Plug (4 - DI4):**
  * 2-wire sensor `IN6` wired between `4.2` ($+24\text{ V}$) and `4.1` (signal)
  * 3-wire sensor `IN8` wired to `4.2` ($+24\text{ V}$), `4.3` (GND $\perp$), and `4.4` (signal)

---

## 10. Instructions on Using the Bus Coupler in the Potentially Explosive Area

> **WARNING: Explosion hazard**  
> Please make sure that the following notes and instructions are observed.

* **Approval according to ATEX Directive 2014/34/EU:** `II 3 G Ex nA IIC T4 Gc X`
* **Ambient Temperature:**
  * $T_{amb} = -25^\circ\text{C} \dots +55^\circ\text{C}$ (horizontal mounting position)
  * $T_{amb} = -25^\circ\text{C} \dots +55^\circ\text{C}$ (use at $55^\circ\text{C}$ and other mounting position: max. $50\%$ utilization)

### Installation Notes
* The category 3 device is designed for installation in zone 2 potentially explosive areas.
* The device meets the requirements of EN 60079-0:2012 + A11:2013 and EN 60079-15:2010.
* Observe the specified conditions for use in potentially explosive areas! Also observe the requirements of EN 60079-14.
* Install the device in a suitable approved housing (with at least IP54 protection) that meets the requirements of EN 60079-15.
* Connect the DIN rail to the protective earth ground.
* Only devices that are designed for operation in Ex Zone 2 and the conditions at the installation location may be connected to the circuits in Zone 2.
* Only assemble, disassemble as well as connect and disconnect cables when the power is disconnected.
* For safe operation, lockable plug connections must have a functional interlock (e.g., locking clip, screw connection, etc.). Insert the interlock. Repair any damaged connectors immediately.
* Only connect one cable per terminal point.
* Make sure that the supplies of $U_{M}$ and $U_{S}$ at the bus coupler do not exceed $4\text{ A}$.
* When using the device in potentially explosive areas, observe the specifications in the application note `AH DE IL EX ZONE 2` (German) / `AH EN IL EX ZONE 2` (English).

---

## 11. Mapping Inputs and Outputs to PROFINET

The module uses the following input and output data words:

| Slot | Data length |
| :--- | :--- |
| **Slot 0** | — |
| **Slot 1** | 4 words IN / 4 words OUT (local bus master) |
| **Slot 2** | 1 byte OUT (DO4) |
| **Slot 3** | 1 byte IN (DI8) |

---

## 12. Process Data

### 12.1 Terminal Point Assignment of Local Outputs to the OUT Process Data
| Byte | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Bit** | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| **Slot** | Not used | Not used | Not used | Not used | **2 (O1)** | **2 (O1)** | **2 (O1)** | **2 (O1)** |
| **Terminal point (signal)** | — | — | — | — | **2.4** | **1.4** | **2.1** | **1.1** |
| **Terminal point (GND)** | — | — | — | — | **2.2** | **1.2** | **2.2** | **1.2** |
| **Terminal point (FE)** | — | — | — | — | **2.3** | **1.3** | **2.3** | **1.3** |
| **Status indicator, LED** | — | — | — | — | **4** | **3** | **2** | **1** |

### 12.2 Terminal Point Assignment of the Local Inputs to the IN Process Data
| Byte | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Bit** | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| **Slot** | **4 (I2)** | **4 (I2)** | **4 (I2)** | **4 (I2)** | **3 (I1)** | **3 (I1)** | **3 (I1)** | **3 (I1)** |
| **Terminal point (signal)** | **4.4** | **3.4** | **4.1** | **3.1** | **2.4** | **1.4** | **2.1** | **1.1** |
| **Terminal point (GND)** | **4.3** | **3.3** | **4.3** | **3.3** | **2.3** | **1.3** | **2.3** | **1.3** |
| **Terminal point (24 V)** | **4.2** | **3.2** | **4.2** | **3.2** | **2.2** | **1.2** | **2.2** | **1.2** |
| **Status indicator, LED** | **8** | **7** | **6** | **5** | **4** | **3** | **2** | **1** |

---

## 13. Startup

> **Note:** Make sure you always use the latest version of the FDCML/GSDML file and the latest documentation for the bus coupler. The latest files and documentation can be found on the Internet at `phoenixcontact.net/products`.

> **Documentation:** How to assign the PROFINET names and the IP address as well as how to startup a device within a PROFINET system is described in the following documents:
> * "PC WORX" quick start guide
> * "Configuring INTERBUS devices in a PROFINET network using the example of STEP 7" quick start guide
>
> For the order designations, please refer to the ordering data. The documentation can be found on the Internet at `phoenixcontact.net/products`.

### Default Upon Delivery / Default Settings
By default upon delivery, the following functions and features are available:

| Setting | Default Value |
| :--- | :--- |
| **PROFINET name:** | No name assigned |
| **IP parameters:** | none |
| **Module designation:** | `IL PN BK DI8 DO4 2TX` |
| **Vendor ID:** | $00\text{B}0_{\text{hex}}$ |
| **Device ID:** | $000\text{A}_{\text{hex}}$ |

### Reset Button (Figure 7)
The reset button (`RESET`) is on the front of the bus coupler (above `LNK1`/`ACT1` and Ethernet port `X1`).
* The bus coupler is restarted by pressing the reset button.
* The outputs of the Inline station are reset. The process image of the inputs is not re-read.

### Firmware Started
Once you have supplied the bus coupler with power or pressed the reset button, the firmware is started. After completion of the firmware boot process the **BF LED** is either on or flashing.

---

## 14. Parameterization

### PC Worx
Parameterization of the PROFINET devices in PC Worx requires at least **PC Worx version 5.0**. An online data sheet of the device with important technical data and a configuration file are integrated into PC Worx. If several versions of the configuration file are available, make sure that you are working with the file version that corresponds to the firmware/hardware version being used.

### Other Tools
The PROFINET device is parameterized using the configuration tool of the PROFINET controller. Please integrate the corresponding GSDML file of the bus coupler into the relevant software tool (STEP 7/HW Config, ...).

> **Note:** Make sure you always use the latest version of the FDCML/GSDML file and the latest documentation for the bus coupler. The latest files and documentation can be found on the Internet at `phoenixcontact.net/products`.

### Parameter Overview
* **Slot 0: Diagnostic alarms**
  * **PROFINET alarm behavior:**
    * Local bus diagnostics
    * I/O diagnostics
    * Indicate return of local module
  * **Local bus settings:**
    * Automatic start after local bus error
    * Automatic start delay
* **Slot 1:** —
  * **PC Worx:** All registers are mapped to system variables.
  * **Step 7:** There are four words of input data and four words of output data:

| Word | Input data | Output data |
| :--- | :--- | :--- |
| **1** | Diagnostic status register | Standard function start register |
| **2** | Diagnostic parameter register | Standard function parameter register |
| **3** | Extended diagnostic parameter register | Reserved |
| **4** | Standard function status register | Reserved |

### Diagnostic Alarms
PROFINET enables the PROFINET device to store diagnostic information together with the error location and error type.

An incoming alarm informs the PROFINET controller that diagnostic information has been stored. The alarms are only transmitted if they have been enabled via parameters during startup.

When the diagnostic information has been removed, an outgoing alarm is transmitted to the controller.

If at least one piece of diagnostic information is stored, the **SF LED** is on. If no diagnostic information is present, the **SF LED** is off.

### Substitute Value Behavior
In the event of a local bus error or a device error of the bus coupler, all Inline station outputs (including analog outputs) are set to `"0"`.

---

## 15. Firmware Update

The bus coupler firmware is updated using the **"PC Worx Firmware Updater"** software.

> **Note:** For more detailed information regarding the firmware update, refer to the "Installation and operation of the PC Worx Firmware Updater software" user manual.

---

## 16. Physical Device - PDev

The module supports all devices of the PDev according to PROFINET.

PDev is a standardized description in PROFINET of the Ethernet interfaces and their features. This includes, for example, the IP and MAC address, diagnostic and neighborhood information, and parameterization settings.

---

## 17. Link Layer Discovery Protocol - LLDP

The device supports LLDP according to IEEE 802.1AB and thus enables topology detection of devices that also have LLDP activated.

### Advantages of Using LLDP
* Improved error location detection
* Improved device replacement
* More efficient network configuration

### Information Exchanged
The following information is received by or sent to neighbors, as long as LLDP is activated:
* The device sends its own management and connection information to neighboring devices.
* The device receives management and connection information from neighboring devices.

### Displaying LLDP Information
Engineering tools can be used to represent the LLDP information as a topology overview.

> **Note:** For additional information on LLDP, please refer to the `FL SWITCH MM HS UM E` user manual.

---

## 18. Device Replacement

Devices can be replaced without having to reconfigure them within the PROFINET network. The station name and address are assigned by the control system to the newly added PROFINET bus coupler using the neighborhood detection function.

> **Note:** Device replacement is possible for Phoenix Contact PROFINET controllers from firmware version 3.0 onwards.

---

## 19. Applicative System Redundancy for Process Data

> **Note:** Applicative system redundancy is only provided for process data but not for parameter data.

Acyclic communication allows two PROFINET controllers (primary and backup) to communicate with the same bus coupler.

Parallel PCP services are not supported. This means, if a second PROFINET controller tries to access a PCP device while there is another PROFINET controller with a service pending, the second service request is rejected by the bus coupler.

With regard to communication, no distinction is made between the "primary" (process controlling) and the "backup" controller.

---

## 20. Failsafe Behavior

In the event of a network failure, previously determined I/O values are output.

If PROFINET communication fails, all output process data is set to zero. The local bus continues to run using these values.

> **Note:** Substitute values are not parameterized.

---

## 21. Acyclic PROFINET Communication

The bus coupler enables acyclic access to intelligent local bus devices (PCP devices) using PROFINET (Record Read function block, Record Write function block).

---

## 22. Mailbox Communication

The bus coupler supports acyclic mailbox communication. This means specific PLC blocks allow acyclic transmission of firmware services (e.g., Read-Value, PCP) from the control system to the PROFINET device or PCP device with the Record Read and Record Write PROFINET services.

> **Note:** Additional PCP information can be found in the `IBS SYS PCP G4 UM E` user manual.

---

## 23. Byte Rotation for 16 and 32-Channel Inline Terminals with a SIMATIC® S7 Controller

To adapt the data format of the 16 and 32-channel Inline terminals to the data format of a SIMATIC S7 controller, you can rotate the I/O data arrangement with device parameters. This adaptation can only be made once and is then valid for all DI16/DO16 and all DI32/DO32 terminals.

### 23.1 Byte Rotation for `IB IL 24 DI 16...` and `IB IL 24 DO 16...` Terminals

#### Default (Word 0)
| Word.bit | **15** | **14** | **13** | **12** | **11** | **10** | **9** | **8** | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Byte.Bit** | **0.7** | **0.6** | **0.5** | **0.4** | **0.3** | **0.2** | **0.1** | **0.0** | **1.7** | **1.6** | **1.5** | **1.4** | **1.3** | **1.2** | **1.1** | **1.0** |
| **Slot** | **4** | **4** | **4** | **4** | **3** | **3** | **3** | **3** | **2** | **2** | **2** | **2** | **1** | **1** | **1** | **1** |
| **Terminal point** | **8.4** | **7.4** | **8.1** | **7.1** | **6.4** | **5.4** | **6.1** | **5.1** | **4.4** | **3.4** | **4.1** | **3.1** | **2.4** | **1.4** | **2.1** | **1.1** |

#### Rotated (Word 0)
| Word.bit | **15** | **14** | **13** | **12** | **11** | **10** | **9** | **8** | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Byte.Bit** | **0.7** | **0.6** | **0.5** | **0.4** | **0.3** | **0.2** | **0.1** | **0.0** | **1.7** | **1.6** | **1.5** | **1.4** | **1.3** | **1.2** | **1.1** | **1.0** |
| **Slot** | **2** | **2** | **2** | **2** | **1** | **1** | **1** | **1** | **4** | **4** | **4** | **4** | **3** | **3** | **3** | **3** |
| **Terminal point** | **4.4** | **3.4** | **4.1** | **3.1** | **2.4** | **1.4** | **2.1** | **1.1** | **8.4** | **7.4** | **8.1** | **7.1** | **6.4** | **5.4** | **6.1** | **5.1** |

---

### 23.2 Byte Rotation for `IB IL 24 DI 32...` and `IB IL 24 DO 32...` Terminals

#### Default — Word 0 (Bytes 0 & 1)
| Word.bit | **15** | **14** | **13** | **12** | **11** | **10** | **9** | **8** | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Byte.Bit** | **0.7** | **0.6** | **0.5** | **0.4** | **0.3** | **0.2** | **0.1** | **0.0** | **1.7** | **1.6** | **1.5** | **1.4** | **1.3** | **1.2** | **1.1** | **1.0** |
| **Slot** | **4** | **4** | **4** | **4** | **4** | **4** | **4** | **4** | **3** | **3** | **3** | **3** | **3** | **3** | **3** | **3** |
| **Terminal point** | **8.4** | **7.4** | **8.3** | **7.3** | **8.2** | **7.2** | **8.1** | **7.1** | **6.4** | **5.4** | **6.3** | **5.3** | **6.2** | **5.2** | **6.1** | **5.1** |

#### Default — Word 1 (Bytes 2 & 3)
| Word.bit | **15** | **14** | **13** | **12** | **11** | **10** | **9** | **8** | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Byte.Bit** | **2.7** | **2.6** | **2.5** | **2.4** | **2.3** | **2.2** | **2.1** | **2.0** | **3.7** | **3.6** | **3.5** | **3.4** | **3.3** | **3.2** | **3.1** | **3.0** |
| **Slot** | **2** | **2** | **2** | **2** | **2** | **2** | **2** | **2** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** |
| **Terminal point** | **4.4** | **3.4** | **4.3** | **3.3** | **4.2** | **3.2** | **4.1** | **3.1** | **2.4** | **1.4** | **2.3** | **1.3** | **2.2** | **1.2** | **2.1** | **1.1** |

#### Rotated — Word 0 (Bytes 0 & 1)
| Word.bit | **15** | **14** | **13** | **12** | **11** | **10** | **9** | **8** | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Byte.Bit** | **0.7** | **0.6** | **0.5** | **0.4** | **0.3** | **0.2** | **0.1** | **0.0** | **1.7** | **1.6** | **1.5** | **1.4** | **1.3** | **1.2** | **1.1** | **1.0** |
| **Slot** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **2** | **2** | **2** | **2** | **2** | **2** | **2** | **2** |
| **Terminal point** | **2.4** | **1.4** | **2.3** | **1.3** | **2.2** | **1.2** | **2.1** | **1.1** | **4.4** | **3.4** | **4.3** | **3.3** | **4.2** | **3.2** | **4.1** | **3.1** |

#### Rotated — Word 1 (Bytes 2 & 3)
| Word.bit | **15** | **14** | **13** | **12** | **11** | **10** | **9** | **8** | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Byte.Bit** | **2.7** | **2.6** | **2.5** | **2.4** | **2.3** | **2.2** | **2.1** | **2.0** | **3.7** | **3.6** | **3.5** | **3.4** | **3.3** | **3.2** | **3.1** | **3.0** |
| **Slot** | **3** | **3** | **3** | **3** | **3** | **3** | **3** | **3** | **4** | **4** | **4** | **4** | **4** | **4** | **4** | **4** |
| **Terminal point** | **6.4** | **5.4** | **6.3** | **5.3** | **6.2** | **5.2** | **6.1** | **5.1** | **8.4** | **7.4** | **8.3** | **7.3** | **8.2** | **7.2** | **8.1** | **7.1** |

---

**Manufacturer Address:**  
PHOENIX CONTACT GmbH & Co. KG  
32823 Blomberg, Germany  
`phoenixcontact.com`