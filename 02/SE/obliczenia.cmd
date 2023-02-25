recalc;
wyniki:="cw2.txt"
objetosc2:=0;
foreach bodies vv do objetosc2:=objetosc2+vv.volume;
objetosc2:= objetosc2/body_count;
cisnienie2:=0;
foreach bodies vv do cisnienie2:= cisnienie2+vv.pressure;
cisnienie2:= cisnienie2/body_count;
powierzchnia2:=0;
foreach face vv do powierzchnia2:= powierzchnia2+vv.area;
powierzchnia2:= powierzchnia2/body_count;
energiaV2:= cisnienie2*objetosc2*log(1/abs(objetosc2));
energiaS2:=0;
foreach face vv do energiaS2:=energiaS2+vv.area*vv.tension;  
energiaS2:=energiaS2/body_count;
energiaT2:=energiaS2+energiaV2;
printf "%e, %e, %e, %e, %e, %e, %e\n",objetosc2,cisnienie2,ambient_pressure_value,powierzchnia2,energiaS2,energiaV2,energiaT2 >> wyniki
 