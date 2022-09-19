# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:43:08 2022

@author: Sebastian Hurtado
"""
import numpy as np

import sympy as sym

import matplotlib.pyplot as plt

def PolinomiosLaguerre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = ((np.e**-x*x**n))
    
    p = sym.diff(y,x,n)*(np.e**x/(np.math.factorial(n)))
    
    return p

''' funciones para hallar las raices de los polinomios'''

def GetNewtonMethod(f,df,xn,itmax = 100000, precision=1e-12):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
           
            error = np.abs(f(xn)/df(xn))
        
        except ZeroDivisionError:
            print("zero division")
            
        xn  = xn1
        it += 1
    
    #print('Raiz:',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn

def GetAllRoots(f,df,x, tolerancia=9):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewtonMethod(f,df,i)
          
        if root != False:
            
            croot = np.round( root, tolerancia ) 
            
            if croot not in Roots:
                Roots = np.append( Roots, croot )
                
    # Ordenamos las raices
    Roots.sort()
    
    return Roots

def GetRootsPolynomial(xi,poly,dpoly):

    
    x = sym.Symbol('x',Real=True)
    
    pn = sym.lambdify([x],poly,'numpy')
    dpn = sym.lambdify([x],dpoly,'numpy')
    Roots = GetAllRoots(pn,dpn,xi,tolerancia=8)
    
    return Roots
    

''' funcion para hallar los pesos'''

def pesosLaguerre(puntos):
    
    xi=np.linspace(0,100,1000)
    
    x = sym.Symbol('x',Real=True)
    
    pesos= []
    
    ln=PolinomiosLaguerre(puntos+1)
    
    ln2=PolinomiosLaguerre(puntos)
    
    lnx = sym.lambdify([x],ln2,'numpy')
        
    dln=sym.diff(ln,x)
    
    
    xi=np.linspace(0,100,1000)
    
    raices= GetRootsPolynomial(xi, ln, dln)
    
    
    
    for i in raices:
        
       
        
        wk= i/((puntos+1)**2 * (lnx(i)**2))
        
        
        
        pesos.append(wk)
        
        
    return pesos

''' funcion para la integral'''

def GausLaguerre(funcion,puntos):
    
    
    x = sym.Symbol('x',Real=True)
    
    xi=np.linspace(0,100,1000)
                    
    pesos=pesosLaguerre(puntos)
    
        
    f=sym.lambdify([x],funcion,'numpy')
    
    integral=0

    
    funl=PolinomiosLaguerre(puntos+1)
    
    dfunl=sym.diff(funl,x)
    
    raices= GetRootsPolynomial(xi,funl,dfunl)
    
        
    for i in range(len(pesos)):
                       
        xn=pesos[i]*(f(raices[i]))
        
        integral += xn
        
    return integral

  
''' funcion'''

x = sym.Symbol('x',Real=True)
f= ((x**3)/(np.e**x - 1))* np.e**(x)

''' prueba'''

resultado= GausLaguerre(f,3)

#pesos=pesosLaguerre(1)
print(resultado)

''' grafica derivada en n puntos'''

p=11
valores=[]
puntoss=[]
for i in range(1,p):
    
    derivada=GausLaguerre(f,i)
    error=derivada/((np.pi**4)/15)
    puntoss.append(i)
    valores.append(error)
    

plt.scatter(puntoss,valores,color='r')

plt.show() 
    




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    