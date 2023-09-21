"""Desarrolle un programa completo en Python, sin usar las funciones
predefinidas min() y max(), que permita cargar por teclado la medida
de los tres lados de un triángulo. Muestre la medida del lado más
chico y luego, si los tres lados son iguales muestre el mensaje
“Triángulo Equilátero”. De lo contrario simplemente no muestre
ningún mensaje."""

# Título
print("-" * 70)
print("Programa para encontrar el lado mas chico de un triángulo y "
      "determinar\nsi el triángulo es equilátero.")
print("-" * 70)

# Iniciación de bandera
equilatero = False

# Ingreso de datos
print("Aclaración: Ingrese los datos en metros.")
print("-" * 70)
lado1 = float(input("Ingrese la medida del primer lado del triángulo: "))
lado2 = float(input("Ingrese la medida del segundo lado del triángulo: "))
lado3 = float(input("Ingrese la medida del tercer lado del triángulo: "))

# Proceso
if lado1 < lado2 and lado1 < lado3:
    lado_men = lado1
elif lado2 < lado3:
    lado_men = lado2
else:
    lado_men = lado3

if lado1 == lado2 == lado3:
    equilatero = True

# Resultado
print("-" * 70)
print("La medida del lado mas chico del triángulo es: ", lado_men)
if equilatero:
    print("Triángulo Equilátero")

input("\nPresione enter para finalizar el programa...")
