from scipy import optimize
import numpy as np
import math


def kat_teta(Obj, promien_krzywizny):
   c = 2 - 3 * Obj / math.pi / math.pow(promien_krzywizny, 3)
   funkcja_optym = lambda x: math.pow(x,3) - 3 * x + c
   pochodna_funkcji = lambda x: 3*math.pow(x,2) - 3
   cosTeta = optimize.newton(funkcja_optym, 0.001, pochodna_funkcji, (), 1e-10, 200)
   if abs(cosTeta)>1:
      wynik = 'liczba zespolona'
   else:
      wynik = str(math.acos(cosTeta)*180/math.pi)
   return wynik

def rozwiaz():
   plik = open('wyniki_koncowe.txt','w' )
   linia = „{:7.4f}, {:7.4f}, {:7.4f}, {:7.4f}, {:7.4f} >> {:8s}, {:8s} \n"
   dane = np.loadtxt('cw1.txt', delimiter = ',', skiprows = 0)
   liczba_linii = len(dane)
   for i in range(0, liczba_linii):
      Ciecz = dane[i,0]
      C_stale = dane[i,1]
      Ciecz_C_stale = dane[i,2]
      promien_krzywizny = dane[i,3]
      Obj = dane[i,4]
      cosTeta = (C_stale - Ciecz_C_stale) / Ciecz
      if abs(cosTeta)>1:
         wynik = 'liczba zespolona'
      else:
         wynik = str(math.acos(cosTeta)*180/math.pi)
      Teta = wynik
      Teta2 = kat_teta(Obj,promien_krzywizny)
      print(Ciecz, C_stale, Ciecz_C_stale, promien_krzywizny, Obj, Teta, Teta2)
      plik.write(linia.format(Ciecz, C_stale, Ciecz_C_stale, promien_krzywizny, Obj, Teta, Teta2))
   plik.close()

rozwiaz()