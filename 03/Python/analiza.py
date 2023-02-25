import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def dopasuj():
   plik_dane = 'wyniki_Weaire_Phelan.txt'
   rzad = 2/3;
   dane = np.loadtxt(plik_dane, delimiter=',', skiprows = 0)
   liczba_wierszy = len(dane)
   dane_x = dane[:,0]
   dane_y = dane[:, 1]
   plt.figure(num=None, figsize=(8,6), dpi=80, facecolor='w', edgecolor='k')
   plt.plot(dane_x, dane_y, 'o', label='')
   rzad0_nachyl, rzad0_WyrWol, r_rzad0, p_rzad0, OdchStd0 = stats.linregress(dane_x, dane_y)
   rzad1_nachyl, rzad1_WyrWol, r_rzad1, p_rzad1, OdchStd1 = stats.linregress(dane_x, np.log(dane_y))
   razd2_nachyl, rzad2_WyrWol, r_rzad2, p_rzad2, OdchStd2 = stats.linregress(dane_x, 1/dane_y)
   rzadX_nachyl, rzadX_WyrWol, r_rzadX, p_rzadX, OdchStdX = stats.linregress(dane_x, dane_y**rzad)
   Y_rzad0 = rzad0_nachyl * dane_x + rzad0_WyrWol
   Y_rzad1 = np.exp(rzad1_nachyl * dane_x + rzad1_WyrWol)
   Y_rzad2 = 1 / (razd2_nachyl * dane_x + rzad2_WyrWol)
   Y_rzadX = (rzadX_nachyl * dane_x + rzadX_WyrWol) ** (1 / rzad)
   # odchylenie standardowe ##############################
   suma_OdchStd0 = 0
   suma_OdchStd1 = 0
   suma_OdchStd2 = 0
   suma_OdchStdX = 0
   for i in range(liczba_wierszy):
      suma_OdchStd0 += np.sqrt((Y_rzad0[i] - dane_y[i]) ** 2)
      suma_OdchStd1 += np.sqrt((Y_rzad1[i] - dane_y[i]) ** 2)
      suma_OdchStd2 += np.sqrt((Y_rzad2[i] - dane_y[i]) ** 2)
      suma_OdchStdX += np.sqrt((Y_rzadX[i] - dane_y[i]) ** 2)
   srednie_OdchStd0 = suma_OdchStd0 / liczba_wierszy
   srednie_OdchStd1 = suma_OdchStd1 / liczba_wierszy
   srednie_OdchStd2 = suma_OdchStd2 / liczba_wierszy
   srednie_OdchStdX = suma_OdchStdX / liczba_wierszy
   #######################################################
   plt.plot( dane_x,Y_rzad0, 'r', label='rzad 0, k=' + str("{:.4f}".format(rzad0_nachyl))+', odch_stand= '+str("{:.5e}".format(srednie_OdchStd0)))
   plt.plot( dane_x,Y_rzad1, 'b', label='rzad I, k=' + str("{:.4f}".format(-rzad1_nachyl))+', odch_stand= '+str("{:.5e}".format(srednie_OdchStd1)))
   plt.plot( dane_x,Y_rzad2, 'g', label='rzad II, k=' + str("{:.4f}".format(razd2_nachyl))+', odch_stand= '+str("{:.5e}".format(srednie_OdchStd2)))
   plt.plot(dane_x, Y_rzadX, 'm', label='rzad ' + str("{:.3f}".format(rzad)) + ', k=' + str("{:.4f}".format(-rzadX_nachyl)) + ', odch_stand= ' + str("{:.3e}".format(srednie_OdchStdX)))
   plt.xlabel('t')
   plt.ylabel('V')
   plt.legend()
   plt.show()

dopasuj()