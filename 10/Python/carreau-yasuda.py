import _data_read as dr
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Careau_Yasuda(name):
   eta,gamma,tau,t=dr.Data_Read(name)
   func1 = lambda x,eta0,etainf,lambda1,a,n: (eta0-etainf)*np.power(1+np.power(lambda1*x,a),n-1)+etainf
   func=np.vectorize(func1)
   Xdata=gamma
   Ydata=eta
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='rownanie Carreau-Yasudy' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1000,100,10,0,1])
   print('Standardowe odchylenie dopasowania fit (eta) = ',dr.stdev(Xdata,Ydata,func,popt))
   plt.plot( Xdata, func( Xdata, *popt ), 'b',
             label='dopasowanie: eta0 = %5.3e, etainf = %5.3e lambda = %5.3e \na = %5.3e n = %5.3e' % tuple( popt ) )
   plt.xlabel('gamma')
   plt.ylabel('eta')
   plt.legend()
   plt.show()

Careau_Yasuda("wyniki.xls")
