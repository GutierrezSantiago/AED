__author__ = "Santiago Gutierrez"


def promedio(n, d):
    if d == 0:
        return None
    else:
        prom_crudo = n/d
        promedio = round(prom_crudo, 2)
    return promedio


def test():
    n = -1
    longitud_orbita_n = 0
    orbita_de_n = ()
    sum_orbita = 0
    ant = 0

    while n <= 0:
        n = int(input("Ingrese un número entero positivo: "))
        if n <= 0:
            print("Ingreso un numero negativo, por favor ingrese un número positivo.\n")
    while n != 1:
        sum_orbita += n
        orbita_de_n += n,
        longitud_orbita_n += 1
        if longitud_orbita_n == 1 or n >= may_orbita:
            may_orbita = n
        if n % 2 == 1:
            n = 3*n + 1
        else:
            n /= 2
    else:
        sum_orbita += n
        orbita_de_n += n,
        longitud_orbita_n += 1


    prom = promedio(sum_orbita, longitud_orbita_n)

    print("n = ", orbita_de_n[0])
    print("Orbita de n = ", orbita_de_n)
    print("Longitud de la órbita: ", longitud_orbita_n)
    print("Promedio de todos los valores de la órbita: ", prom)
    print("Mayor de los números en esa orbita:", may_orbita)

if __name__ == "__main__":
    test()




