import _data_read as dr
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Meter(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   func1 = lambda x,eta0,etainf,ro2,alpha: etainf+(eta0-etainf)/np.power(1+x/ro2,alpha-1)
   func=np.vectorize(func1)
   Xdata=tau
   Ydata=eta
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='rownanie Metera' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[10,1000,10,10])
   print('Standardowe odchylenie dopasowania fit (eta) = ',dr.stdev(Xdata,Ydata,func,popt))
   plt.plot( Xdata, func(Xdata,*popt), 'b',
             label='dopasowanie: eta0 = %5.3e, etainf = %5.3e ro = %5.3e alpha = %5.3e' % tuple( popt ) )
   plt.xlabel('tau')
   plt.ylabel('eta')
   plt.legend()
   plt.show()

Meter("wyniki.xls")
