# Examen 2. Analisis Numerico
# Alumno: Luis Mario Ruelas Heras

# Ejercicio 1. Utilice el metodo de Newton-Raphson para calcular raiz cubica
# de 75 con una precisión de cuatro cifras significativas.

# Tenemos (75)**(1/3) = x, y queremos encontrar el valor de x
# Entonces podemos escribirla como 75 - x**3 = 0

import sys

## Modulo Newton-Raphson
## raiz = newtonRaphson(f,df,a,b,tol=1.0e-9).
## Encuentra la raiz de f(x) = 0 combinando Newton-Raphson
## con biseccion. La raiz debe estar en el intervalo (a,b).
## Los usuarios definen f(x) y su derivada df(x).
def err(string):
  print(string)
  input('Press return to exit')
  sys.exit

def newtonRaphson(f,df,a,b,tol=1.0e-9):
  from numpy import sign
  fa = f(a)
  if fa == 0.0: return a
  fb = f(b)
  if fb == 0.0: return b
  if sign(fa) == sign(fb): err('La raiz no esta en el intervalo')
  x = 0.5*(a + b)
  for i in range(30):
    print(i)
    fx = f(x)
    if fx == 0.0: return x 
    if sign(fa) != sign(fx): b = x # Haz el intervalo mas pequeño
    else: a = x
    dfx = df(x)  
    try: dx = -fx/dfx # Trata un paso con la expresion de Delta x
    except ZeroDivisionError: dx = b - a # Si division diverge, intervalo afuera
    x = x + dx # avanza en x
    if (b - x)*(x - a) < 0.0: # Si el resultado esta fuera, usa biseccion
      dx = 0.5*(b - a)
      x = a + dx 
    if abs(dx) < tol*max(abs(b),1.0): return x # Checa la convergencia y sal
  print('Too many iterations in Newton-Raphson')


# Definimos la funcion
def f1(x):
    return 75 - x**3

#Definimos la derivada de la funcion
def df1(x):
    return -3 * x**2

# Definimos los extremos del intervalo
a = 4
b = 5

raiz = newtonRaphson(f1, df1, a, b)
raiz = round(raiz, 4)
print(f'El valor buscado es: {raiz}')

#%%

# Ejercicio 2. Encuentre la raiz positiva real mas pequeña de la ecuacion,
# utilizando el metodo de biseccion

# Metodo de Biseccion Mejorado para el Ejemplo de clase

def y(x):                    # define la funcion y(x)
  y = x**3 - 3.23 * x**2 - 5.54 * x + 9.84
  return y

# Graficar la funcion para ver las raices
import numpy as np
import matplotlib.pyplot as plt

ax = np.linspace(-3, 3, 100)
ay = y(ax)

plt.plot(ax,ay)
plt.grid(True)
plt.title('Grafica de la funcion y = x³ - 3.23x² - 5.54x + 9.84')
plt.show()

# De la grafica notamos que la raiz mas pequeña este entre x = 1 y x = 2
# Por lo tanto escribimos x1 = 1 y x2 = 2

x1 = float(input('Captura el valor de x1: ')) # peticion de valor x1
x2 = float(input('Captura el valor de x2: ')) # peticion de valor x2
y1 = y(x1)                                    # evalua la funcion y(x1)
y2 = y(x2)                                    # evalua la funcion y(x1)

if y1*y2 > 0:                                 # prueba si los signos son iguales
  print('No hay raices en el intervalo')
  exit

for i in range(100):
  xh = (x1+x2)/2
  yh = y(xh)                                  # evalua la funcion y(xh)
  y1 = y(x1)                                  # evalua la funcion y(x1)
  if abs(y1) < 1.0e-6:
    break
  elif y1*yh < 0:
    x2 = xh
  else:
    x1 = xh
print('La raiz es: %.5f' % x1)
print('Numero de bisecciones: %d' % (i+1))

#%%

# Ejercicio 3. Utilice aproximaciones por diferencias finitas para calcular
# f'(2.36) y f"(2.36)

# x = [2.36, 2.37, 2.38, 2.39]
# fx = [0.85866, 0.86289, 0.86710, 0.87129]

# Como nos piden las derivadas en x = 2.36, solamente podemos calcular
# las derivadas con aproximacion de diferencias forward.

# Para la primera derivada

# Funcion para calcular la primera derivada con aproximacion forward
def df(fx, h, fxh):
    df = (fxh - fx) / h
    return df

fx = 0.85866 # f(x), en este caso f(2.36)
h = 0.01 
fxh = 0.86289 # f(x+h), en este caso f(2.37)

# Calculamos f'(2.36)
df = df(fx, h, fxh)
print("f'(2.36) =", df)

# Para la segunda derivada

# Funcion para calcular la segunda derivada con aproximacion forward
def d2f(fx, h, fxh, fx2h):
    d2f = (fx2h - 2*fxh + fx) / (h**2)
    return d2f

fx2h = 0.86710 # f(x+2h), en este caso f(2.38)

# Calculamos f"(2.36)
d2f = d2f(fx, h, fxh, fx2h)
print('f"(2.36) =', d2f)

#%%

# Ejercicio 4. Evalue la integral utilizando la regla trapezoidal recursiva
# Limites de integracion: de 0 a 1
# ∫(sin(x))/sqrt(x) dx

# Haciendo el cambio variable x = e**t, dx = e**t dt
# ∫ (sin(e**t) / sqrt(e**t)) * e**t dt

# Simplificando tenemos
# ∫ sin(e**t) * sqrt(e**t) dt


import math

e = math.e

'''
Modulo regla trapezoidal recursiva

Inew = trapecio_recursiva(f,a,b,Iold,k).
Iold = Integral de f(x) de x = a hasta b calculada
con la regla trapezoidal recursiva con 2ˆ(k-1) paneles.
Inew = la misma integral calculada con 2ˆk paneles.
'''
def trapecio_recursiva(f,a,b,Iold,k):
  if k == 1: Inew = (f(a) + f(b))*(b - a)/2.0
  else:
    n = 2**(k -2 ) # numero de nuevos puntos
    h = (b - a)/n # espaciamiento de nuevos puntos
    x = a + h/2.0
    sum = 0.0
    for i in range(n):
      sum = sum + f(x)
      x = x + h
      Inew = (Iold + h*sum)/2.0
  return Inew

def f(x):
    return math.sin(e**x) * math.sqrt(e**x)

Iold = 0.0
for k in range(1,21):
  Inew = trapecio_recursiva(f, 0.0, 1.0,Iold,k)
  if (k > 1) and (abs(Inew - Iold)) < 1.0e-6: break
  Iold = Inew

print('Integral =',Inew)
print('n Panels =',2**(k-1))