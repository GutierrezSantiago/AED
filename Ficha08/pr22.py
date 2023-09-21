# ERROR VER SOLUCION EN FICHA
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
opcion = 1

while opcion >= 1 and opcion <= 3:
    print("Cargue el número que corresponda a la opción que quiere "
      "realizar")
    print("-" * 70)
    print("1. Suma de los numeros enteros desde 1 al número ingresado")
    print("2. Factorial de un número")
    print("3. Valor de un polinomio de segundo grado en un punto X")
    opcion = int(input("¿Que opción quiere realizar?: "))

    if opcion == 1:
        suma = 0
        n = int(input("Ingrese el número del cual se quiere sacar la suma: "))
        for i in range(1, n):
            suma += i
        print("La suma de los números enteros desde 1 a ", \
                    str(n), "es igual a ", str(suma))
    elif opcion == 2:
        factorial = 1
        n = int(input("Ingrese el número del cual se quiere sacar el"
                      " factorial: "))
        for i in range(2, n):
            factorial *= i
        print("El factorial de ", str(n), "es", str(factorial))
    elif opcion == 3:
        a = int(input("Ingrese el coeficiente 'a' del polinomio de"
                      "segundo grado: "))
        b =  int(input("Ingrese el coeficiente 'b' del polinomio de"
                      "segundo grado: "))
        c = int(input("Ingrese el coeficiente 'c' del polinomio de"
                      "segundo grado: "))
        x = int(input("Ingrese el punto X del cual se quiere saber"
                      " el valor del polinomio: "))
        polinomio = (a*x**2) + b*x + c
        print("El valor del polinomio ", str(a), "x^2 + ", \
                    str(b), "x + ", str(c), " en el punto X = ",\
                    str(x), " es ", str(polinomio))
    else:
        print("El número ingresado no corresponde a ninguna opción.")
        opcion = int(input("Recuerde que las opciones validas para "
                           "ingresar son 1, 2 y 3: "))
        continue

    fin = int(input("¿Desea utilizar otra opción o repetir la elegida?"
                    " (Ingrese 0 para no, 1 para si): "))

    while fin < 1 and fin > 2:
        print("El número ingresado no corresponde a ninguna opción.")
        fin = int(input("¿Desea utilizar otra opción o repetir la "
                        "elegida? (Ingrese 0 para no,\n 1 para si): "))
    else:
        if fin == 0:
            break
        elif fin == 1:
            continue

print("El programa a finalizado.")
