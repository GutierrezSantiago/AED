class Alquiler:
    def __init__(self, ide, desc, tipo, imp, dias):
        self.identificacion = ide
        self.descripcion = desc
        self.tipo = tipo
        self.importe = imp
        self.dias = dias


def validate(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Recuerde que el número debe ser superior a ", inf, ".")
    return n


def validate_range(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Recuerde que el número debe ser un número entre ", inf,
                  " y ", sup, ".")
    return n


def read(v):
    for i in range(len(v)):
        titulo = "{:^20}".format("Alquiler nº", str(i+1))
        print(titulo)
        ide = validate(0, "Ingrese el número de identificación(Mayor a 0): ")
        desc = input("Ingrese la descripción del automóvil: ")
        tipo = validate_range(0, 9, "Ingrese el tipo de automóvil "
                                    "(Entre 0 y 9): ")
        imp = int(input("Ingrese el importe a cobrar por el alquiler: "))
        dias = int(input("Ingrese la cantidad de días por los que se hace"
                         " el alquiler: "))
        v[i] = Alquiler(ide, desc, tipo, imp, dias)


def to_string(alquiler):
    r = ""
    r += "{:<25}".format("ID de operación: ", str(alquiler.identificacion))
    r += "{:<15}".format("Tipo de auto: ", str(alquiler.tipo))
    r += "{:<15}".format("Importe: ", str(alquiler.importe))
    r += "{:<24}".format("Cantidad de días: ", str(alquiler.dias))
    r += "{:<79}".format("\nDescripción: ", alquiler.descripcion)


def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3*h + 1

    while h > 0:
        for j in range(h, n):
            y = v[j].importe
            k = j - h
            while k >= 0 and y < v[k].importe:
                v[k+h].importe = v[k].importe
                k -= h
            v[k+h].importe = y
        h //= 3


def conteo(v):
    cont = [0] * 10
    for i in range(len(v)):
        cont[v[i].tipo] += 1

    return cont


def string_cont(cont):
    r = "{:<20}".format("Tipo de vehiculo")
    r += "{:<20}".format("| Cantidad de alquileres")
    for i in range(len(v)):
        r = "{:<20}".format("\n" + str(i))
        r += "{:<20}".format("| " + str(v[i]))


def determinar(v, c, x):
    for i in range(len(v)):
        if v[i].descripcion == c and v[i].dias >= x:
            return i
    return -1


def opcion1():
    n = validate(0, "Ingrese la cantidad de alquileres: ")
    v = [None] * n
    read(v)
    return v


def opcion2(v):
    shell_sort(v)
    for i in range(len(v)):
        titulo = "{:^20}".format("Alquiler nº", str(i+1))
        print(titulo)
        print(to_string(v[i]))


def opcion3(v):
    cont = conteo(v)
    print(string_cont(cont))


def opcion4(v):
    print("Para buscar el automóvil alquilado:")
    c = input("Ingrese la descripción a: ")
    x = validate(0, "Ingrese la cantidad de dias:")
    i = determinar(v, c, x)
    if i == -1:
        print("El vehiculo ingresado no existe.")
    else:
        print("Los datos del primer automóvil alquilado con la descripción"
              " igual a \nla ingresada y los dias alquilados mayor o iguales "
              "a los ingresados son:")
        print(to_string(v[i]))


def menu_opciones():
    mensaje = "{:-^79}".format("Manejo de Alquileres") + "\n\t1 - Crear y cargar " \
               "el vector de alquileres.\n\t2 - Mostrar todos los alquileres de " \
               "menor a mayor importe a cobrar.\n\t3 - Determinar y mostrar la " \
               "cantidad de alquileres que se hicieron por cada \ntipo de automóvil" \
               "\n\t4 - Determinar si fue alquilado un vehículo con una descripcion" \
               " y una \ncantidad de días minimos cargados por teclado.\n\t5 - Salir" \
               " del menu de opciones." + "\n{:-^79}".format("")
    v = None
    op = -1
    while op != 5:
        print(mensaje)
        op = validate_range(1, 5, "Ingrese una opción a realizar: ")
    if op == 1:
        v = opcion1()
    elif op == 2:
        if v is not None:
            opcion2(v)
        else:
            print("No hay un vector cargado.")
    elif op == 3:
        if v is not None:
            opcion3(v)
        else:
            print("No hay un vector cargado.")
    elif op == 4:
        if v is not None:
            opcion4(v)
        else:
            print("No hay un vector cargado.")
        input()



if __name__ == "__main__":
    menu_opciones()
