#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Tarea 2
# Autor: Luis Mario Ruelas Heras

# Ejercicio 1. Interseccion de trayectorias.
import numpy as np

# Formar matriz con los coeficientes de las ecuaciones que describen las trayectorias
a = np.array([[2.0, -1.0, 3.0],
              [0.0, 2.0, -1.0],
              [7.0, -5.0, 0.0]])

print('La matriz de coeficientes es:\n ', a)

# Formar la matriz constante
b = np.array([[24.0], [14.0], [6.0]])
n = len(b)
print('La matriz constante es:\n ', b)

# Formar matriz aumentada
matriz_aumentada = np.concatenate((a,b), axis=1, dtype=float)
print('La matriz aumentada es :\n', matriz_aumentada)

# Funcion para resolver sistemas de ecuaciones lineales por el metodo de eliminacion de Gauss
def gaussElimin(a,b):
  # Fase de eliminacion
  for k in range(0,n-1):
    for i in range(k+1,n):
      if matriz_aumentada[i,k] != 0.0:
        lam = matriz_aumentada[i,k]/matriz_aumentada[k,k]
        matriz_aumentada[i] = matriz_aumentada[i] - lam*matriz_aumentada[k]
        b[i] = b[i] - lam*b[k]
        print(f'El siguiente elemento del procedimiento es:\n {matriz_aumentada}')
  # Fase de sustitucion hacia atras
  for k in range(n-1,-1,-1):
    b[k] = (b[k] - np.dot(matriz_aumentada[k,k+1:n],b[k+1:n]))/matriz_aumentada[k,k]
  return b

# Mostrar solucion
print('El punto de intersección es:\n',gaussElimin(a,b))


# In[2]:


# Ejercicio 2. Carga de los quarks.

# Formar matriz de coeficientes
a = np.array([[2.0, 1.0],
              [1.0, 2.0]])
print('La matriz de coeficientes es:\n ', a)

# Matriz constante
b = np.array([[1.0], [0.0]])
n = len(b)
print('La matriz constante es:\n ', b)

# Formar matriz aumentada
matriz_aumentada = np.concatenate((a,b), axis=1, dtype=float)
print('La matriz aumentada es :\n', matriz_aumentada)

# Solucionar el sistema de euaciones lineales para encontrar la carga de los quarks y mostrar la solucion
print('Las cargas de los quarks u y d son:\n',gaussElimin(a,b))


# In[4]:


# Ejercicio 3. Meteoros

# Formar matriz de coeficientes
a = np.array([[1.0, 5.0, 10.0, 20.0],
              [0.0, 1.0, -4.0, 0.0],
              [-1.0, 2.0, 0.0, 0.0],
              [1.0, 1.0, 1.0, 1.0]])
print('La matriz de coeficientes es:\n ', a)

# Formar matriz constante
b = np.array([[95.0], [0.0], [1.0], [26.0]])
n = len(b)
print('La matriz constante es:\n ', b)

# Matriz aumentada
matriz_aumentada = np.concatenate((a,b), axis=1, dtype=float)
print('La matriz aumentada es :\n', matriz_aumentada)

# Solucionar sistema de ecuaciones y mostrar la solucion
print('La cantidad de meteoros de 1kg, 5kg, 10kg y 20kg es:\n',gaussElimin(a,b), "\nrespectivamente")


# In[ ]:




