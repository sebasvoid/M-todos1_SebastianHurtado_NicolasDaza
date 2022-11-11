# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:01:07 2022

@author: Sebastian Hurtado
"""

import numpy as np

r=4 # cuantos colores queremos elegir

n=3 # numeroi de colores

''' se usa la formula de combinaciones con repeticion donde imaginas
que tenemos 3 colores y los queremos ubicar de 4 formas'''

combinacion= (np.math.factorial(r+n-1))/(np.math.factorial(r)*np.math.factorial(n-1))

''' sin emabrgo, al utilizar este conteo existe la posibilidad de que los 4 espacios
sean ocupados por 4 llaes del mismo color, pero solo se tienen 3, por esta razon, al
resultado final le restamos 3 ya que son estos los casos donde estan los 4 espacios 
con 4 llaves del mismo color, esto nos daria la respuesta correcta'''

combinacion=combinacion-3

print(combinacion)