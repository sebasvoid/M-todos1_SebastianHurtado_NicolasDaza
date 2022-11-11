# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:37:42 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt

'DEFINIMOS CONJUNTOS DE PROBABILIDAD'

Dado=np.array([0,1])  # 0 = 1,2 y 1=3,4,5,6

Colores=np.array([0,1,2]) # 0 =rojo, 1= negro , 2=verde

Pdado=np.array([2/6,4/6])

Urna1=np.array([3/10,1/10,6/10])

Urna2=np.array([6/10,2/10,2/10])

'DEFINIMOS LA FUNCION DE LA PROBABILIDAD para N lanzamientos aleatorios'

N=int(1e4)

Lchoice = np.zeros(N)
LTotal = np.zeros(N)

for i in range(N):
    
    Lchoice[i] = np.random.choice(Dado, p=Pdado)
    
    if Lchoice[i] == 0:
        
        g = np.random.choice(Colores, p=Urna1)
        if g == 1:
            LTotal[i] = 1
        if g == 2:
            LTotal[i] = 2
    else:
        g = np.random.choice(Colores, p=Urna2)
        if g == 1:
            LTotal[i] = 1
        if g == 2:
            LTotal[i] = 2
            
plt.hist(LTotal)

x=np.linspace(0,3,4)
print(x)

n,bins=np.histogram(LTotal,x)

n=n/N
print('la probabilidad de que sea roja es de', n[0],'Y la probabilidad de que sea negra es de',n[1])

' Calculo por axiomas de probabilidad'

Proja=Pdado[0]*Urna1[0]+Pdado[1]*Urna2[0]
Pnegra=Pdado[0]*Urna1[1]+Pdado[1]*Urna2[1]

print( 'probabilidad de Roja por axiomas de probabilidad:',round(Proja,2))
print( 'probabilidad de Negra por axiomas de probabilidad:',round(Pnegra,5))


'CALCULO DE PROBABILIDAD DE LAS URNAS POR AXIOMAS MATEMATICOS'

PUrna1= (Pdado[0]*Urna1[1])/Pnegra
PUrna2=(Pdado[1]*Urna2[1])/Pnegra

print('La probabilidad de que sea de la Urna 1 dado que es negra es',PUrna1)

print('La probabilidad de que sea de la Urna 2 dado que es negra es',PUrna2)


















    
    

