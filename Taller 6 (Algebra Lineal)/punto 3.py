# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:35:12 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt

A=np.array([[1,0,0],[5,1,0],[-2,3,1]])

D=np.array([[4,-2,1],[0,3,7],[0,0,2]])

def MultiMatricez(A,D):
    
    M,N=A.shape
    
    "M=filas"
    "N=columnas"
    
    J,K=D.shape
    
    "J=filas"
    "K=columnas"
    
    C= np.zeros((M,K))
    
    it=0
    
    fila=0
    
    columna=0
    
    
    
    
    if N==J:
        
        while it < (M*K): 
            
            suma=0
            
            if fila < M:
                
                for i in range(J):
                    
                    suma += A[fila,i]* D[i,columna]
                    
                C[fila,columna]=suma    
                    
                columna+=1
                
            if columna == K:
               
               columna=0
               
               fila+=1
                                           
            it +=1
    
            
    else:
        print('el numero de columnas de la primera matriz'/
              'debeser igual al numero de filas de la segunda matriz')
        
    return C


print(MultiMatricez(A, D))
            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            