"""Funciones para el manejo de un sistema de gestion de una competencia
mundial.

Lista de funciones incluidas:
:validate_range(inf, may, mensaje): Valida que un numero se encuentre en un rango
:opcion1(v): Muestra un vector de registros
:opcion2(v): Busca y muestra los paises con la mayor cantidad de campeonatos
ganados
:opcion3(v): Determina y muestra la cantidad de paises que ganaron un
campeonato por confederacion
:opcion4(v): Crea un archivo binario con los registros de una confederacion
:opcion5(v): Determina si existe un archivo binario de una confederacion y lo
 muestra
:opcion6(v): Genera el fixture para el proximo mundial
:opcion7(mat): Busca en el fixture un pais y muestra el grupo al que pertenece
:menu_de_opciones(): Maneja el menu de opciones del sistema de gestion de una
competencia mundial
"""

import registros_equipo
import manejo_de_archivos
import manejo_de_fixture

def validate_range(inf, may, mensaje):
    """Valida que el numero ingresado se encuentre dentro del rango
    ingresado por parametros.

    :param inf: El limite inferior del rango
    :param may: El limite superior del rango
    :param mensaje: El mensaje a mostrar por pantalla en el input
    :return: El valor validado dentro del rango especificado
    """
    n = -1
    while n < inf or n > may:
        n = int(input(mensaje))
        if n < inf or n > may:
            print("Recuerde que el número debe estar entre", inf, "y", may, ".")

    return n


def opcion1(v):
    """Utiliza la funcion display_all(v) para procesar el vector de registros
    e imprimirlo en pantalla.

    :param v: El vector de registros
    """
    registros_equipo.display_all(v)


def opcion2(v):
    """Busca los paises con mayor cantidad de campeonatos ganados y los muestra
    por pantalla.

    :param v: El vector de registros Equipo donde se buscaran dichos paises
    """
    pos_mayor_t = registros_equipo.mayor_camp_ganados(v)
    registros_equipo.mostrar_mayor_camp_ganados(v, pos_mayor_t)


def opcion3(v):
    """Determina y muestra la cantidad de paises que ganaron algun campeonato
    por confederacion.

    :param v: El vector de registros Equipo
    """
    cont = registros_equipo.conf_ganados(v)
    registros_equipo.muestra_conf_ganados(cont)


def opcion4(v):
    """Crea un archivo binario con los registros de una confederacion
    ingresada por teclado.

    :param v: El vector de registros Equipo
    """
    x = validate_range(0, 5, "Ingrese un codigo de confederación para generar "
                             "el vector de esa confederación: ")
    w = registros_equipo.generador_confX(v, x)
    cant = len(w)
    FD = manejo_de_archivos.generar_archivo_confederacion(w, x)
    print("-" * 79)
    print("Nombre del archivo binario creado: ", FD)
    print("Cantidad de registros que contiene el archivo: ", cant)


def opcion5(v):
    """Busca un archivo binario y lo muestra. Si este archivo no existe, crea
    uno y avisa por pantalla.

    """
    x = validate_range(0, 5, "Ingrese un codigo de confederación para generar "
                             "el vector de esa confederación: ")
    f = manejo_de_archivos.buscar_archivo_confederacion(v, x)
    if not f:
        print("No habia ningun archivo de esa confederación. Se genero un "
              "archivo binario \n correspondiente a esa confederación.")


def opcion6(v):
    """Genera la matriz con el fixture del proximo mundial y la muestra
    por pantalla.

    :param v: El vector de registros Equipo
    :return: La matriz con el fixture
    """
    w = manejo_de_fixture.contenido_mat(v)
    mat = manejo_de_fixture.generar_fixture(w)
    r = manejo_de_fixture.mostrar_fixture(mat)
    print(r)

    return mat


def opcion7(mat):
    """Busca en una matriz un pais ingresado por teclado y muestra a que
    grupo pertenece y si no existe lo informa.

    :param mat: La matriz donde se buscara el pais ingresado por teclado
    """
    if mat is None:
        print("No se puede procesar la solicitud. El fixture no se encuantra"
              " generado.")
    else:
        x = manejo_de_fixture.validador_pais("Ingrese el país a buscar en el "
                                             "fixture: ", "Recuerde ingresar "
                                                          "un país existente.")
        c = manejo_de_fixture.buscar_fixture(mat, x)
        if c == -1:
            print("El pais no se encuentra en el fixture.")
        else:
            manejo_de_fixture.mostrar_grupo(x, c)


def menu_de_opciones():
    """Maneja el menu de opciones del sistema de gestión de competencia
    mundial.

    """
    mat = None
    v = manejo_de_archivos.generar_vector_equipos("paises.csv")
    menu = "{:*^79}".format(" Menu de opciones ") + "\n" + \
           "{:<79}".format("\t1. Mostrar el listado completo de paises.") + "\n"\
           "{:<79}".format("\t2. Mostrar el o los paises con mayor cantidad de"
                           " campeonatos ganados.") + "\n" + \
           "{:<79}".format("\t3. Determinar la cantidad de paises que ganaron "
                           "algun campeonato por \n\tconfederacion.") + "\n" + \
           "{:<79}".format("\t4. Generar un archivo binario que contenga un "
                           "vector con los paises de una \n\tconfederación X "
                           "que se ingresa por teclado.") + "\n" + \
           "{:<79}".format("\t5. Ingresar una confederación por teclado y "
                           "buscar su archivo de \n\tclasificación.") + "\n" + \
           "{:<79}".format("\t6. Generar el fixture del proximo mundial y "
                           "mostrarlo por pantalla.") + "\n" + \
           "{:<79}".format("\t7. Buscar en el fixture un país ingresado por "
                           "teclado.") + "\n" + \
           "{:<79}".format("\t8. Salir del menu de opciones.") + "\n"

    op = -4
    while op != 8:
        print(menu)
        op = validate_range(0,8, "Ingrese la opción que desee ejecutar: ")
        if op == 1:
            print("-" * 79)
            opcion1(v)
            print("-" * 79)
            input(" >Presione enter para continuar...")
        elif op == 2:
            print("-" * 79)
            opcion2(v)
            print("-" * 79)
            input(" >Presione enter para continuar...")
        elif op == 3:
            print("-" * 79)
            opcion3(v)
            print("-" * 79)
            input(" >Presione enter para continuar...")
        elif op == 4:
            print("-" * 79)
            opcion4(v)
            print("-" * 79)
            input(" >Presione enter para continuar...")
        elif op == 5:
            print("-" * 79)
            opcion5(v)
            print("-" * 79)
            input(" >Presione enter para continuar...")
        elif op == 6:
            print("-" * 79)
            mat = opcion6(v)
            print("-" * 79)
            input(" >Presione enter para continuar...")
        elif op == 7:
            print("-" * 79)
            opcion7(mat)
            print("-" * 79)
            input(" >Presione enter para continuar...")
        print("-" * 79)

if __name__ == "__main__":
    menu_de_opciones()
