n = int(input("Ingrese la cantidad de números a procesar: "))
may = None
for i in range(n):
    num = int(input("Ingrese un número: "))
    if i == 0 or num > may:
        may = num

print("El mayor de los números ingresados es: ", may)
