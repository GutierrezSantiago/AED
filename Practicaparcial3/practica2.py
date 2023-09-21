"""
Enunciado:
Un comercio dedicado a la Venta de Artículos Deportivos necesita un programa para conocer algunas estadísticas de su inventario.
Por cada artículo a la venta se tienen los siguientes datos: el número de identificación del artículo,
    la descripción del articulo, el costo y un numero de 1 a 15 que identifica el deporte asociado al artículo (1 - Rugby,
    2 - Basquet, 3 - Futbol, 4 Hockey, etc). Se desea almacenar la información referida a los n Artículos en un
    arreglo de registros de tipo Artículo (definir el tipo Artículo y cargar n por teclado).
Se pide desarrollar un programa en Python controlado por un menú de opciones,  que permita gestionar las siguientes tareas:
    1- Cargar el arreglo pedido con los datos de los n artículos. Valide que el número identificador del artículo sea
        positivo y que el costo del mismo sea mayor a cero. Puede hacer la carga en forma manual, o puede generar los
        datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea.
        Pero al menos una debe programar.
    2- Mostrar todos los datos de todos los artículos, en un listado ordenado de menor a mayor por número de identificación.
    3- Mostrar los datos de los equipos alquilados cuyo costo sea mayor a un valor c que se carga por teclado e informar
        el costo promedio de los artículos mostrados.
        Si no hay ningún artículo que cumpla esta condición, muestre un mensaje de la forma: "Ningún artículo supera el
        costo ingresado".
    4- Determinar si existe un artículo cuya descripción sea igual a d, siendo d un valor que se cargan por teclado.
        Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida
        con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
    5- Determinar el costo acumulado de todos los artículos por deporte asociado, filtrar en el resultado los deportes de
        los que no existen artículos a la venta.

"""
class Articulo():
    def __init__(self, numero, desc, costo, dep):
        self.numero = numero
        self.descripcion = desc
        self.costo = costo
        self.deporte = dep


def validate(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Recuerde que el número debe ser mayor a", inf)

    return n


def validate_range(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Recuerde que el número ingresado debe estar entre ", inf, " y ", sup, ".")

    return n

def to_string(articulo):
    r = ""
    r += "Número: " + str(articulo.numero) + " - "
    r += "Descripción: " + articulo.descripcion + " - "
    r += "Costo: $" + str(articulo.costo) + " - "
    r += "Deporte: " + str(articulo.deporte)

    return r


def display_all(v):
    for i in range(len(v)):
        print(to_string(v[i]))


def read(v):
    for i in range(len(v)):
        print("{:<30}".format("\t> Para el artículo nº " + str(i+1)))
        numero = validate(0, "Ingrese el número de identificación (Mayor a 0): ")
        desc = input("Ingrese la la descripción: ")
        costo = validate(0, "Ingrese el costo: ")
        dep = validate_range(1, 15, "Ingrese el identificador de deporte: ")

        v[i] = Articulo(numero, desc, costo, dep)


def shell_sort_numero(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3*h + 1

    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y.numero < v[k].numero:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3


def promedio(n, d):
    if d != 0:
        return n / d
    return None


def buscar_c(v, c):
    r = ""
    n = d = 0
    for i in range(len(v)):
        if v[i].costo > c:
            r += to_string(v[i]) + "\n"
            n += v[i].costo
            d += 1

    return r, promedio(n, d)


def buscar_d(v, d):
    for i in range(len(v)):
        if v[i].descripcion == d:
            res = to_string(v[i])
            return res


def costo_deporte(v):
    acum = [0] * 15
    for i in range(len(v)):
        acum[v[i].deporte-1] += v[i].costo

    return acum


def string_costo_deporte(acum):
    r = "Deporte | Coste acumulado\n"
    for i in range(len(acum)):
        if acum[i] != 0:
            r += "{:^7}".format(str(i+1))
            r += "{:<}".format(" | ")
            r += "{:^15}".format("$" + (str(acum[i]) + "\n"))


def opcion1():
    n = validate(0, "Ingrese la cantidad de artículos: ")
    v = [None] * n
    print("-" * 79)
    read(v)
    print("-" * 79)

    return v


def opcion2(v):
    if v is None:
        print("No hay vector cargado")
    else:
        shell_sort_numero(v)
        display_all(v)


def opcion3(v):
    if v is None:
        print("No hay vector cargado")
    else:
        c = int(input("Ingrese el costo 'c': "))
        r, promedio = buscar_c(v, c)
        if r == "":
            print("No hay ningun articulo con costo mayor a ", c)
        else:
            print(r)
            print("Promedio de los articulos mostrados: $", promedio)


def opcion4(v):
    if v is None:
        print("No hay vector cargado")
    else:
        d = int(input("Ingrese la descripción 'd': "))
        articulo = buscar_d(v, d)
        if articulo == "":
            print("No hay ningun artículo con esa descripción.")
        else:
            print("El primer articulo cuya descripcion coincide con ", d," es:")
            print(articulo)


def opcion5(v):
    if v is None:
        print("No hay vector cargado")
    else:
        acum = costo_deporte(v)
        print(string_costo_deporte(acum))


def menu():
    op = -1
    v = None
    mensaje = "{:^79}".format("*" * 31 + "") + "\n"\
              "{:^79}".format("* Menu de Manejo de Artículos *") + "\n"\
              "{:^79}".format("*" * 31 + "") + "\n" + ("-" * 79) + "\n" +\
              "{:<79}".format("\t1 - Cargar arreglo de articulos.") + "\n"\
              "{:<79}".format("\t2 - Mostrar los artículos ordenados por nº de"
                              " identificación.") + "\n" + \
              "{:<79}".format("\t3 - Mostrar los datos de los equipos alquilados"
                              " cuyo costo sea mayor a \n\tun valor c que se carga "
                              "por teclado e informar el costo promedio de los \n\t"
                              "artículos mostrados.") + "\n" + \
              "{:<79}".format("\t4 - Determinar si existe un artículo cuya "
                              "descripción sea \n\tigual a d, siendo d un "
                              "valor que se cargan por teclado.") + "\n" + \
              "{:<79}".format("\t5 - Mostrar el costo acumulado de todos "
                              "los artículos por deporte asociado.") + "\n" + \
              "{:<79}".format("\t6 - Salir del menu de opciones") + "\n" + ("-" * 79)
    while op != 6:
        print(mensaje)
        op = validate_range(1, 6, "Ingrese una opción a realizar: ")
        print("-" * 79)
        if op == 1:
            v = opcion1()
        elif op == 2:
            opcion2(v)
        elif op == 3:
            opcion3(v)
        elif op == 4:
            opcion4(v)
        elif op == 5:
            opcion5(v)
        input("Presione enter para continuar...")
        print("-" * 79)

if __name__ == "__main__":
    menu()
