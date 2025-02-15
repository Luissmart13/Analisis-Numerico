# Autor: Luis Mario Ruelas Heras
# Ejercicio 1.  Analisis Numerico
# Elabora un programa que calcule la temperatura en grados Celsius a partir de
# temperaturas conocidas (dadas) en grados Farenheit.

def far_cel(f): # Definir una funcion para convertir los grados dados en Farenheit.
    c = (f - 32) / 1.8 # Formula para convertir grados Farenheit en Celsius.
    return c  # La funcion devuelve la conversion en Celsius.

# Input para ingresar la temperatura en Farenheit
f = float(input('Ingrese la temperatura en grados Farenheit: '))

# Utilizar la funcion definida anteriormente, utilizando la variable f como argumento.
c = far_cel(f)

# Mostrar el resultado obtenido.
print(f'La temperatura en grados Celsius es: {round(c, 2)}')
# Redondeo a dos decimales para mejor visualizacion