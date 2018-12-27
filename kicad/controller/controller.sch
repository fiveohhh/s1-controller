EESchema Schematic File Version 4
LIBS:controller-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Isolator:PC817 ON_OFF1
U 1 1 5C11284B
P 3000 2350
F 0 "ON_OFF1" H 3000 2675 50  0000 C CNN
F 1 "PC817" H 3000 2584 50  0000 C CNN
F 2 "Package_DIP:DIP-4_W7.62mm" H 2800 2150 50  0001 L CIN
F 3 "http://www.soselectronic.cz/a_info/resource/d/pc817.pdf" H 3000 2350 50  0001 L CNN
	1    3000 2350
	-1   0    0    -1  
$EndComp
$Comp
L Isolator:PC817 ON_STB_LED1
U 1 1 5C11288D
P 3100 3150
F 0 "ON_STB_LED1" H 3100 3475 50  0000 C CNN
F 1 "PC817" H 3100 3384 50  0000 C CNN
F 2 "Package_DIP:DIP-4_W7.62mm" H 2900 2950 50  0001 L CIN
F 3 "http://www.soselectronic.cz/a_info/resource/d/pc817.pdf" H 3100 3150 50  0001 L CNN
	1    3100 3150
	1    0    0    -1  
$EndComp
$Comp
L Isolator:PC817 BOIL_LED1
U 1 1 5C1128D5
P 3050 4000
F 0 "BOIL_LED1" H 3050 4325 50  0000 C CNN
F 1 "PC817" H 3050 4234 50  0000 C CNN
F 2 "Package_DIP:DIP-4_W7.62mm" H 2850 3800 50  0001 L CIN
F 3 "http://www.soselectronic.cz/a_info/resource/d/pc817.pdf" H 3050 4000 50  0001 L CNN
	1    3050 4000
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x08 J1
U 1 1 5C112B1E
P 1450 2600
F 0 "J1" H 1370 3117 50  0000 C CNN
F 1 "Screw_Terminal_01x08" H 1370 3026 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x08_P2.54mm_Vertical" H 1450 2600 50  0001 C CNN
F 3 "~" H 1450 2600 50  0001 C CNN
	1    1450 2600
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR0101
U 1 1 5C112BD5
P 4100 1800
F 0 "#PWR0101" H 4100 1550 50  0001 C CNN
F 1 "GND" H 4105 1627 50  0000 C CNN
F 2 "" H 4100 1800 50  0001 C CNN
F 3 "" H 4100 1800 50  0001 C CNN
	1    4100 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 1800 3750 1800
Wire Wire Line
	3300 2450 3750 2450
Wire Wire Line
	3750 2450 3750 1800
Connection ~ 3750 1800
Wire Wire Line
	3750 1800 4100 1800
$Comp
L Connector:Raspberry_Pi_2_3 J2
U 1 1 5C112CE3
P 5950 3150
F 0 "J2" H 5950 4628 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 5950 4537 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical" H 5950 3150 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 5950 3150 50  0001 C CNN
	1    5950 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 1600 2400 1600
Wire Wire Line
	3300 2250 4250 2250
Wire Wire Line
	4250 2250 4250 2450
$Comp
L Isolator:PC817 BOIL1
U 1 1 5C11279A
P 3050 1700
F 0 "BOIL1" H 3050 2025 50  0000 C CNN
F 1 "PC817" H 3050 1934 50  0000 C CNN
F 2 "Package_DIP:DIP-4_W7.62mm" H 2850 1500 50  0001 L CIN
F 3 "http://www.soselectronic.cz/a_info/resource/d/pc817.pdf" H 3050 1700 50  0001 L CNN
	1    3050 1700
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3350 1600 4600 1600
Wire Wire Line
	4600 1600 4600 1500
Wire Wire Line
	4900 1500 7000 1500
Wire Wire Line
	7000 1500 7000 3050
$Comp
L Device:R_US R3
U 1 1 5C11973B
P 2050 3150
F 0 "R3" H 2118 3196 50  0000 L CNN
F 1 "R_US" H 2118 3105 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 2090 3140 50  0001 C CNN
F 3 "~" H 2050 3150 50  0001 C CNN
	1    2050 3150
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R1
U 1 1 5C119795
P 1800 3450
F 0 "R1" H 1868 3496 50  0000 L CNN
F 1 "R_US" H 1868 3405 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 1840 3440 50  0001 C CNN
F 3 "~" H 1800 3450 50  0001 C CNN
	1    1800 3450
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R5
U 1 1 5C1197ED
P 4250 2600
F 0 "R5" H 4318 2646 50  0000 L CNN
F 1 "R_US" H 4318 2555 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" V 4290 2590 50  0001 C CNN
F 3 "~" H 4250 2600 50  0001 C CNN
	1    4250 2600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R6
