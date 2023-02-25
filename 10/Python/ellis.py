import _data_read as dr
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Ellis(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   func1 = lambda x,eta0,ro2,alpha: eta0/np.power(1+x/ro2,alpha-1)
   func=np.vectorize(func1)
   Xdata=gamma
   Ydata=eta
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='rownanie Ellisa' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1,1,1])
   print('Standardowe odchylenie dopasowania fit (eta) = ',dr.stdev(Xdata,Ydata,func,popt))
   plt.plot( Xdata, func(Xdata,*popt), 'b',
             label='dopasowanie: eta0 = %5.3e, ro2 = %5.3e alpha = %5.3e' % tuple( popt ) )
   plt.xlabel('tau')
   plt.ylabel('eta')
   plt.legend()
   plt.show()

Ellis("wyniki.xls")
