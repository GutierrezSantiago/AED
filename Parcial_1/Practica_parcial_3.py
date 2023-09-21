'''Desarrolle un programa completo en Python, sin usar funciones predefinidas
min() y max(), que permita cargar por teclado 3 variables (3 valores enteros).
Si el primer valor ingresado es igual a cero, calcule y muestre
la siguiente fórmula: √ bᶟ + cᶟ .
Si el primer valor ingresado es mayor a la suma del segundo y tercer valor,
calcule y muestre el cociente entre b/c. Caso contrario, mostrar el mayor
valor entre el segundo valor ingresado y el tercero.'''

a = int(input("Ingrese un primer valor: "))
b = int(input("Ingrese un segundo valor: "))
c = int(input("Ingrese un tercer valor: "))

if a == 0:
    resultado = (b**3 + c**3) ** (1/2)
    cadena = "√ bᶟ + cᶟ = "
elif a > (b+c):
    resultado = b // c
    cadena = "El cociente entre b/c = "
else:
    if b > c:
        resultado = b
    else:
        resultado = c
    cadena = "El mayor es "

print(cadena + str(resultado))
