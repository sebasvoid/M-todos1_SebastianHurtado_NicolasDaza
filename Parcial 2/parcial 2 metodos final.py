# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:05:50 2022

@author: Sebastian Hurtado
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

' Punto a) deficinicion de funcion de temperatura'


def aproximacion_bilineal(t,a):
    
    temperatura=0 
        
    for i in range (2):
        for j in range(2):
            temperatura+=a[j,i]*t[0]**j * t[1]**i
                        
    return temperatura

' Punto B) matriz de posicionamiento'

'coordenadas de cada punto(x,y,temperatura)'

p1=[1,1,1]
p2=[-1,1,2]
p3=[-1,-1,0.5]
p4=[1,-1,0.3]

' definicion de matriz de coordenada'

position = np.zeros((4,2))

n=1

for i in position:
    
    i[0]+=n
    i[1]+=n
position[1][0]*=-1
position[2][0]*=-1
position[2][1]*=-1
position[3][1]*=-1


print('la matriz de vectores de posicion es:')

print(position)

'crear matriz de factores'


'primer paso, definir la matriz y sus valores'

Temp=np.array([p1[2],p2[2],p3[2],p4[2]])

T=np.array([])

matriz1=np.zeros((4,4))

for i in range(4):
    
    t=Temp[i]
    
    T=np.append(T,t)
    
    fila= [1,position[i,0],position[i,1],position[i,0]*position[i,1]]
    
    
    matriz1[i]=fila

print('la matriz A de la solucion AX=Y es: ')

print(matriz1)

print('la matriz X de la solucion AX=Y es:')

print(T)

'segundo paso, encontrar la solucion con algun metodo y comparar con la solucion de spyder'

def Sol_Minv(A,B):
    a = np.linalg.inv(A)
    sol = np.dot(a,B)
    return sol


'comparar'

j=Sol_Minv(matriz1, T)

solve_spyder= np.linalg.solve(matriz1,T)

print(' la solucion por el metodo es:')
print(j)
print(' la solucion por el spyder es:')
print(solve_spyder)

'definir  matriz de coeficientes de a00...a11:'

a=np.zeros((2,2))

for i in range (2):
    a[i]=[j[i],j[2+i]]
    
print(' la matriz de coeficientes es:')

print(a)

'Punto D) verificar condiciones frontera'

print('la temperatura en el punto (1,1) es: ',aproximacion_bilineal((1,1), a))
print('la temperatura en el punto (-1,1) es: ',aproximacion_bilineal((-1,1), a))
print('la temperatura en el punto (-1,-1) es: ',aproximacion_bilineal((-1,-1), a))
print('la temperatura en el punto (1,-1) es: ',aproximacion_bilineal((1,-1), a))
            


' Punto E) grafica 2D y 3D de ltemperatur del satelite '


'2D'

x, y = np.meshgrid(np.linspace(-1,1,100), np.linspace(-1,1,100))

z = aproximacion_bilineal((x,y), a)

l_x=x.min()
r_x=x.max()
l_y=y.min()
r_y=y.max()
l_z,r_z  = -np.abs(z).min(), np.abs(z).max()



figure, axes = plt.subplots()

c = axes.pcolormesh(x, y, z, cmap='coolwarm', vmin=l_z, vmax=r_z)
axes.set_title('Mapa de temperatura')
axes.axis([l_x, r_x, l_y, r_y])
figure.colorbar(c)

'3D'

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1, projection = '3d')

surface = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

#configurar límites de los ejes
axes.axis([l_x, r_x, l_y, r_y])
ax.set_zlim3d(l_z, r_z)



plt.show()

'Punto F) la temperatura fallida es:'

temperatura_fallida=aproximacion_bilineal((0,0.5), a)

print(temperatura_fallida)

'Punto G) funcion de rotacion:'

def GetRotation(angle, position):
    
    a=np.zeros((2,2))
    
    a[0][0],a[0][1],a[1][0],a[1][1]=np.cos(angle),-1*np.sin(angle),np.sin(angle),np.cos(angle)
    
    rotated=np.zeros((4,2))
    
    u=len(position)
    
    for i in range(u):
        
        rotated[i][0]=a[0][0]*position[i][0]+a[0][1]*position[i][1]
        rotated[i][1]=a[1][0]*position[i][0]+a[1][1]*position[i][1]
        
    return rotated





def GetMatrix(angle,u):
    
    new=GetRotation(angle,u)
    n=[]
    for i in new:
        x=i[0]
        y=i[1]
        n.append([x,y])
        
    Temp=np.array([n[0],n[1],n[2],n[3]])
    
    T=np.array([])
    
    for i in range(4):
        
        t=Temp[i,1]
        
        T=np.append(T,t)
        
        fila= [1,Temp[i,0],Temp[i,1],Temp[i,0]*Temp[i,1]]
        
        
        matriz1[i]=fila

    return matriz1


def Solving(m,T):
    
    ag=Sol_Minv(m, T)
    
    oth=np.zeros((2,2))
    
    for i in range (2):
        
        oth[i]=[ag[i],ag[2+i]]
        
    return oth

Ext=GetMatrix(0, position)
nu=Solving(Ext,T)

theta = np.linspace(0,2*np.pi,200)


def GetMinimal(angles,T,position,coor):
    group={}
    for i in angles:
        Ext=GetMatrix(i,position)
        oth=Solving(Ext,T)
        nu=aproximacion_bilineal(coor, oth)
        group[i]=nu
        a=min(group, key=group.get)
    return a

print(Ext, aproximacion_bilineal((0,0.5), nu),GetMinimal(theta,T,position,(0,0.5)))
print('el angulo que hay que rotar para minimizar es: ',GetMinimal(theta,T,position,(0,0.5)),'radianes')

'2D'


rot=GetMatrix(2.65, position)
nu=Solving(rot,T)


x, y = np.meshgrid(np.linspace(-1,1,100), np.linspace(-1,1,100))

z = aproximacion_bilineal((x,y), nu)

l_x=x.min()
r_x=x.max()
l_y=y.min()
r_y=y.max()
l_z,r_z  = -np.abs(z).min(), np.abs(z).max()



figure, axes = plt.subplots()

c = axes.pcolormesh(x, y, z, cmap='coolwarm', vmin=l_z, vmax=r_z)
axes.set_title('Mapa de temperatura')
axes.axis([l_x, r_x, l_y, r_y])
figure.colorbar(c)

'3D'

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1, projection = '3d')

surface = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

#configurar límites de los ejes
axes.axis([l_x, r_x, l_y, r_y])
ax.set_zlim3d(l_z, r_z)



plt.show() 


