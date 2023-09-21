"""
n1 = int(input("Ingrese un primer número: "))
n2 = int(input("Ingrese un segundo número: "))
if n1 > n2:
    may = n1
    men = n2
else:
    may = n2
    men = n1
print("Los numeros ordenados son: ", men, may)

a = 5
b = 7
c = 1
print(a < b+c and a > c or c == 2)

#Mostrar si un número es el mayor de tres números
#Ingreso de datos
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

# Proceso
if n1 > n2 and n1 > n3:
    mensaje = "El primero es el mayor"
else:
    mensaje = "El primero no es el mayor"
print(mensaje)

import random
x = random.random()
y = int(x * 100)
print(x)
print(y)

import random
x = random.randrange(15, 48)
print(x)

import random
x = random.randint(15, 48)
print(x)

t = ("Silvio", "German", "Esteban", "Carmela")
x = random.choice(t)
print(x)

s = "Hola"
x = random.choice(s)
print(x)
"""
