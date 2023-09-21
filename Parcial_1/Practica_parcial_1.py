#=================================EJERCICIO 1====================================
'''Desarrolle un programa completo en Python, sin usar funciones predefinidas
min() y max(), que permita cargar por teclado 3 valores (3 números reales).
Si el primer valor ingresado es Par, determinar y mostrar el mayor y menor
entre el segundo y tercer valor ingresado. Caso contrario, determinar y
mostrar el mayor y menor entre el primer y segundo valor ingresado. Además,
calcular y mostrar el promedio entre el mayor y el menor.
'''

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 % 2 == 0:
    if n2 > n3:
        may = n2
        men = n3
    else:
        may = n3
        men = n2
else:
    if n1 > n2:
        may = n1
        men = n2
    else:
        may = n2
        men = n1

promedio = (may+men) / 2

print("El mayor es: ", may)
print("El menor es: ", men)
print("El promedio entre el mayor y el menor: ", promedio)
