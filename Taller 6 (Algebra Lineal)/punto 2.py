# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:51:52 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt


M = np.array([[3,-1,-1],[-1.,3.,1.],[2,1,4]])

b = np.array([1.,3.,7.])

class Solvelineal:
    
    def __init__(self,M,b,itmax=1000,error=1e-10):
        
         self.M=M
         self.b=b
         self.itmax=1000
         self.error=error
    def GausSeidel(self):
        
        M,N = self.M.shape
        
        y = np.zeros(N)
        
        sumk = np.zeros_like(y)
        
        x = [13,21,-1]
        
        
        
        
        
        it = 0
        
        residuo = np.linalg.norm( self.b - np.dot(self.M,x) )
        
        while ( residuo > self.error and it < self.itmax ):
            
            #print(x)
            it += 1
            xk=(-self.M[0,1]*x[1] - self.M[0,2]*x[2] + self.b[0])/self.M[0,0]
            
            yk= (-self.M[1,0]*xk - self.M[1,2]*x[2] + self.b[1])/self.M[1,1]
            
            zk= (-self.M[2,0]*xk - self.M[2,1]*yk + self.b[2])/self.M[2,2]
            
            x2= [xk,yk,zk]
            for i in range(M):
                sum_ = 0
                for j in range(N):
                    if i != j:
                        sum_ += self.M[i][j]*x2[j]
                        #print(x2)
                sumk[i] = sum_
                
            for i in range(M):
                
                if self.M[i,i] != 0:
                    x[i] = (self.b[i] - sumk[i])/self.M[i,i]
                    
                else:
                    print('No invertible con Jacobi')
                #print(x)
            
            residuo = np.linalg.norm( self.b - np.dot(self.M,x) )
            
        return x,it,residuo
    
    def jacobi(self):
        
        M,N = self.M.shape
        
        y = np.zeros(N)
        
        sumk = np.zeros_like(y)
        
        x = [13,21,-1]
        
        
        
        
        
        it = 0
        
        residuo = np.linalg.norm( self.b - np.dot(self.M,x) )
        
        while ( residuo > self.error and it < self.itmax ):
            
            #print(x)
            it += 1
            
            for i in range(M):
                sum_ = 0
                for j in range(N):
                    if i != j:
                        sum_ += self.M[i][j]*x[j]
                        #print(x2)
                sumk[i] = sum_
                
            for i in range(M):
                
                if self.M[i,i] != 0:
                    x[i] = (self.b[i] - sumk[i])/self.M[i,i]
                    
                else:
                    print('No invertible con Jacobi')
                #print(x)
            
            residuo = np.linalg.norm( self.b - np.dot(self.M,x) )
            
        return x,it,residuo
    

init=Solvelineal(M, b)

solve_Seidel=init.GausSeidel()

solve_jacobi=init.jacobi()

print(solve_jacobi)

print(solve_Seidel)
