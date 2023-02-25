#Lakatos I., Lakatos-Szabo J.,
#Acta Chim. Hung., 118, 147 (1985)

import _data_read as dr
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Careau(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   func1 = lambda x,eta0,gammaP1,n: eta0/np.power(1+np.power(x/gammaP1,2),n)
   func=np.vectorize(func1)
   Xdata=gamma
   Ydata=eta
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='rownanie Carreau' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1000,0.01,1])
   print('Standardowe odchylenie dopasowania fit (eta) = ',dr.stdev(Xdata,Ydata,func,popt))
   plt.plot( Xdata, func(Xdata,*popt), 'b',
             label='dopasowanie: eta0 = %5.3e, gammaP1 = %5.3e n = %5.3e' % tuple( popt ))
   plt.xlabel('gamma')
   plt.ylabel('eta')
   plt.legend()
   plt.show()

Careau("wyniki.xls")
