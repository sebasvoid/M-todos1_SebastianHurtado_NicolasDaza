# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 12:55:08 2022

@author: Sebastian Hurtado
"""
import numpy as np
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Sigmoid.csv'
url_data=urllib.request.urlopen(url)
   


Data = pd.read_csv(url_data,sep=',')
x = np.float64(Data['x'])
y = np.float64(Data['y'])
N = len(x)

def M_model(x,Q):
    
    solve= Q[0]/(Q[1] + np.e**(-Q[2]*x))
    
    return solve

def F_costo(x,y,Q):
    
    
    M=M_model(x,Q)
    
    solve=np.sum((y-M)**2)
    
    return solve

def GetJacobian(x,y,Q,h=1e-6):
    
    dim = len(Q)
    
    J = np.zeros((dim))
    
    
    J[0] = ( F_costo(x,y,[Q[0]+h,Q[1],Q[2]]) - F_costo(x,y,[Q[0]-h,Q[1],Q[2]]))/(2*h)
    J[1] = ( F_costo(x,y,[Q[0],Q[1]+h,Q[2]]) - F_costo(x,y,[Q[0],Q[1]-h,Q[2]]) )/(2*h)
    J[2] = ( F_costo(x,y,[Q[0]+h,Q[1],Q[2]+h]) - F_costo(x,y,[Q[0],Q[1],Q[2]-h]) )/(2*h)
        
    return J

Q=[1,1,1]


def GradDescend(Q,lr=1e-5,itmax=10000,error=0.01):
    it = 0
    p = 1
    while p > error and it < itmax:
        
        x1 = GetJacobian(x,y,Q)
        
        
        Q = Q - lr*x1
        
        p = np.linalg.norm(Q)
        
        it += 1
        
    if it==itmax:
        
        print('El entrenamiento no ha sido completado')
        
    if p< error:
        
        print('El entrenamiento no ha sido completado')
    return Q,p,it

x2=np.linspace(min(x),max(x),500)
Tsol,d,it=GradDescend([1,1,1])

Solve,d,it=GradDescend([1,1,1])

plt.scatter(x,y,label='Datos')
plt.plot(x2,M_model(x2,Tsol),color='r')