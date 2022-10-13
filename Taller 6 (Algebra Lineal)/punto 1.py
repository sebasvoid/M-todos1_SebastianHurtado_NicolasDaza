# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 23:01:13 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt

M = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])

b = np.array([1.,3.,7.])



def GetGausSeidelMethod(A,b,itmax=1000,error = 1e-10):
    
    M,N = A.shape
    
    y = np.zeros(N)
    
    sumk = np.zeros_like(y)
    
    x = [13,21,-1]
        
    it = 0
    
    residuo = np.linalg.norm( b - np.dot(A,x) )
    
    while ( residuo > error and it < itmax ):
        
        print(x)
        it += 1
        xk=(-A[0,1]*x[1] - A[0,2]*x[2] + b[0])/A[0,0]
        
        yk= (-A[1,0]*xk - A[1,2]*x[2] + b[1])/A[1,1]
        
        zk= (-A[2,0]*xk - A[2,1]*yk + b[2])/A[2,2]
        
        x2= [xk,yk,zk]
        for i in range(M):
            sum_ = 0
            for j in range(N):
                if i != j:
                    sum_ += A[i][j]*x2[j]
                    #print(x2)
            sumk[i] = sum_
            
        for i in range(M):
            
            if A[i,i] != 0:
                x[i] = (b[i] - sumk[i])/A[i,i]
                
            else:
                print('No invertible con Jacobi')
            #print(x)
        
        residuo = np.linalg.norm( b - np.dot(A,x) )
        
    return x,it,residuo

print(GetGausSeidelMethod(M, b))