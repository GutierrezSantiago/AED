import pickle
import os.path


class Profesional():
    def __init__(self, dni, nom, imp, afil, trab):
        self.dni = dni
        self.nombre = nom
        self.importe = imp
        self.afiliacion = afil
        self.trabajo = trab


def to_string(prof):
    r = "DNI: " + str(prof.dni)
    r += "Nombre: " + prof.nombre
    r += "Importe: $" + str(prof.importe)
    r += "Tipo de adiliación: " + str(prof.afiliacion)
    r += "Tipo de trabajo: " + str(prof.trabajo)

    return r

def display_all(v):
    print("{:*^79}".format("Profesionales del colegio"))
    for i in range(len(v)):
        print(to_string(v[i]))


def validate(inf, mensaje, error, type=0):
    n = inf - 1
    while n <= inf:
        if type == 0:
            n = int(input(mensaje))
        else:
            n = float(input(mensaje))
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


def add_in_order_dni(v, prof):
    izq, der = 0, len(v) - 1
    while izq < der:
        c = (izq + der) // 2
        if prof.dni == v[c].dni:
            pos = c
            break
        if prof.dni > v[c].dni:
            izq = c + 1
        else:
            der = c - 1

    if izq >= der:
        pos = izq

    v[pos:pos] = [prof]


def crear_vector(n):
    v = []
    print("{:^60}".format("Ingrese los datos de un profesional:"))
    for i in range(n):
        if i != 0:
            print("{:^60}".format("Ingrese el siguiente profesional: "))
        dni = int(input("Ingrese el DNI: "))
        nom = input("Ingrese el nombre: ")
        imp = validate(0, "Ingrese el importe que paga el colegio por mes: ",
                       "Recuerde que debe ser un número mayor a 0.", 1)
        afil = validate_range(0, 4, "Ingrese el tipo de afiliación: ",
                              "Recuerde que debe ser un número entre 0 y 4 "
                              "inclusive.")
        trab = validate_range(0, 14, "Ingrese el tipo de trabajo que desempeña: ",
                              "Recuerde que debe ser un número entre 0 y 14 "
                              "inclusive.")
        prof = Profesional(dni, nom, imp, afil, trab)
        add_in_order_dni(v, prof)

    return v


def opcion1():
    n = validate(0, "Ingrese la cantidad de profesional a ingresar: ",
                 "Recuerde que debe ser un número mayor a 0.")
    v = crear_vector(n)

    return v


def opcion2(v):
    display_all(v)


def crear_archivo(v, x, FD):
    m = open(FD, "wb")
    for i in range(len(v)):
        if v[i].trabajo >= 3 and v[i].trabajo <= 5 and v[i].importe > x:
            pickle.dump(v[i], m)

    m.close()


def opcion3(v):
    x = float(input("Ingrese el importe mensual X para crear el archivo: "))
    FD = input("Ingrese el nombre del archivo a crear: ")
    crear_archivo(v, x, FD)

    return FD, x


def mostrar_archivo(FD, x):
    if FD == "":
        print("El archivo todavia no fue creado.")
    else:
        m = open(FD, "rb")
        tsize = os.path.getsize(FD)
        print("Profesionales del colegio que desempeñan el tipo de trabajo 3, "
              "4 o 5 y su \nimporte es mayor a $", x, ".")
        while m.tell() < tsize:
            prof = pickle.load(m)
            print(to_string(prof))


def opcion4(FD, x):
    mostrar_archivo(FD, x)


def buscar_nom(v, nom):
    for i in range(len(v)):
        if nom.lower() == (v[i].nombre).lower():
            return i

    return -1


def opcion5(v):
    nom = input("Ingrese el nombre a buscar entre los profesionales del "
                "colegio: ")
    i = buscar_nom(v, nom)
    if i == -1:
        print("No hay ningun profesional en el colegio bajo ese nombre.")
    else:
        print("Se encontro un profesional bajo ese nombre: ")
        print(to_string(v[i]))


def matriz_conteo(v):
    mat = [[0] * 15 for f in range(5)]
    for i in range(len(v)):
        mat[v[i].afiliacion][v[i].trabajo] += 1

    return mat


def mostrar_res_conteo(mat):
    print("Tipo de afiliación | Tipo de Trabajo | Cantidad de profesionales")
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[f][c] != 0:
                print(("{:^18}".format(str(f))) + " | " +
                      ("{:^15}".format(str(c))) + " | " +
                      ("{:^25}".format(str(mat[f][c]))))


def opcion6(v):
    mat = matriz_conteo(v)
    mostrar_res_conteo(mat)


def menu_de_opciones():
    op = -1
    FD = ""
    x = 0
    while op != 7:
        print("{:*^79}".format("Menu de opciones"))
        print("\t1 - Cargar los datos de los profesionales en un arreglo.")
        print("\t2 - Mostrar los datos de los profesionales.")
        print("\t3 - Crear un archivo con los profesionales de trabajo 3, 4 o "
              "5 y con un \n\timporte mayor a X que se carga por teclado.")
        print("\t4 - Mostrar el archivo creado mediante la opcion 3.")
        print("\t5 - Buscar en el arreglo de vectores un profesional cuyo "
              "nombre sea igual \n\ta uno cargado por teclado..")
        print("\t6 - Determinar la cantidad de profesionales de cada tipo de "
              "afiliación por \n\tcada posible tipo de trabajo.")
        print("\t7 - Salir del menu de opciones")
        print(("*" * 79) + "\n")

        op = validate_range(1, 7, "Ingrese una opción a realizar: ",
                            "Ingrese una opción valida.")
        if op == 1:
            print("-" * 79)
            v = opcion1()
        elif op == 2:
            print("-" * 79)
            opcion2(v)
        elif op == 3:
            print("-" * 79)
            FD, x = opcion3(v)
        elif op == 4:
            print("-" * 79)
            opcion4(FD, x)
        elif op == 5:
            print("-" * 79)
            opcion5(v)
            print("-" * 79)
        elif op == 6:
            opcion6(v)
        input("\n\t>Presione enter para continuar...")
        print("-" * 79)

if __name__ == "__main__":
    menu_de_opciones()
