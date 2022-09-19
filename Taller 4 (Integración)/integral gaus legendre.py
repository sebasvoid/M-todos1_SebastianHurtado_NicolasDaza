# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 00:23:34 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt

''' Pesos y abcisas para 2 puntos'''
w2N=[1,1]
zt2=[(3**0.5)/3,-(3**0.5)/3]

'''pesos y abcisas para 3 puntos'''

w3N=[0.55555,0.88888,0.55555]

zt3=[(15**0.5)/5,0,-(15**0.5)/5]

''' desarrollo de la integral'''

funcion= lambda x: 1/x**2

def gaus_legendre(a,b,n,funcion,pesos,abcisas):
     
    b_a= (b-a)/2
    
    a_b= (a+b)/2
    sumatoria=0
    for i in range(n):
                   
        xn=pesos[i]*funcion(b_a*abcisas[i] + a_b)
        
        sumatoria += xn
    
    integral= b_a*sumatoria
    
    return integral

print(' integal con 2 pntos:',gaus_legendre(1, 2, 2, funcion, w2N, zt2))

print(' integal con 3 pntos:',gaus_legendre(1, 2, 3, funcion, w3N, zt3))
                   
        