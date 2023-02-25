import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

def dopasuj():
    plik_dane = 'cw2.txt'
    funkcja = lambda x, A, B: A / x - B * math.pow(x,-1/3)
    funkcja_mapujaca = np.vectorize(funkcja)
    dane = np.loadtxt(plik_dane, delimiter=',', skiprows = 0)
    obj = dane[:,0]
    cisn_wewn = dane[:, 1]
    cisn_zewn = dane[:, 2]
    plt.figure(figsize=(8, 6))
    plt.plot(obj, cisn_wewn, 'o', label='Cisnienie wewnetrzne = f(V)')
    plt.plot(obj, cisn_zewn, 'x', label='Cisnienie zewnetrzne= f(V)')
    parametry1, macierz_kowar_1 = curve_fit(funkcja_mapujaca, obj, cisn_wewn, p0=[1,1])
    parametry2, macierz_kowar_2 = curve_fit(funkcja_mapujaca, obj, cisn_zewn, p0=[1,1])
    print(parametry1)
    print(tuple(parametry1))

    plt.plot(obj, funkcja_mapujaca(obj, *parametry1), 'b',
    label='dopasowanie p$_{wewn}$: A = %5.3f, B = %5.3f' % tuple(parametry1))
    plt.plot(obj, funkcja_mapujaca(obj, *parametry2), 'r',
    label='dopasowanie p$_{zewn}$: A = %5.3f, B = %5.3f' % tuple(parametry2))
    plt.xlabel('Objętość (V)')
    plt.ylabel('ciśnienie (p)')
    plt.legend()
    plt.show()
    
dopasuj()


