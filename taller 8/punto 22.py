# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:36:25 2022

@author: Sebastian Hurtado
"""

import numpy as np


''''Para este problema se usara la formula de combinaciones con repeticion
se imagina que se tienen 10 numeros 1 que se quieren organizar en 3 espacios
si hay 3 unos en una casilla corresponde al numero 3, si hay 4, al numero 4 
y asi sucesivamente, planetado de esta forma, e problema se resuleve asi'''

r=10 # numero de unos

n=3 # numero de casillas disponibles

combinaciones= (np.math.factorial(r+n-1))/(np.math.factorial(r)*np.math.factorial(n-1))
                

print(combinaciones)