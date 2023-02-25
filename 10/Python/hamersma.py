#Hamersma P.J., Ellenberg J., Fortuin Y.M.H., 
#Rheol. Acta, 20, 270 (1981)

import _data_read as dr
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Hamersma(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   func1 = lambda x,etainf,tau2,H: etainf/(1-tau2/x*(1-np.exp(-H*x)))
   func=np.vectorize(func1)
   Xdata=tau
   Ydata=eta
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='rownanie Hamersmy' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1,10,1])
   print('Standardowe odchylenie dopasowania fit (eta) = ',dr.stdev(Xdata,Ydata,func,popt))
   plt.plot( Xdata, func(Xdata,*popt), 'b',
             label='dopasowanie: etaint = %5.3e, tau2 = %5.3e H = %5.3e' % tuple( popt ) )
   plt.xlabel('tau')
   plt.ylabel('eta')
   plt.legend()
   plt.show()

Hamersma("wyniki.xls")
