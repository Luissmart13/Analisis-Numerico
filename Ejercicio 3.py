# Autor: Luis Mario Ruelas Heras
# Ejercicio 3.  Analisis Numerico

# =============================================================================

# 1. Considera la relacion entre el seno en variable compleja y el seno
# hiperbolico en variable real x.

# sin(ix) = i sinh(x)

# Elabora un programa que calcule el valor de sin(ix) y de sinh(x) para ciertos
# valores dados de x, para verificar la identidad.

# Importar las funciones requeridas para trabajar con numeros complejos.
from cmath import sin, cos, sinh, e 

# Input para ingresar cualquier numero complejo.
x = complex(input('Ingrese un número complejo: '))

a = sin(x * 1j) # Calcular el lado izquierdo de la igualdad.
b = 1j * sinh(x) # Calcular el lado derecho de la igualdad.

# Mostrar resultados
print(f'sin{x}i = {a}') 
print(f'i sinh{x} = {b}')
print('') # Imprimir un renglon vacio

# Comprobar que los resultados son exactamente iguales.
if a == b:
    print('La identidad se cumple.')
else:
    print('La identidad no se cumple.')
    
# =============================================================================

# 2. Considera la relacion de Euler para x real.

# e^(ix) = cos(x) + i sin(x)

# Elabora un programa que calcule el valor de cos(x), sin(x) y de e^(ix) para
# ciertos valores dados de x, para verificar la identidad.

# Utilizando el mismo numero complejo de antes.
 
eix = e**(1j * x) # Calcular el lado izquierdo de la igualdad.
identidad = cos(x) + 1j * sin(x) # Calcular el lado derecho de la igualdad.

# Mostrar ressultados
print('')
print(f'e^(ix) = {eix}')
print(f'cos(x) + i sin(x) = {identidad}')
print('')

# Comprobar que los resultados son exactamente iguales.
if eix == identidad:
    print('La identidad se cumple.')
else:
    print('La identidad no se cumple.')