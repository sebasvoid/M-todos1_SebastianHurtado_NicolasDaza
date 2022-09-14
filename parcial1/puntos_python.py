# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:19:26 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt

tangente= lambda x: (np.tan(x))**0.5

derivada_tan= lambda x: (1/(np.cos(x))**2)/(2*((np.tan(x))**0.5))

x=np.linspace(0.1,1.1,100)

h= x[1]-x[0]

def derivadah2(x,f,h):
    
    derivada= ((-3*f(x))+ (4*f(x + h))- (f(x + 2*h)))/2*h*10000
    
    return derivada


def DerivativeC(x,f,h):
    
    return (f(x+h)-f(x-h))/(2*h)





derivadap= derivadah2(x,tangente,h)

derivadac= DerivativeC(x,tangente,h)

derivada_tan2=derivada_tan(x)

plt.scatter(x,derivadap)

plt.scatter(x,derivadac)

plt.scatter(x,derivada_tan(x))


def error(funcion1,funcion2):
    diferencia=[]
    for i in range(len(funcion1)):
        
        error= abs(funcion1[i]-funcion2[i])
        
        diferencia.append(error)
        
    return diferencia


''' graficas error nodal'''

error_nodal_progresiva=error(derivadap,derivada_tan2)

error_nodal_central=error(derivadac,derivada_tan2)

fig=plt.figure(figsize=(6,5))


ax1=fig.add_subplot(1,3,1)

ax1.scatter(x,derivadap)
ax2=fig.add_subplot(1,3,2)
ax2.scatter(x,derivadac)
ax3=fig.add_subplot(1,3,3)
ax3.scatter(x,derivada_tan(x))  

''' el error nodal es el mismo en cada derivada'''



plt.show
    
    
    

    

