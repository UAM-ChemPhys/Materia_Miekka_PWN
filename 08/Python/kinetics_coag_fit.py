import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fit():
   file1='wyniki.txt'
   #file1 = str(input('Nazawa pliku:  '))
   A0 = float(input("Rzedna poczatkowa = "))
   func1 = lambda x,B,C: A0+B*x+C*x**2
   func=np.vectorize(func1)
   AA=np.loadtxt(file1,delimiter=',',skiprows = 0)
   Xdata=AA[:,0]
   Ydata = AA[:,1]  
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='punkty eksperymentalne' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1,1])
   plt.plot( Xdata, func( Xdata, *popt ), 'b',
             label='fit: B = %5.3e C = %5.3e' % tuple( popt ) )
   plt.xlabel('t')
   plt.ylabel('A')
   plt.legend()
   plt.show()

fit()
