# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:04:21 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
n = 100 
h = (b-a)/n
x = np.arange(a+h,b,h)
sumatoria = 0


def funcion(x):
    
    f = np.exp(-x**2)
    
    return f

f = funcion(x)


    
suma1 = (h/2)*( funcion(a) + funcion(b) )



for i in range(len(x)):
    
    xn = funcion(x[i])*h
    
    sumatoria += xn
    
resultado = suma1 + sumatoria    

d2 = (funcion(x+h) - 2*funcion(x) + funcion(x-h)) / h**2
 
maxi= np.max(np.abs(d2))
error1= ((h**2)*(b-a))*(1/12)
error= error1 * maxi 


plt.plot(x,f,color='r')

print("la integarl de la funcion es: ",resultado)

print("El error de integracion esta acotado por el valor maximo promedio" 
      +" de la segunda derivada de la funcion:",error)

    