"""
Una empresa de venta de automóviles mantiene información sobre los distintos vehículos que tiene a la venta.
 Por cada vehículo se registran los datos siguientes: número de identificación (un entero), nombre del vehículo
 (una cadena), cantidad en stock (puede ser cero), pais de origen del vehículo (un valor entre 0 y 19 incluidos,
  por ejemplo: 0: Argentina, 1: Brasil, etc.) y tipo de vehículo (un número entero entre 0 y 9 incluidos, para
  indicar (por ejemplo): 0: camioneta, 1: sedán, etc.) Se pide definir un tipo registro Vehículo con los campos
   que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Vehículo en un arreglo de registros (cargue n por teclado).
 Valide que el stock y el pais de origen estén dentro de los valores descriptos. Puede cargar los datos manualmente,
  o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual, y si la hace automática
   entonces TODA debe ser automática). El arreglo debe crearse de forma que siempre quede ordenado de menor a mayor,
   según el nombre de los vehículos, y para hacer esto debe aplicar el algoritmo de inserción ordenada con
   búsqueda binaria. Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y
   ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.

2- Mostrar el arreglo creado en el punto 1, a razón de  un registro por línea.

3- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación sea igual a
num (cargar num por teclado).  Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe,
 informar con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.

4- Usando el arreglo creado en el punto 1, determine la cantidad de vehículos de cada posible pais de origen por
cada posible tipo (o sea, 20 * 10 = 200 contadores en una matriz de conteo). Muestre sólo los resultados diferentes de 0.

5- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los registros cuyo
origen no sea 6 ni 5.

6- Mostrar el archivo creado en el punto anterior, a razón de un registro por línea en la pantalla, peor muestre
solo losq registros cuya cantidad en stock es diferente de cero.
"""
import pickle
import os.path


class Vehiculo():
    def __init__(self, ident, nom, stock, pais, tipo):
        self.ident = ident
        self.nombre = nom
        self.stock = stock
        self.pais = pais
        self.tipo = tipo


def to_string(vehiculo):
    r = "ID: " + str(vehiculo.ident)
    r += " | Nombre: " + vehiculo.nombre
    r += " | Stock: " + str(vehiculo.stock)
    r += " | Pais de origen: " + str(vehiculo.pais)
    r += " | Tipo de vehiculo: " + str(vehiculo.tipo)

    return r


def display_all(v):
    for i in range(len(v)):
        print(to_string(v[i]))


def validate(inf, mensaje, error):
    n = inf - 1
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(error)

    return n


def validate_range(inf, sup, mensaje, error):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print(error)

    return n


def add_in_order_nom(v, vehiculo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].nombre == vehiculo.nombre:
            pos = c
            break
        if v[c].nombre > vehiculo.nombre:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [vehiculo]


def cargar_arreglo(n):
    v = []
    print("\tCargue los datos para cada Vehiculo:")
    for i in range(n):
        if i != 0:
            print("-" * 79)
            print("\tCargue el siguiente vehiculo:")
        ident = int(input(">Ingrese el número de identificacion: "))
        nom = input(">Ingrese el nombre: ")
        stock = validate(-0.1, ">Ingrese su cantidad en stock: ",
                         "-Recuerde que debe ser mayor o igual a 0-")
        pais = validate_range(0, 19, ">Ingrese el valor que representa el país "
                                     "de origen: ", "-Recuerde que es un número "
                                                    "entre 0 y 19 incluidos-")
        tipo = int(input(">Ingrese el valor que representa el tipo de vehiculo: "))
        vehiculo = Vehiculo(ident, nom, stock, pais, tipo)
        add_in_order_nom(v, vehiculo)

    return v


def opcion1():
    n = validate(0, "Ingrese la cantidad de vehiculos a ingresar: ",
                 "-Recuerde que debe ser un número mayor a 0-")
    v = cargar_arreglo(n)

    return v


def opcion2(v):
    display_all(v)


