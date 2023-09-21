"""Funciones para el manejo de registros Equipo y Equipo_conf.

Lista de funciones incluidas:
:to_string_equipo(equipo): Retorna un string con los datos del registro tipo
Equipo
:to_string_equipo_conf(equipo): Retorna un string con los datos del registro
tipo Equipo_conf
:display_all(v, o=0): Muestra todos los registros de un vector de registros
:add_in_order(v, equipo): Agrega al vector un registro Equipo manteniendo su
orden descendiente por puntos.
:mayor_camp_ganados(v): Retorna las posiciones de los paises con mayor cantidad
 de campeonatos ganados
:mostrar_mayor_camp_ganados(v, pos_mayor_t): Muestra los paises con mayor
cantidad de campeonatos ganados
:conf_ganados(v): Retorna un vector de conteo con la cantidad de paises que
ganaron un campeonato por confederacion
:muestra_conf_ganados(cont): Muestra la cantidad de paises que ganaron al
menos un campeonato por confederacion
:generador_confX(v, x): Retorna un vector de registros Equipo_conf
"""

class Equipo():
    def __init__(self, conf, nom, puntos, camp):
        """
        :param conf: El valor de 0 a 5 que representa la confederación
        :param nom: Nombre del país
        :param puntos: Puntos de rankin de ese país
        :param camp: Cantidad de campeonatos ganados por ese país
        """
        self.conf = conf
        self.nom = nom
        self.puntos = puntos
        self.camp = camp


class Equipo_conf():
    def __init__(self, nom, puntos, camp):
        """
        :param nom: Nombre del país
        :param puntos: Puntos de rankin de ese país
        :param camp: Cantidad de campeonatos ganados por ese país
        """
        self.nom = nom
        self.puntos = puntos
        self.camp = camp


def to_string_equipo(equipo):
    """Convierte los datos del registro en un string.

    :param equipo: El registro equipo que se quiere convertir en string para
    poder imprimirlo
    :return: Devuelve un string de el equipo bajo el formato de presentacion
    """
    confederacion = ["UEFA", "CONMEBOL", "CONCACAF", "CAF", "AFC", "OFC"]
    st = ""
    st += "{:<23}".format("Confederación: " + confederacion[equipo.conf])
    st += "{:<56}".format(" - Descripcion del equipo:" + equipo.nom)
    st += "{:<15}".format("\nPuntos: " + str(equipo.puntos))
    st += "{:<64}".format(" - Cantidad de Campeonatos ganados: " +
                          str(equipo.camp))

    return st


def to_string_equipo_conf(equipo):
    """Convierte los datos del registro en un string.

    :param equipo: El registro equipo que se quiere convertir en string para
    poder imprimirlo
    :return: Devuelve un string de el equipo bajo el formato de presentacion
    """
    st = ""
    st += "{:<56}".format(" - Descripcion del equipo:" + equipo.nom)
    st += "{:<15}".format(" - Puntos: " + str(equipo.puntos)) + "\n"
    st += "{:^79}".format(" - Cantidad de Campeonatos ganados: " +
                          str(equipo.camp))

    return st


def display_all(v, o=0):
    """Muestra todos los equipos de un vector de registros.

    :param v: El vector de registros que contiene los equipos
    :param o: 0 para to_string_equipo(equipo) y distinto a 0 para
    to_string_equipo_conf(equipo)
    """
    print("-" * 79)
    for i in range(len(v)):
        if o == 0:
            print(to_string_equipo(v[i]))
        else:
            print(to_string_equipo_conf(v[i]))
        print("-" * 79)


def add_in_order(v, equipo):
    """Agrega el vector v el registro equipo de modo que el vector v siga
    ordenado por puntos.

    :param v: El vector ordenado por puntos
    :param equipo: El equipo a insertar en el vector
    """
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].puntos == equipo.puntos:
            pos = c
            break

        if equipo.puntos > v[c].puntos:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [equipo]


def mayor_camp_ganados(v):
    """Busca cuales son las posiciones de los equipos con la mayor cantidad de
    campeonatos ganados en el vector de registros Equipo.

    :param v: El vector de registros en el cual se va a buscar
    :return: Una lista con la posición de dichos equipos en el vector de
    registros
    """
    pos_mayor = 0
    for i in range(1, len(v)):
        if v[i].camp == v[pos_mayor].camp:
            pos_mayor_t.append(v[i])
        if v[i].camp > v[pos_mayor].camp:
            pos_mayor = i
            pos_mayor_t = [i]

    return pos_mayor_t


def mostrar_mayor_camp_ganados(v, pos_mayor_t):
    """Muestra en pantalla los paises con la mayor cantidad de campeonatos
    ganados.

    :param v: El vector de registros Equipo
    :param pos_mayor: La tupla con la posición de los equipos con mayor
    cantidad de campeonatos ganados.
    """
    if len(pos_mayor_t) == 1:
        print("El país con mayor cantidad de campeonatos ganados son: ")
    else:
        print("Los paises con mayor cantidad de campeonatos ganados son: ")
    for x in pos_mayor_t:
        print("\t>", v[x].nom)


def conf_ganados(v):
    """Genera un vector de conteo con la cantidad de paises con campeonatos
    ganados por confederacion.

    :param v: El vector de registros Equipo
    :return: El vector de conteo
    """
    cont = [0] * 6
    for i in range(len(v)):
        if v[i].camp > 0:
            cont[v[i].conf] += 1

    return cont


def muestra_conf_ganados(cont):
    """Muestra por pantalla la cantidad de paises que ganaron algun campeonato
    por confederacion.

    :param cont: El vector de conteo de paises que ganaron algun campeonato por
    confederacion
    """
    confederacion = ["UEFA", "CONMEBOL", "CONCACAF", "CAF", "AFC", "OFC"]
    print("{:^25}".format("Confederación") + "|"
          "{:^53}".format("Cantidad de países que ganaron algún campeonato"))
    for i in range(len(cont)):
        print("{:^25}".format(str(confederacion[i])) + "|"
              "{:^53}".format(str(cont[i])))


def generador_confX(v, x):
    """Genera un vector conteniendo los paises de una confederación X que se
     ingresa por teclado.

    :param v: El vector de registros Equipo del cual se generara el nuevo vector.
    :param x: El valor que representa la confederación
    :return: El vector de registros Equipo_conf con paises de la confederacion X
    """
    w = []
    for i in range(len(v)):
        if v[i].conf == x:
            equipo = Equipo_conf(v[i].nom, v[i].puntos, v[i].camp)
            add_in_order(w, equipo)

    return w
