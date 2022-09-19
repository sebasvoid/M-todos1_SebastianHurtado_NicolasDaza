# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 23:28:15 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt


funcion = lambda x: (1+ (np.e**(-x**2)))**0.5

def simpson3_8(a,b,n,funcion):
    h=(b-a)/n
    
    p1= funcion(a)
    p2=funcion(b)
    sumatoria=0
    
    for i in range(1,n):
        
        if i%3==0:
            
            xn=2*funcion(a + i*h)
            
            
        else:
            xn= 3*funcion(a + i*h)
            
        
        sumatoria +=xn
    
    integral= ((3/8))*(sumatoria+p1+p2)*h
    
    return integral

print(simpson3_8(-1, 1,300, funcion))
        
        