def buscar_ident(v, num):
    for i in range(len(v)):
        if v[i].ident == num:
            return i

    return -1


def opcion3(v):
    num = int(input("Ingrese el número de identificación a buscar: "))
    print("-" * 79)
    i = buscar_ident(v, num)
    if i == -1:
        print("No se encontraron registros con ese número de identificación.")
    else:
        print("Se encontro un registro con el numero de identificación", num, ".")
        print(to_string(v[i]))


def mat_conteo(v):
    mat = [[0] * 10 for f in range(20)]
    for i in range(len(v)):
        mat[v[i].pais][v[i].tipo] += 1

    return mat


def mostrar_pais_tipo(mat):
    print("Pais de origen | Tipo de vehiculo | Cantidad de vehiculos")
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[f][c] != 0:
                print("{:^14}".format(str(f)) + " | " +
                      "{:^16}".format(str(c)) + " | " +
                      "{:^21}".format(str(mat[f][c])))


def opcion4(v):
    mat = mat_conteo(v)
    mostrar_pais_tipo(mat)


def crear_archivo(v, FD):
    m = open(FD, "wb")
    for i in range(len(v)):
        if v[i].pais != 5 and v[i].pais != 6:
            pickle.dump(v[i], m)

    m.close()


def opcion5(v):
    FD = input("Ingrese el nombre del archivo de registros a crear: ")
    crear_archivo(v, FD)
    print("El archivo de registros fue creado.")


def mostrar_archivo(FD):
    m = open(FD, "rb")
    tsize = os.path.getsize(FD)
    while m.tell() < tsize:
        vehiculo = pickle.load(m)
        if vehiculo.stock != 0:
            print(to_string(vehiculo))

    m.close()


def opcion6():
    FD = input("Ingrese el nombre del archivo a mostrar: ")
    if os.path.exists(FD):
        mostrar_archivo(FD)
    else:
        print("El archivo no fue creado todavia.")


def menu_de_opciones():
    menu = "{:*^79}".format("Menu de opciones") + "\n" + \
           "\t1 - Cargar los vehiculos en un arreglo." + "\n" + \
           "\t2 - Mostrar el arreglo creado mediante la opcion 1." + "\n" + \
           "\t3 - Buscar un registro que tenga un número de identificación " \
           "igual a uno \n\tcargado por teclado." + "\n" + \
           "\t4 - Determinar y mostrar la cantidad de vehiculos de cada " \
           "posible pais de \n\torigen por cada posible tipo." + "\n" + \
           "\t5 - Crear un archivo a partir del arreglo sin incluir a los " \
           "registros cuyo \n\tpais de origen sea 5 o 6." + "\n" + \
           "\t6 - Mostrar los registros del archivo creado en la opcion 5 cuyo" \
           " stock sea\n\t diferente de cero." + "\n" + \
           "\t7 - Salir del menu de opciones." + "\n" + ("*" * 79) + "\n"

    v = None
    op = -1
    while op != 7:
        print(menu)
        op = validate_range(1, 7, "Ingrese la opción a realizar: ", "-Ingrese una opcion valida-")
        print("-" * 79)
        if op == 1:
            v = opcion1()
        elif op == 2:
            if v == None:
                print("No se han cargado vehiculos en el arreglo.")
            else:
                opcion2(v)
        elif op == 3:
            if v == None:
                print("No se han cargado vehiculos en el arreglo.")
            else:
                opcion3(v)
        elif op == 4:
            if v == None:
                print("No se han cargado vehiculos en el arreglo.")
            else:
                opcion4(v)
        elif op == 5:
            if v == None:
                print("No se han cargado vehiculos en el arreglo.")
            else:
                opcion5(v)
        elif op == 6:
            opcion6()

        if op != 7:
            input("\n>Presione enter para continuar...")
            print("-" * 79)


if __name__ == "__main__":
    menu_de_opciones()

