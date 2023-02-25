import _data_read as dr
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Hershel_Bulkley(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   func1 = lambda x,kappa,n,tauY: kappa*np.power(x,n)+tauY
   func=np.vectorize(func1)
   Xdata=gamma
   Ydata=tau
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='rownanie Hershela-Bulkley`a' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1,1,0])
   print('Standardowe odchylenie dopasowania fit (Hershel-Bulkley, tau) = ',dr.stdev(Xdata,Ydata,func,popt))
   plt.plot( Xdata, func(Xdata,*popt), 'b',
             label='dopasowanie: kappa = %5.3e, n = %5.3e, tauY = %5.3e' % tuple( popt ) )
   plt.xlabel('gamma')
   plt.ylabel('tau')
   plt.legend()
   plt.pause(0.001)

def Bingham(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   func1 = lambda x,kappa,tauY: kappa*x+tauY
   func=np.vectorize(func1)
   Xdata=gamma
   Ydata=tau
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='rownanie Bimghama' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1,0])
   print('Standardowe odchylenie dopasowania fit (Bimgham, tau) = ',dr.stdev(Xdata,Ydata,func,popt))
   plt.plot( Xdata, func(Xdata,*popt), 'b',
             label='dopasowanie: kappa = %5.3e, tauY = %5.3e' % tuple( popt ) )
   plt.xlabel('gamma')
   plt.ylabel('tau')
   plt.legend()
   plt.pause(0.001)

def Cason(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   func1 = lambda x,kappa,tauY: np.sqrt(abs(kappa*x))+np.sqrt(abs(tauY))
   func=np.vectorize(func1)
   Xdata=gamma
   Ydata=tau
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='rownanie Casona' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1,1])
   print('Standardowe odchylenie dopasowania (Cason, tau) = ',dr.stdev(Xdata,Ydata,func,popt))
   plt.plot( Xdata, func(Xdata,*popt), 'b',
             label='dopasowanie: kappa = %5.3e, tauY = %5.3e' % tuple( popt ) )
   plt.xlabel('gamma')
   plt.ylabel('tau')
   plt.legend()
   plt.show()

Hershel_Bulkley("wyniki.xls")

Bingham("wyniki.xls")

Cason("wyniki.xls")
