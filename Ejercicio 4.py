# Autor: Luis Mario Ruelas Heras
# Ejercicio 4.  Analisis Numerico

# Importar NumPy para poder utilizar funciones con numeros complejos.
from numpy.lib.scimath import *

# Considera que las raices de f(z) = az² + bz + c se obtienen de

# z = (-b ± sqrt(b**2 - 4*a*c)) / (2*a)
 
# Elabora un programa en el que uses Numpy para calcular el valor de las raices
# con diferentes valores dados de a, b y c, para obtener ejemplos de raices
# reales y complejas.

# Dar valores a a, b y c.
a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
c = float(input('Ingrese el valor de c: '))

# Una ecuacion cuadratica tiene dos soluciones, que son las sigiuentes:
z_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
z_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

# Mostrar las raices
print(f'Las raices para una ecuacion cuadratica con a = {a}, b = {b} y c = {c}, son:')
print(f'z_1 = {z_1}')
print(f'z_2 = {z_2}')