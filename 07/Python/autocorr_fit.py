import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fit():
   file1='a'
   #file1 = str(input('Nazwa pliku:  '))
   func1 = lambda x,A,E,B: A*np.exp(-E*x)+B
   func=np.vectorize(func1)
   AA=np.loadtxt(file1,delimiter=',',skiprows = 0)
   Xdata=AA[:,0]
   Ydata = AA[:,1]
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='Funkcja autokorelacyjna' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1e-4,1e-3,1e-5])
   plt.plot( Xdata, func( Xdata, *popt ), 'b',
             label='fit: A = %5.3e, E = %5.3e B = %5.3e' % tuple( popt ) )
   plt.xlabel('tau')
   plt.ylabel('C(tau)')
   plt.legend()
   plt.show()

fit()
