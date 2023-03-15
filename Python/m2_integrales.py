import numpy as np
import pylab as plt
from sympy import * # Librería de Calculo
from sympy.plotting import plot as symplot # Librería para las gráficas
from sympy.abc import x, y, h,a,b,c,d # Carga de un simbolico "x"
from sympy.plotting.pygletplot import PygletPlot as Plot # Librería para las gráficas
from matplotlib import pyplot as plt
from scipy.integrate import quad,dblquad

# Integral definida entre un intervalo: 

def func(x):
    return  x**2 + 8*x + 6

int_def = quad(func,0,2) # Importante no poner (x).

print(int_def[0])

print(float(integrate(func(x),(x,0,2)))) # integral definida mediante integrate

# Integral simbólica:

func2 = 4*x**3 + 5*x**2 + 7*x + 10

func2_int = integrate(func2,x)

func2_int = Integral(func2_int,x).doit()

print(func2_int)

# Integrales Múltiples

func3 = 1 # Aqui se puede introducir cualquier cosa
integral_2 = integrate(func3,(y,a,b))
Res = simplify(integrate(integral_2,(x,c,d))) # Importante simplificar

print(Res)

f = lambda x,y : 16*x*y
g = lambda y : 0
h = lambda y : np.sqrt(1-4*y**2)

Res2 = dblquad(f,0,0.5,g,h)
print(Res2)

# Ejercicios:

f = sin(x)
k = 5

Res1 = integrate(k*f,(x,-pi/2,pi))
print(Res1)

Res2 = k * integrate(f,(x,-pi/2,pi))
print(Res2)



