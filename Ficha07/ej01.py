# Problema 18
# Titulo
print("-" * 70)
print(" "*18 + "Programa para calculo de factorial" + " "*18)
print("-" * 70)
factorial = 1
n = int(input("Ingrese el número cuyo factorial quiere saber: "))

for i in range(1, n+1):
    factorial *= i
print("El factorial de ", n, " es igual a ", factorial)
