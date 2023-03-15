import numpy as np
from sympy import * # Librería de Calculo
from sympy.plotting import plot as symplot # Librería para las gráficas
from sympy.abc import x, y, h, a, b, c, z # Carga de un simbolico "x"
from sympy.plotting.pygletplot import PygletPlot as Plot # Librería para las gráficas



# Limites:

def func2(x):
    return x**2 + 4

lim1 = limit(func2(x),x,oo) # Limite x -> infinito
print(lim1) 

limder = limit((func2(x+h)-func2(x))/h,h,0) # Derivada por definicion

print(limder)

#Diferenciales:

func = 5*x**2 + 10*x + 7*y**2 + 9*y 

d1 = diff(func,x) # Derivada Parcial Respecto x
d2 = diff(func,y) # Derivada Parcial Respecto y
grad = (d1,d2) # Calculo de La Gradiente de Func
print(grad)


func3 = x**5 

d3 = diff(func3,x,5) # Derivada quinta
print(d3)



# Polinomios de Taylor:

funci = sin(x)
funci2 = series(funci,x,0,20).removeO() # Obligatorio poner removeO().
#symplot(funci2,funci) # Dibuja las dos funciones

val = funci.subs(x,90)
val2 = funci2.subs(x,90)


# Analisis de Funciones:

numerador = 2 * (x**2 -9)
denominador = (x**2 - 4)

funcio = numerador / denominador

asinhor = limit(funcio,x,oo)
asinver = solve(denominador,x)
print(asinhor,asinver)
symplot(funcio,asinhor,xlim=(-6,6),ylim=(-12,12)) # Muestra Asíntota horizontal

# Puntos Criticos:

func3 = x**2 + 8*x + 7
func3der = diff(func3,x)
CriticosX = list(solveset(func3der,x))
CriticosY = [func3.subs(x,a) for a in CriticosX]
print(CriticosX,CriticosY)





# Representacion Grafica: 

rep = symplot(func2(x),(x,0,5)) # Representacion de una funcion
rep1 = symplot(func2(x),x**2 + 7*x , (x,0,20),show = false) # Representacion de 2 funciones
rep1[0].line_color = 'skyblue' # Cambio el color de la primera funcion
rep1[1].line_color = 'orange' # Cambio el color a la segunda funcion
rep1.show() # Se muestra el grafico con las dos funcones





# Ejercicios de Derivadas:

mat = [cos(4*x),3*x],[x,sin(5*x)]
der = list([[diff(f,x) for f in mat[0]]])
der.append([diff(f,x) for f in mat[1]])
print(f'Array Solucion: {der}')

funciones = [tan(x+y),a*x + b*y + c*z,x**(0.5) - 3*y]
derivadas = list([diff(f,x) for f in funciones])
print(f'Las Derivadas de las funciones : {funciones} \n Aqui las Derivadas: \n {derivadas}')


#Matriz Jacobina:

jac = Matrix([exp(1)**x,cos(y),sin(z)])
sym = Matrix([x,y,z])

print(jac.jacobian(sym))

#Matriz Hessiana:

func = x*y + 2*z*x

print(hessian(func,(x,y)))



import matplotlib.pyplot as plt

# Obtener puntos Críticos:

func = x**2 + 8*x + 7
f1 = diff(func,x)
CriticosX = list(solveset(f1,x))
CriticosY = [func.subs(x,a) for a in CriticosX if a < 0]
# Creando mapa:

xx = np.linspace(-10,10,1000)
yy = lambdify(x,[func])(xx)
plt.plot(xx,np.transpose(yy))
plt.plot(CriticosX,CriticosY,'p')
plt.show()

