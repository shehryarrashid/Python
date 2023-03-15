from cProfile import label
from cmath import cos, sin
import numpy as np
import scipy
import sympy
from sympy.plotting import plot as symplot # Librería para las gráficas
from sympy.abc import x, y, h, a, b, c, z # Carga de un simbolico "x"
from sympy.plotting.pygletplot import PygletPlot as Plot # Librería para las gráficas
from scipy.interpolate import * # Include de todas las interpolaciones 
import matplotlib.pyplot as plt


# Barycentric Interpolacion (Interpolacion Básica)

# Definicion puntos. funcion = 1 / (1 + x**2)

xx = np.arange(11) -5 # Definimos 11 puntos entre el -5 y 5
yy = 1 / (1 + xx**2) # Sustituimos Cada Punto en la funcion 

x = np.linspace(-5,5,100) # Definimos 100 espacios en el eje x 
y = barycentric_interpolate(xx,yy,x) # Interpolamos con los puntos calculados anteriormente y usamos el eje x 

fp2 = 1 / (1 + x**2) # Sustituimos los 100 puntos del eje x en la funcion
# Basicamente se hace para ver la funcion en el grafico

# Representacion Visual
    
fig,ax = plt.subplots(figsize=(7,7)) # Crea la maqueta de la figura
ax.plot(x,fp2,'black') # En el eje x dibuja los 100 puntos creando la figura original
ax.plot(x,y,'red') # Funcion Interpoladora
ax.plot(xx,yy,'o') # Puntos interpolados
plt.show()



# Interpolacion Lagrange:



Puntos_X = [0,2]
Puntos_Y = list(1 + let**2 for let in Puntos_X)
#print(f'{Puntos_X}\n{Puntos_Y}')

#interp_lagrange = sympy.polys.specialpolys.interpolating_poly(1,x,X=Puntos_X,Y=Puntos_Y) # Lagrange

lagranja = lagrange(Puntos_X,Puntos_Y) # No tiene niguna utilidad excepto que para obtener el cociente

# Splines:

# Numpy Interpolation np.interp(domain,x,y)

X_Pato = np.arange(23) - 11
Y_Pato = [12,21,4,2,43,21,4,38,64,3,1,3,5,43,5,65,43,23,1,2,4,6,32]

X_DOMAIN = np.linspace(min(X_Pato),max(X_Pato),1000)

spline = np.interp(X_DOMAIN,X_Pato,Y_Pato)

fig,ax = plt.subplots(figsize=(10,8))
ax.plot(X_DOMAIN,np.transpose(spline),label="Funcion Interpoladora")
ax.plot(X_Pato,np.transpose(Y_Pato),'o',label="Puntos A Interpolar")
ax.legend()
plt.show()

# Numpy Interpolacion scipy.interpolate.interp1d(puntosx,puntosy,'cubic')(linspace)

from scipy import *

x_pato = [0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.8, 5.0, 6.0, 7.0, 8.0, 9.1, 10.5, 11.2, 11.6, 12, 12.6, 13, 13.2]
y_pato = [1.3, 1.5, 1.8, 2.1, 2.6, 2.7, 2.3, 2.1, 2.0, 2.1, 2.2, 2.3, 2.2, 1.9, 1.4, 0.9, 0.8, 0.6, 0.5, 0.4, 0.2]
dominio = np.linspace(min(x_pato),max(x_pato),1000)


spl = scipy.interpolate.interp1d(x_pato,y_pato,'cubic')(dominio)

fix,ax = plt.subplots(figsize = (10,8))
ax.plot(dominio,spl,'black')
plt.show()


xp = [2506.7,2582.8,2658.1,2733.7,2810.4,2967.9,3131.6]
yp = [100,150,200,250,300,400,500]

xli = np.linspace(min(xp),max(xp),1000)
interp = scipy.interpolate.interp1d(xp,yp,'cubic')
real = interp(xli)
concisada = interp(2680.78)

plt.plot(xli,np.transpose(real),'black',label = "Interpolacion")
plt.plot(2680.78,np.transpose(concisada),'o',label = "Concisada")
plt.legend()
plt.show()

she = [2,3,4,5,6,7,8,10,20,25,30,45,90]
he = [10,-7,-3,20,5,-4,7,-7,24,12,11,-23,9]
domaina = np.linspace(min(she),max(she),1000)

interp = interpolate.interp1d(she,he,'cubic')(domaina)

plt.plot(domaina,interp,'black')
plt.plot(she,he,'o')
plt.show()



