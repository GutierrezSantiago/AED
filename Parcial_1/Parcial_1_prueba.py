"""
# Primer programa hecho
a = float(input("Ingrese un número: "))
b = float(input("Ingrese un número: "))

if a > b:
    may = a
else:
    may = b

print("El mayor es: ", may)
print("El cuadrado del mayor es: ", may ** 2)
print("El cubo del mayor es: ", may ** 3)

# Segundo programa hecho
pares = 0
impares = 0

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
n3 = int(input("Ingrese un número: "))

if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
    print("Los tres números son pares")
elif n1 % 2 == 1 and n2 % 2 == 1 and n3 % 2 == 1:
    print("Los tres números son impares")
else:
    print("Hay tantos números pares como impares")

# Tercer programa hecho pero erroneo ya que no piden cual es el mediano
import random

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
n3 = int(input("Ingrese un número: "))

if n1 > n2:
    may = n1
    men = n2
else:
    may = n2
    men = n2
if n3 > may
    med = may
    may = n3
elif n3 < men:
    med = men
    men = n3
else:
    med = n3

# Tercer programa correcto
import random

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))
n3 = int(input("Ingrese un número: "))

if n1 > n2 and n1 > n3:
    may = n1
    if n2 > n3:
        men = n3
    else:
        men = n2
else:
    if n2 > n3:
        may = n2
        if n1 > n3:
            men = n3
        else:
            men = n1
    else:
        may = n3
        if n1 > n2:
            men = n2
        else:
            men = n3
# Dice un numero aleatorio sin especificar, posible usar cualquier random
na = random.random()
producto = na * may

print("El mayor es: ", may)
print("El menor es: ", men)
print("El producto de el mayor con un numero generado aleatoriamente\
 es: ", producto)

# Programa probar raiz
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

r1 = n1 ** (1/2)
r2 = n2 ** (1/3)

print("Raiz de n1: ", r1)
print("Raiz de n2: ", r2)
"""
import random
a = 1
while a == 1:
    b = random.randrange(1,10)
    print(b)
