# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:43:05 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt

n=10**4

k= 30



def correlacion(puntos,k):
    
    a=np.random.rand(puntos)
    coeficientes=[]
    sumatoria=0
    
    for i in range(1,k+1):
        print(i)
        
        for j in range(len(a)):
            #print(j-k)
            sumatoria+= a[j] * a[j-i]
            
   
        
        resultado= (1/puntos)*sumatoria
    
        coeficientes.append(resultado)
        
        sumatoria=0
      
    
    
    return coeficientes

    
    
    
resultado=correlacion(n,k)

vecinos=[]


for i in range(1,k+1):
    
    vecinos.append(i)
    
print(resultado)



    
plt.plot(vecinos,resultado)