""""Una empresa de seguros pide un programa para procesar los datos de las Pólizas que están siendo administradas.
Por cada Póliza se conoce su número de identificación, el nombre del cliente, el tipo de póliza
(un valor del 0 al 19, por ejemplo: 0: Terceros, 1: Terceros Transportados, 2: Total, etc.)
 y el costo mensual de dicha poliza. Se desea almacenar la información referida a los n pólizas
 en un arreglo de registros de tipo Poliza (definir el tipo Poliza y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones,  que permita gestionar las siguientes tareas:

1. Cargar el arreglo con los datos de las n pólizas. Valide que el costo mensual de la póliza sea mayor a cero y que el
   tipo de póliza esté en el rango especificado. Puede hacer la carga en forma manual, o puede generar los datos en forma
   automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
2. Mostrar todos los datos de todas las pólizas, en un listado ordenado de mayor a menor según el nombre de los clientes.
3. Determinar la cantidad total por cada tipo de póliza que se carga en el puerto, 20 contadores en total en un vector de conteo.
4. Determinar el costo mensual promedio entre todas las pólizas del vector que sean tipo 2, 5, o 9. Muestre además los
   datos de todas las pólizas de esos tres tipos, cuyo costo mensual sea menor al promedio que acaba de calcular.
5. Determinar si existe una póliza cuya número sea igual x y tal que su costo mensual sea mayor a un valor c,
   siendo x y c dos valores que se carga por teclado. Si existe, mostrar sus datos. Si no existe, informar con un mensaje.
   Si existe mas de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre."""
from x import *
# general
class Poliza():
    def __init__(self, num, nom, tipo, costo):
        self.numero = num
        self.nombre = nom
        self.tipo = tipo
        self.costo = costo


def to_string(pol):
    r = ""
    r += "{:<39}".format("Número de ID: " + str(pol.numero))
    r += "{:<40}".format("| Nombre del cliente: " + pol.nombre)
    r += "\n"
    r += "{:<39}".format("Tipo de póliza: " + str(pol.tipo))
    r += "{:<40}".format("| Costo mensual: $" + str(pol.costo))

    return r


def display_all(v):
    print("{:^79}".format("* Pólizas *"))
    print("-" * 79)
    for i in range(len(v)):
        print(to_string(v[i]))
        print("-" * 79)


def validate(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Recuerde que el numero debe ser mayor a ", inf)

    return n


def validate_range(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Recuerde que el numero debe estar entre ", inf, " y ", sup)

    return n


def promedio(n, d):
    if d != 0:
        promedio = round(n/d, 2)
        return promedio

    return


def read(v):
    print("{:^79}".format("* Cargue las pólizas: *"))
    print("-" * 79)
    for i in range(len(v)):
        num = int(input("Ingrese el número de identificacion de la poliza: "))
        nom = input("Ingrese el nombre del cliente: ")
        tipo = validate_range(0, 19, "Ingrese el tipo de póliza: ")
        costo = validate(0, "Ingrese el costo mensual de la póliza: $")
        print("-" * 79)

        v[i] = Poliza(num, nom, tipo, costo)


def opcion1():
    n = validate(0, "Ingrese la cantidad de polizas a cargar: ")
    print("-" * 79)
    v = [None] * n
    read(v)

    return v


def shell_sort_nom(v):
    n = len(v)
    h = 1

    while h <= n // 9:
        h = 3*h + 1

    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y.nombre > v[k].nombre:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3


def opcion2(v):
    if v is not None:
        shell_sort_nom(v)
        display_all(v)
    else:
        print("No hay un vector cargado.")
        print("-" * 79)


def cantidad_por_tipo(v):
    cont = [0] * 20
    for i in range(len(v)):
        cont[v[i].tipo] += 1

    return cont


def display_cant_tipo(cont):
    print("{:^79}".format("* Cantidad de pólizas por tipo *"))
    for i in range(len(cont)):
        print("Tipo de póliza: ", i, end=" ")
        print("| Cantidad de pólizas: ", cont[i])


def opcion3(v):
    if v is not None:
        cont = cantidad_por_tipo(v)
        display_cant_tipo(cont)
    else:
        print("No hay un vector cargado.")
        print("-" * 79)

def costo_promedio_por_tipo(v, *tipo):
    costo = d = 0

    for i in range(len(v)):
        if (v[i].tipo == 2 or v[i].tipo == 5 or v[i].tipo == 9):
            costo += v[i].costo
            d += 1

    return promedio(costo, d)


def display_costo_men_promedio(v, p, *tipo):
    for i in range(len(v)):
        if (v[i].tipo == 2 or v[i].tipo == 5 or v[i].tipo == 9)\
                and v[i].costo < p:
            print(to_string(v[i]))


def opcion4(v):
    if v is not None:
        p = costo_promedio_por_tipo(v, (2, 5, 9))
        print("El costo mensual promedio entre las pólizas de tipo 2, 5 o 9 fue: ", p)
        print("-" * 79)
        print("{:<79}".format("Las pólizas de tipo 2, 5 o 9 cuyo costo mensual es "
                              "menor al promedio: "))
        print("-" * 79)
        costo(v, p, 2, 5, 9)
        print("-" * 79)
    else:
        print("No hay un vector cargado.")
        print("-" * 79)


def buscar_x_c(v, x, c):
    for i in range(len(v)):
        if x == v[i].numero and c < v[i].costo:
            return i

    return


def opcion5(v):
    if v is not None:
        print("{:^79}".format("Para la póliza a buscar: "))
        x = int(input("Ingrese el número: "))
        c = validate(0, "Ingrese el costo: $")
        i = buscar_x_c(v, x, c)
        if i is not None:
            print("Se encontró una póliza que cumple con los criterios de busqueda: ")
            print(to_string(v[i]))
        else:
            print("No se encontró una póliza que cumple con los criterios de busqueda.")
    else:
        print("No hay un vector cargado.")
        print("-" * 79)

def menu():
    v = None
    op = -1
    mensaje = "{:^79}".format("*" * 39) + "\n" + \
            "{:^79}".format("* Menu para procesar datos de pólizas *") + "\n" \
            + "{:^79}".format("*" * 39) + "\n" + \
            "\t1 - Cargar las pólizas." + "\n\t2 - Mostrar las pólizas " \
            "ordenadas de mayor a menor según el nombre de los \n\t\tclientes." + \
            "\n\t3 - Mostrar la cantidad total por tipo de póliza." + \
            "\n\t4 - Determinar el costo mensual promedio entre todas " \
            "las pólizas del vector que \n\t\tsean tipo 2, 5, o 9 y mostrar " \
            "aquellas pólizas de esos tipos que sean menor\n\t\t que el promedio." + \
            "\n\t5 - Buscar una póliza cuyo numero sea igual a 'x' y su costo " \
            "mensual mayor a \n\t\t'c', siendo 'x' y 'c' valores que se cargan por " \
            "teclado."
    while op != 6:
        print("-" * 79)
        print(mensaje)
        print("-" * 79)
        op = validate_range(1, 6, "Ingrese la opción a utilizar: ")
        print("-" * 79)
        if op == 1:
            v = opcion1()
        elif op == 2:
            opcion2(v)
        elif op == 3:
            opcion3(v)
        elif op == 4:
            opcion4(v)
        else:
            opcion5(v)
        input("Presione enter para continuar...")


if __name__ == "__main__":
    menu()
