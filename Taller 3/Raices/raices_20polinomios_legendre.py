# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 00:00:54 2022

@author: Sebastian Hurtado
"""

import numpy as np

import sympy as sym

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

def PolinomiosLegendre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = (x**2-1)**n
    
    p = sym.diff(y,x,n)/(2**n * np.math.factorial(n))
    
    return p

def GetRootsPolynomial(n,xi,poly,dpoly):
    
    x = sym.Symbol('x',Real=True)
    
    pn = sym.lambdify([x],poly[n],'numpy')
    dpn = sym.lambdify([x],dpoly[n],'numpy')
    Roots = GetAllRoots(pn,dpn,xi,tolerancia=8)
    
    return Roots

polinomios = []
derivadas = []

x = sym.Symbol('x',Real=True)
n=20

for i in range(n+1):
    
    poly = PolinomiosLegendre(i)
    
    polinomios.append(poly)
    derivadas.append(sym.diff(poly,x,1))

#raices=GetRootsPolynomial(6,xi,funcion,derivada_funcion)

xi=np.linspace(-1,1,100)
for j in range(1,21):
    
    raices=GetRootsPolynomial(j,xi,polinomios,derivadas)
    
    print('el polinomio n'+str(j)+' tiene estas raices: ', raices)



    