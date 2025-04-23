#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Tarea 4
# Autor: Luis Mario Ruelas Heras

# Sección 4.1

# Ejercicio 11. Encontrar las raíces de x sinx + 3 cosx - x = 0 en (-6, 6)
# utilizando el método de Newton-Raphson

import sys
from math import sin, cos

## Modulo Newton-Raphson
## raiz = newtonRaphson(f,df,a,b,tol=1.0e-9).
## Encuentra la raiz de f(x) = 0 combinando Newton-Raphson
## con biseccion. La raiz debe estar en el intervalo (a,b).
## Los usuarios definen f(x) y su derivada df(x).
def err(string):
  print(string)
  input('Press return to exit')
  sys.exit()

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



# Definición de f(x) y df(x)  
def f(x): return x*sin(x) + 3*cos(x) - x
def df(x): return x*cos(x) - 2*sin(x) - 1

# El intervalo (a,b):
a = -6
b = 6

# Encontramos la raíz
root = newtonRaphson(f, df, a, b)
print('Raíz =', root)


# In[3]:


from math import log

# Ejercicio 19. La velocidad v de un cohete Saturn V en vuelo vertical cerca
# de la superficie de la Tierra puede ser aproximada por
# v = u ln(M_0 / (M_0 - mt)) - gt
# donde
# u: velocidad de escape relativa al cohete
# M_0: masa del cohete al despegue
# m: tasa de consumo de combustible
# g: aceleración de la gravedad
# t: tiempo medido desde el despegue
# Determine el tiempo cuando el cohete alcanza la velocidad del sonido (335 m/s)

# Escribimos la ecuación igualada a cero
# Nos interesa encontrar el tiempo, así que escribimos x en lugar de t
# v - u * log(M0 / (M0 - m*x)) + g*x = 0

# Los valores de las constantes son
v = 335 # m/s
u = 2510 # m/s
M0 = 2.8 * 10**6 # kg
m = 13.3 * 10**3 # kg/s
g = 9.81 # m/s²

# Método de Bisección
# Utilizamos el método de bisección para encontrar la raíz de la ecuación
# La raíz representará el timepo en el que el cohete alcanza la velocidad del sonido

x1 = 0                # primer valor del intervalo
x2 = 100               # segudo valor del intervalo
y1 = v - u * log(M0 / (M0 - m*x1)) + g*x1    # calcula y1
y2 = v - u * log(M0 / (M0 - m*x2)) + g*x2    # calcula y2
if y1*y2 > 0:          # prueba si los signos son iguales
    print('No hay raices en el intervalo dado')
    exit               # termina el programa  #falta encontrar el buen EXIT!!
for i in range(1,101): # asume que 100 bisecciones son suficientes
  xh = (x1+x2)/2         # calcula el valor medio
  yh = v - u * log(M0 / (M0 - m*xh)) + g*xh    # calcula el valor de y en el valor medio yh
  y1 = v - u * log(M0 / (M0 - m*x1)) + g*x1   # calcula y1
  if abs(y1) < 1.0e-6:   # condicion de acercamiento a la solucion (tol)
    break                  # salir del loop
  elif y1*yh < 0:        # si el signo es diferente quedarse en la primera mitad
    x2 = xh                # que x2 sea el punto medio
  else:                  # si el signo es igual quedarse en la segunda mitad
    x1 = xh                # que x1 sea el punto medio
print('La raiz es: %.5f' % x1)
print('Numero de bisecciones: %d' % i)
print('El cohete alcanza la velocidad del sonido en %.2f' % x1 ,'segundos')


# In[6]:


# Sección 5.1
# Ejercicio 9. Calcular f'(0.2) usando los siguientes datos:
# x = [0.0, 0.1, 0.2, 0.3, 0.4]
# f(x) = [0.000000, 0.078348, 0.138910, 0.192916, 0.244981]

# Calcular la derivada con aproximación forward
# dff = [4f(x+h) - 3f(x) - f(x+2h)] / 2h  

# Calcular la derivada con aproximación backward
# dfb = [f(x-2h) - 4f(x-h) + 3f(x)] / 2h

fx = 0.138910     # f(0.2)
h = 0.1
fxh = 0.192916    # f(x+h)
fx_h = 0.078348   # f(x-h)
fx2h = 0.244981   # f(x+2h)
fx_2h = 0.0       # f(x-2h)

# Valor de la derivada con aproximación forward
dff = (4*fxh - 3*fx - fx2h) / (2*h)
# Valor de la derivada con aproximación backward
dfb = (fx_2h - 4*fx_h + 3*fx) / (2*h)

print("f'(0.2) =",dff)
print("f'(0.2) =",dfb)


# In[8]:


# Ejercicio 10. Usando cinco cifras significativas, determine d(sinx)/dx en
# x = 0.8 de (a) la primera aproximación forward y (b) la primera aproximación
# central. En cada caso, utilice la h que de el resultado más preciso.

from math import sin, cos

# Función a derivar con n decimales
def f(x, n):
    return round(sin(x), n)

# La derivada de la función (se usará para calcular el error)
def df(x, n):
    return round(cos(x), n)

# Con aproximación central
def dfc(x, h, f, n):
    dfc = (f(x+h, n) - f(x-h, n)) / (2*h)
    return dfc

# Con aproximación forward
def dff(x, h, f, n):
    dff = (4*f(x+h, n) - f(x + 2*h, n) - 3*f(x, n)) / (2*h)
    return dff

# Derivada de f con aproximación forward
h = 0.64

print("Con la aproximación forward tenemos que")
print("   h     5 dígitos   Error")
print("---------------------------")
for i in range(10):
  E1=abs(((df(0.8, 5)-dff(0.8, h, f, 5))/df(0.8, 5))*100)
  print("%.5f   %.5f    %.2f" %(h, dff(0.8 , h, f, 5),E1))
  h=h/2
print()

# Derivada de f con aproximación central
# Valor de h de prueba
# El valor de h más adecuado será el que tenga el error más pequeño
h = 0.64

print("Con la aproximación central tenemos que")
print("   h     5 dígitos   Error")
print("---------------------------")
for i in range(10):
  E1=abs(((df(0.8, 5)-dfc(0.8, h, f, 5))/df(0.8, 5))*100)
  print("%.5f   %.5f    %.2f" %(h, dfc(0.8 , h, f, 5),E1))
  h=h/2
print()


# In[9]:


# Sección 6.1
# Ejercicio 1. Use la regla trapezoidal recursiva para evaluar la integral

from math import pi, log, tan

# Definimos la función a integrar
def f(x):
    f = log(1 + tan(x))
    return f

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

# Definimos límites de integración
a = 0
b = pi/4

# Calculamos la integral
Iold = 0.0
for k in range(1,21):
  Inew = trapecio_recursiva(f, a, b,Iold,k)
  if (k > 1) and (abs(Inew - Iold)) < 1.0e-6: break
  Iold = Inew

print('Integral =',Inew)
print('n Panels =',2**(k-1))


# In[ ]:




