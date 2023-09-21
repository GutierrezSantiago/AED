"""Se pide desarrollar un programa que permita leer una serie de números.
La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo.
Los requerimientos funcionales del programa son:
a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.
b) Cantidad de valores pares ingresados.
c) Cantidad de valores impares ingresados.
d) Informar si en la carga de números se ingreso al menos un número 0.
e) Informar si la serie contiene solo números pares e impares alternados"""
sumatoria = 0
par = 0
impar = 0
cero = False
alternados = True
serie = int(input("Ingrese una serie de números: "))
anterior = serie
while serie >= 0:
    if serie >= 50 and serie <= 100:
        sumatoria += serie
    if serie % 2 == 0:
        par += 1
    else:
        impar += 1
    if serie == 0:
        cero = True
    serie = int(input("Ingrese otra serie de números: "))
    if anterior % 2 == serie % 2:
        alternados = False
    anterior = serie

print("La sumatoria de los números comprendidos entre 50 y 100 es: ", sumatoria)
print("La cantidad de valores pares ingresados: ", par)
print("La cantidad de valores impares ingresados: ", impar)
if cero:
    print("Al menos una serie ingresada es igual a cero(0)")
if alternados:
    print("Los valores ingresados se alternan entre par e impar.")
