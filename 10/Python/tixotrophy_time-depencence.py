import _data_read as dr
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def time_depedence(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   Xdata=t
   Ydata=eta
   func1 = lambda x,A,B: A*np.exp(-B*x)
   func=np.vectorize(func1)
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='zaleznosc od czasu' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1000,0.1])
   plt.plot( Xdata, func(Xdata,*popt), 'b',
             label='dopasowanie: A = %5.3e, B = %5.3e ' % tuple( popt ) )
   plt.xlabel('t')
   plt.ylabel('eta')
   plt.legend()
   plt.show()

time_depedence("wyniki.xls")
