# fischertechnik® — Taktstraße mit 2 Bearbeitungsstationen 24V / Indexed line with 2 machining stations 24V
**Art.-Nr. / Item-No.:** 96790

---

## 1. Component Overview & Sensor/Actuator Mapping (Page 1)

The diagram on Page 1 illustrates the physical layout of the indexed line with 2 machining stations (milling and drilling) and indicates the locations of the following inputs (`I`) and outputs (`Q`):

* **Sliders (Schieber):**
  * `Q1/Q2`: Motor Slider 1 (backward / forward)
  * `I1`: Push-button Slider 1 front
  * `I2`: Push-button Slider 1 rear
  * `Q3/Q4`: Motor Slider 2 (backward / forward)
  * `I3`: Push-button Slider 2 front
  * `I4`: Push-button Slider 2 rear
* **Conveyors & Light Barriers (Bänder & Fototransistoren):**
  * `Q5`: Motor conveyor belt feed
  * `I5`: Phototransistor slider 1
  * `I7`: Phototransistor loading station
  * `Q6`: Motor conveyor belt milling machine
  * `I6`: Phototransistor milling machine
  * `Q8`: Motor conveyor belt drilling machine
  * `I8`: Phototransistor drilling machine
  * `Q10`: Motor conveyor belt swap (exit)
  * `I9`: Phototransistor conveyor belt swap
* **Machining Units (Bearbeitungsstationen):**
  * `Q7`: Motor milling machine
  * `Q9`: Motor drilling machine

---

## 2. Circuit Layout / Belegungsplan (Pages 2–3)

**Belegungsplan für Taktstraße mit 2 Bearbeitungsmaschinen 24V (Art.-Nr. 96790)**  
**Circuit layout for Indexed line with 2 machining stations 24V (item-no. 96790)**

| Klemme Nr. / Terminal no. | Funktion / Function (DE / EN) | Eingang/Ausgang / Input/Output |
| :--- | :--- | :--- |
| **1** | Stromversorgung (+) Aktoren / power supply (+) actuators | 24V DC |
| **2** | Stromversorgung (+) Sensoren / power supply (+) sensors | 24V DC |
| **3** | Stromversorgung (-) / power supply (-) | 0V |
| **4** | Stromversorgung (-) / power supply (-) | 0V |
| **5** | Taster Schieber 1 vorne / Push-button slider 1 front | I1 |
| **6** | Taster Schieber 1 hinten / Push-button slider 1 rear | I2 |
| **7** | Taster Schieber 2 vorne / Push-button slider 2 front | I3 |
| **8** | Taster Schieber 2 hinten / Push-button slider 2 rear | I4 |
| **9** | Fototransistor Schieber 1 / Phototransistor slider 1 | I5 |
| **10** | Fototransistor Fräsmaschine / Phototransistor milling machine | I6 |
| **11** | Fototransistor Einlegestation / Phototransistor loading station | I7 |
| **12** | Fototransistor Bohrmaschine / Phototransistor drilling machine | I8 |
| **13** | Fototransistor Auslagerband / Phototransistor conveyor belt swap | I9 |
| **14** | *(Unassigned / Reserve)* | *(Empty)* |
| **15** | Motor Schieber 1 zurück / motor slider 1 backward | Q1 |
| **16** | Motor Schieber 1 vor / motor slider 1 forward | Q2 |
| **17** | Motor Schieber 2 zurück / motor slider 2 backward | Q3 |
| **18** | Motor Schieber 2 vor / motor slider 2 forward | Q4 |
| **19** | Motor Zuführband / motor conveyor belt feed | Q5 |
| **20** | Motor Band Fräsmaschine / motor conveyor belt milling machine | Q6 |
| **21** | Motor Fräser / motor milling machine | Q7 |
| **22** | Motor Band Bohrmaschine / motor conveyor belt drilling machine | Q8 |
| **23** | Motor Bohrmaschine / motor drilling machine | Q9 |
| **24** | Motor Band Ausgang / motor conveyor belt swap | Q10 |

---

## 3. 26-Pin Connector Header / 26pol. Steckerleiste (Page 3)

Physical pinout layout of the 26-pin ribbon cable header (`26pol. Steckerleiste`):

| Left Column Signal | Left Pin | Right Pin | Right Column Signal |
| :--- | :---: | :---: | :--- |
| **+24V (Aktoren / actuators)** | **1** | **2** | **+24V (Sensoren / sensors)** |
| **0V (GND)** | **3** | **4** | **0V (GND)** |
| **I1** | **5** | **6** | **I2** |
| **I3** | **7** | **8** | **I4** |
| **I5** | **9** | **10** | **I6** |
| **I7** | **11** | **12** | **I8** |
| **I9** | **13** | **14** | *(Not connected)* |
| **Q1** | **15** | **16** | **Q2** |
| **Q3** | **17** | **18** | **Q4** |
| **Q5** | **19** | **20** | **Q6** |
| **Q7** | **21** | **22** | **Q8** |
| **Q9** | **23** | **24** | **Q10** |
| **GND** | **25** | **26** | **GND** |