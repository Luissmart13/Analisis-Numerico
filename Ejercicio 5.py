# Autor: Luis Mario Ruelas Heras
# Ejercicio 5.  Analisis Numerico

from sympy import symbols, lambdify, tan, cos

# ¿Cual es la trayectoria de una pelota que se lanza con una rapidez inicial
# v_0 a una angulo θ medido de la horizontal?

# Sabemos que la pelota seguira una trayectoria y = f(x), donde, en ausencia
# de resistencia del aire, f(x) = x tanθ - (g/(2v_0²))(x²/cos²θ))+y_0.

# En esta expresion, x es la coordenada horizontal, g es la aceleracion de la
# gravedad y y_0 es la posicion inicial de la pelota.

# 1. En tu portafolio de clase, elabora un programaen el que evalues esta 
# expresion. El programa debe escribir el valor de todas las variables
# involucradas junto con las unidades usadas.

# Definir las variables de forma simbolica
x, θ, g, v0, y0 = symbols('x θ g v0 y0')

# Escribir la funcion
f_x = x*tan(θ) - ( g / ( 2 * v0**2 ) ) * ( x**2 / (cos(θ)**2) ) + y0

# Convertir la expresion simbolica en una funcion de Python
f = lambdify([x, θ, g, v0, y0 ], f_x)

# Definir los valores para los argumentos de la funcion. 
x_value = 2
θ_value = 2
g_value = 9.81
v0_value = 5
y0_value = 10

# Evaluar la funcion con los argumentos definidos
print ('Evaluacion:', f(x_value, θ_value, g_value, v0_value, y0_value), 'm.')

#Mostrar los valores de los argumentos, junto con sus unidades.
print(f'Valor de x: {x_value} m')
print(f'Valor de θ: {θ_value} rad')
print(f'Valor de g: {g_value} m/s²')
print(f'Valor de v0: {v0_value} m/s')
print(f'Valor de y0: {y0_value} m')