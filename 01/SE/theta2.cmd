function real theta2()
{SumTheta:=0;ii:=0;
  {foreach edge ee where ee.valence==3 do
     {foreach ee.facet ff1 where not on_constraint 1 do
        {Cos1:=ff1.z/ff1.area;
           ff1.color:=blue;};
           alpha1:=acos(Cos1);
           alpha2:=0;
   foreach ee.facet ff2 where on_constraint 1 do
        {Cos2:=ff2.z/ff2.area;
           alpha2:=alpha2+acos(Cos2);
           ff2.color:=red;};
           SumTheta:=SumTheta+(alpha1-alpha2/2+pi/2);ii++;};};
return SumTheta/ii*180/pi;};
print theta2();


