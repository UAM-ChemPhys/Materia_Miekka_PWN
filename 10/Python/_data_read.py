import xlrd
import numpy as np


def Data_Read(file1):
   #  Plik powinien zawierac jedynie dane numeryczne w postaci kolumn
   #  z ktorych pierwsze 6 powinno zawierac
   #  RPM      Viscosity       EOS      ShearStress     Temperature     Time
   #============================================================================
   Visc_D = xlrd.open_workbook(file1)
   dataV = Visc_D.sheet_by_index(0)
   eta=[]
   tau=[]
   t=[]
   gamma=[]
   for i in range(0, dataV.nrows):
      eta.append(dataV.cell(i, 1).value)
      tau.append(dataV.cell(i, 3).value)
      t.append(dataV.cell(i, 5).value)
      gamma.append(dataV.cell(i, 3).value/dataV.cell(i, 1).value)
   return eta,gamma,tau,t

def stdev(Xdata,Ydata,func,popt):
   N=len(Xdata)
   sum=0
   for i in range(0,N):
     sum+=np.power(func(Xdata[i],*popt)-Ydata[i],2)
   return np.sqrt(sum/N)