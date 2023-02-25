import _data_read as dr
import numpy as np
import math as math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Powell_Eyring(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   func1 = lambda x,eta0,etainf,tau0: etainf+(eta0-etainf)*math.asinh(tau0*x)/(tau0*x)
   func=np.vectorize(func1)
   Xdata=gamma
   Ydata=eta
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='rownanie Powella-Eyringa' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1,1,1])
   print('Standardowe odchylenie dopasowania fit (eta) = ',dr.stdev(Xdata,Ydata,func,popt))
   plt.plot( Xdata, func(Xdata,*popt), 'b',
             label='dopasowanie: eta0 = %5.3e, etainf = %5.3e tau0 = %5.3e' % tuple( popt ) )
   plt.xlabel('gamma')
   plt.ylabel('eta')
   plt.legend()
   plt.show()

Powell_Eyring("wyniki.xls")
