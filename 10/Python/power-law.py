import _data_read as dr
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def power_law(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   func1 = lambda x,kappa,n: kappa*np.power(x,n-1)
   func=np.vectorize(func1)
   Xdata=gamma
   Ydata=eta
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='rownanie potegowe' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1,1])
   print('Standardowe odchylenie dopasowania fit (eta) = ',dr.stdev(Xdata,Ydata,func,popt))
   plt.plot( Xdata, func(Xdata,*popt), 'b',
             label='dopasowanie: kappa = %5.3e, n = %5.3e' % tuple( popt ) )
   plt.xlabel('gamma')
   plt.ylabel('eta')
   plt.legend()
   plt.show()

power_law("wyniki.xls")
