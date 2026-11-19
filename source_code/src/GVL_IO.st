VAR_GLOBAL
    byBK_In  : BYTE;   // coupler inputs  IN1..IN8   (bit0 = IN1 ... bit7 = IN8)
    byBK_Out : BYTE;   // coupler outputs OUT1..OUT4 (bit0 = OUT1 ... bit3 = OUT4)
    byDI16_0 : BYTE;   // DI16 module, first byte
    byDI16_1 : BYTE;   // DI16 module, second byte
    byDO16_0 : BYTE;   // DO16 module, first byte
    byDO16_1 : BYTE;   // DO16 module, second byte
	xI1_S1Front, xI2_S1Rear, xI3_S2Front, xI4_S2Rear : BOOL;
	xI5_LbSlider1, xI6_LbMill, xI7_LbLoad, xI8_LbDrill : BOOL;
	xQ1_S1Back, xQ2_S1Fwd, xQ3_S2Back, xQ4_S2Fwd : BOOL;
END_VAR