U 1 1 5C11984D
P 4750 1500
F 0 "R6" V 4545 1500 50  0000 C CNN
F 1 "R_US" V 4636 1500 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 4790 1490 50  0001 C CNN
F 3 "~" H 4750 1500 50  0001 C CNN
	1    4750 1500
	0    1    1    0   
$EndComp
Wire Wire Line
	2050 3300 2800 3300
Wire Wire Line
	2800 3300 2800 3250
Wire Wire Line
	1800 2800 1800 3300
Wire Wire Line
	1650 2800 1800 2800
Wire Wire Line
	1800 3600 1800 4100
Wire Wire Line
	1800 4100 2750 4100
Wire Wire Line
	3750 2450 3750 3250
Wire Wire Line
	3750 3250 3400 3250
Connection ~ 3750 2450
Wire Wire Line
	3750 3250 3750 3300
Wire Wire Line
	3750 4100 3350 4100
Connection ~ 3750 3250
Connection ~ 3750 4100
Wire Wire Line
	5150 2650 4800 2650
Wire Wire Line
	4800 2650 4800 3000
Wire Wire Line
	4800 3000 4000 3000
Wire Wire Line
	3400 3000 3400 3050
Wire Wire Line
	5150 3850 4000 3850
Wire Wire Line
	3350 3850 3350 3900
Wire Wire Line
	6750 3050 7000 3050
Wire Wire Line
	4250 3750 5150 3750
Wire Wire Line
	4250 2750 4250 3750
Wire Wire Line
	2050 2900 2050 3000
Wire Wire Line
	1650 2900 2050 2900
Wire Wire Line
	2700 2450 2550 2450
Wire Wire Line
	2350 2700 1650 2700
Wire Wire Line
	2350 2700 2350 3050
Wire Wire Line
	5950 4450 5950 5000
Wire Wire Line
	5650 4450 5650 5000
Connection ~ 5650 5000
Wire Wire Line
	3750 5000 5650 5000
Wire Wire Line
	5650 5000 5950 5000
Wire Wire Line
	1650 2500 2150 2500
Wire Wire Line
	2150 2500 2150 1800
Wire Wire Line
	2150 1800 2750 1800
Wire Wire Line
	3750 4100 3750 4150
Wire Wire Line
	2550 2300 1650 2300
Wire Wire Line
	2550 2300 2550 2450
Wire Wire Line
	1650 2400 2000 2400
Wire Wire Line
	2000 2400 2000 2250
Wire Wire Line
	2000 2250 2700 2250
$Comp
L Device:C C1
U 1 1 5C25DA5E
P 4000 3150
F 0 "C1" H 4115 3196 50  0000 L CNN
F 1 "C" H 4115 3105 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 4038 3000 50  0001 C CNN
F 3 "~" H 4000 3150 50  0001 C CNN
	1    4000 3150
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 5C25DAD0
P 4000 4000
F 0 "C2" H 4115 4046 50  0000 L CNN
F 1 "C" H 4115 3955 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 4038 3850 50  0001 C CNN
F 3 "~" H 4000 4000 50  0001 C CNN
	1    4000 4000
	1    0    0    -1  
$EndComp
Connection ~ 4000 3850
Wire Wire Line
	4000 3850 3350 3850
Wire Wire Line
	4000 4150 3750 4150
Connection ~ 3750 4150
Wire Wire Line
	3750 4150 3750 5000
Connection ~ 4000 3000
Wire Wire Line
	4000 3000 3400 3000
Wire Wire Line
	4000 3300 3750 3300
Connection ~ 3750 3300
Wire Wire Line
	3750 3300 3750 4100
Wire Wire Line
	2350 3900 2750 3900
Wire Wire Line
	2800 3050 2350 3050
Connection ~ 2350 3050
Wire Wire Line
	2350 3050 2350 3900
Wire Wire Line
	1650 2600 2400 2600
Wire Wire Line
	2400 1600 2400 2600
$EndSCHEMATC
