# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:19:25 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt

def funcion(r):
    
    return r[0]**2+  r[1]**2 + r[2]**2 + r[3]**2-1

G = (funcion,)

def GetVectorF(G,r):
    
    vector = G[0](r)
    
    return np.array([vector])

def GetMetric(G,r):
    
    vector = GetVectorF(G,r)
    
    return np.linalg.norm(vector)

def GetJacobian(G,R,h=1e-6):
    
    dimension = len(G)
    
    J = np.zeros((dimension,4))
    
    for i in range(dimension):
        
        for j in range(4):
            
            auxi = np.zeros(4)
            
            auxi[j] = h
            
            J[i,j] = (  G[i](R+auxi) - G[i](R-auxi) )/(2*h)
        
    return J.T

def Puntos(minimo=-1,maximo=1):
    puntos = [np.random.uniform(minimo,maximo),np.random.uniform(minimo,maximo),
         np.random.uniform(maximo,maximo),np.random.uniform(minimo,maximo)]
    return puntos


def GetSolve(G,r,lr=1e-3,ep=int(1e5),error=1e-7):
    
    d = 1
    
    it = 0
    
    vector_f = np.array([])
    
    vector_r = np.array(r)
    
    while d > error and it < ep:
        
        actualf = GetMetric(G,r)
        
        J = GetJacobian(G,r)
        
        gvector = GetVectorF(G,r)

        
        r -= lr*np.dot(J,gvector) 
        
        vector_r = np.vstack((vector_r,r))
        
        Nuevof = GetMetric(G,r)
        
        vector_f = np.append(vector_f,Nuevof)
        
        d = np.abs( actualf - Nuevof )/Nuevof
        
        it += 1
        
    
        
    if it == ep:
        
        print('Entrenamiento incompleto ')
        
    return r,it,vector_f,vector_r


N = 1e3
puntos = np.zeros((int(N),4))

for i in range(int(N)):
    
    sol,it,vect,rvect=GetSolve(G,Puntos())
    
    puntos[i,0]= sol[0]
    
    puntos[i,1]= sol[1]
    
    puntos[i,2]= sol[2]
    
    puntos[i,3]= sol[3]
    
fig = plt.figure(figsize=(8,8))

ax = fig.add_subplot(1,1,1, projection = '3d')

ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)

ax.view_init(10, 60)
X=Puntos[:,0]
Y=Puntos[:,1]
Z=Puntos[:,2]

ax.scatter(X,Y,Z)

plt.show()