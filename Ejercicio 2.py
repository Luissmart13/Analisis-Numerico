# Autor: Luis Mario Ruelas Heras
# Ejercicio 2.  Analisis Numerico
# Elabora un programa que calcule el valor de sinh(x) en x = 2π de tres diferentes maneras.

# Importar las funciones requeridas de la libreria math
from math import sinh, pi, e, exp 
# Guardar el valor de 2π en la variable x para utilizarla mas adelante facilmente.
x = 2*pi 

# 1. Evaluando sinh(x) directamente:

a = sinh(x) # Aplicar directamente la funcion sinh de math, sobre la variable x.
print(f'El seno hiperbolico de 2π es: {a}') # Mostrar el resultado

# 2. Evaluando la definicion del lado derecho, usando la funcion exponencial

# La expresion a la que se hace referencia es la siguiente
b = ( exp(x) - exp(-x) ) / 2

# Donde b seria el valor del seno hiperobilco de x.
# Ademas, utilizamos la funcion exp de la libreria math.

print(f'El seno hiperbolico de 2π es: {b}') # Mostrar el resultado

# 3. Evaluando con la definición del lado derecho, usando la potencion
# Similar a la manera anterior, pero usando el numero e, obtenido de la libreria math.

c = ( e**x - e**(-x) ) / 2

print(f'El seno hiperbolico de 2π es: {c}')

