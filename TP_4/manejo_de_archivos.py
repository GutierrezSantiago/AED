"""Funciones para el manejo de archivos.

Lista de funciones incluidas:
:generar_vector_equipos(FD): Crea un vector de registros desde un archivo csv
:generar_archivo_confederacion(w, x): Genera un archivo binario conteniendo registros Equipo_conf
:buscar_archivo_confederacion(v, x): Busca un archivo binario y de existir lo muestra
"""

import registros_equipo
from registros_equipo import Equipo
import pickle
import os.path

def generar_vector_equipos(FD):
    """Crea un vector de registros Equipo desde el archivo separado por comas
    cuyo nombre se ingresa como parametro.

    :param FD: El nombre del archivo del que se quieren extraer los equipos
    :return: El vector de registros Equipo
    """
    v = []
    m = open(FD, "rt")
    arch = m.readlines()
    for linea in arch:
        linea = linea.replace("\n", "")
        tokens = linea.split(",")
        equipo = Equipo(int(tokens[0]), tokens[1], int(tokens[2]), int(tokens[3]))

        registros_equipo.add_in_order(v, equipo)

    m.close()
    return v

def generar_archivo_confederacion(w, x):
    """Genera un archivo binario conteniendo registros Equipo_conf
    de los paises de la confederacion X.

    :param w: El vector de registros Equipos_conf
    :param x: El valor que representa la confederación
    :return: El nombre del archivo
    """
    FD = "clasificacion" + str(x) + ".dat"
    m = open(FD, "wb")
    for i in range(len(w)):
        pickle.dump(w[i], m)
    m.close

    return FD


def buscar_archivo_confederacion(v, x):
    """Busca un archivo binario y muestra su contenido y de no existir este
    archivo, lo crea.

    :param x: El valor que representa la confederación
    :return: True si el archivo existia, False de lo contrario
    """
    FD = "clasificacion" + str(x) + ".dat"
    f = os.path.exists(FD)
    if f:
        tsize = os.path.getsize(FD)
        m = open(FD, "rb+")
        print("-" * 79)
        while m.tell() < tsize:
            equipo = pickle.load(m)
            print(registros_equipo.to_string_equipo_conf(equipo))
            print("-" * 79)


    else:
        m = open(FD, "wb")
        w = registros_equipo.generador_confX(v, x)
        generar_archivo_confederacion(w, x)

    m.close()

    return f







