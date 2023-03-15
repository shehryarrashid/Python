import numpy as np
import pylab as plt
from sympy import * # Librería de Calculo
from sympy.plotting import plot as symplot # Librería para las gráficas
from sympy.abc import x, y, z, h, a, b, c # Carga de un simbolico "x"
from sympy.plotting.pygletplot import PygletPlot as Plot # Librería para las gráficas
from scipy.optimize import fsolve


# Nociones Básicas

funcio = x**2 - sin(x) - 1/2
funcio_np = lambdify(x,funcio)
np_error = fsolve(funcio_np,0.5) 
print(np_error)

# Explicación : Para funciones que contengan trigonometria utilizar fsolve()
# En caso contario se puede usar solve() or solveset()



# Metodo Biseccion : 

def Biseccion(f,a,b,epsilon,delta,n):
    
    i = 1
    h = abs(b-a)
    c = a
    
    while abs(f.subs(x,c)) > epsilon and h > delta and i <= n:
        i = i + 1
        c = (a+b)/2
        h = h/2 
        if sign(f.subs(x,a)*f.subs(x,c)) < 0:
            b = c
        else:
            a = c 
    return c

f = x**2 - 4

bis = Biseccion(f,0,4,0.01,0.01,10)
print(bis)



