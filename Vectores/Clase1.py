def validate(inf):
    n = inf
    while n <= inf:
        n = int(input("Ingrese el tamaño del arreglo(Mayor a " + str(inf) + "): "))
        if n <= inf:
            print("Error! Se pidió un nómero mayor a " + str(inf) + ".")
    return n


def creacion_vector(v):
    for i in range(len(v)):
        v[i] = float(input("Ingrese una altura: "))


def promedio_arreglo(v):
    cont = 0
    suma = 0
    for i in range(len(v)):
        suma += v[i]
        cont += 1
    promedio = suma / cont
    promedio = round(promedio, 2)
    return promedio

def comparar_arreglo(v, pr):
    n = len(v)
    may_pr = 0
    men_pr = 0
    for i in range(n):
        if v[i] > pr:
            may_pr += 1
        else:
            men_pr += 1
    return may_pr, men_pr

def test():
    n = validate(0)
    v = n * [0]
    creacion_vector(v)
    promedio = promedio_arreglo(v)
    mayor_promedio, menor_promedio = comparar_arreglo(v, promedio)
    print("Las alturas cargadas son: ", v)
    print("El promedio de las alturas es: ", promedio)
    print("Cantidad de alturas mayor al promedio: ", mayor_promedio)
    print("Cantidad de alturas menor al promedio: ", menor_promedio)

if __name__ == "__main__":
    test()
