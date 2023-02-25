import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math



def fit():
   file1='wyniki.txt'
   #file1 = str(input('Nazwa pliku:  '))
   func1 = lambda x,C,gamma,omega: math.log(C)+(gamma-1)*math.log(x)+x*math.log(omega)
   func=np.vectorize(func1)
   AA=np.loadtxt(file1,delimiter=',',skiprows = 0)
   Xdata=AA[:,0]
   Ydata = AA[:, 3]
   plt.figure( num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k' )
   plt.plot( Xdata, Ydata, 'o', label='' )
   popt, pcov = curve_fit(func, Xdata, Ydata, p0=[1,1,1])
   plt.plot( Xdata, func( Xdata, *popt ), 'b',
             label='dopasowanie: C = %5.3f, gamma = %5.3f omega_eff = %5.3f' % tuple( popt ) )
   plt.xlabel('N')
   plt.ylabel('E')
   plt.legend()
   plt.show()

fit()
