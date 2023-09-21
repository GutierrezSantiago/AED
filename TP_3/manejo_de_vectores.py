class Participante:
    def __init__(self, nom, cont, ranking, puntaje=None):
        self.nombre = nom
        self.continente = cont
        self.ranking = ranking
        self.puntaje = puntaje


def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3*h + 1

    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while (k >= 0) and y.ranking < v[k].ranking:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3


def validate(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Recuerde que el número ingresado debe ser mayor a ", str(inf))

    return n


def validate_num(inf, sup, mensaje=("Ingrese un número dentro del rango "
                                    "establecido: ")):
    n = inf - 1
    while n < inf or n >= sup:
        n = int(input(mensaje))
        if n < inf or n >= sup:
            print("Recuerde que el número debe ser menor a " + str(sup) +
                  " y mayor o igual a " + str(inf))
    return n


def control_nombre(v, x):
    for i in range(len(v)):
        if v[i] == None:
            return -1
        if v[i].nombre == x:
            return None
    return -1


def control_ranking(v, x):
    for i in range(len(v)):
        if v[i] == None:
            return -1
        if v[i].ranking == x:
            return None
    return -1


def cont_continente(v):
    cont = [0] * 5
    for i in range(len(v)):
        cont[v[i].continente] += 1
    return cont


def display_continente(cont):
    continente = ["América", "Europa", "Asia", "Africa", "Oceanía"]
    print("{:^30}".format("Cantidad de participantes por continente"))
    for i in range(len(cont)):
        print("\t" + continente[i] + " = " + str(cont[i]))


def carga_participante(v, manual):
    if manual == 0:
        import random
        nombres = ["Agustin", "Benjamin", "Carlos", "Dominique", "Ernesto",
                   "Francisco", "Geraldine", "Hector", "Ivana", "Javier",
                   "Karen", "Maximo", "Nicole", "Omar", "Pablo", "Merlina",
                   "Rodrigo", "Santiago", "Tomas", "Ulises", "Damian", "Walter"]
        apellido = ["Laje", "Franklin", "Jimenez", "Toretto", "Guevara",
                   "Totti", "Assale", "Cordoba", "Fort", "Bueno", "Leblanc",
                    "Taier", "Gorsd", "Varela", "Gutierrez", "Campos",
                   "Gonzalez", "Da Silva", "Angeli", "Bjornson", "Moron"]
    for i in range(len(v)):
        if manual == 0:
            nom = random.choice(nombres)
            apell = random.choice(apellido)
            nombre = nom + " " + apell
            ranking = random.randrange(1, 100)
            cont = random.randrange(0, 5)
            while control_nombre(v, nombre) != -1:
                nom = random.choice(nombres)
                apell = random.choice(apellido)
                nombre = nom + " " + apell
            while control_ranking(v, ranking) != -1:
                ranking = random.randrange(1, 50)


        else:
            nombre = input("Ingrese el nombre del participante nº"
                                + str(i+1) + ": ")
            print("(0: América, 1: Europa, 2:Asia, 3: África, 4: Oceanía)")
            cont = validate_num(0, 5, "Ingrese el número correspondiente al "
                                        "continente del participante: ")
            ranking = int(input("Ingrese el ranking del participante: "))
            while control_nombre(v, nombre) != -1:
                print("El nombre ingresado esta repetido.")
                nombre = input("Ingrese el nombre del participante nº"
                            + str(i+1) + ": ")
            while control_ranking(v, ranking) != -1:
                print("El ranking ingresado esta repetido.")
                ranking = int(input("Ingrese el ranking del participante: "))

        v[i] = Participante(nombre, cont, ranking)


def to_string(participante):
    continente = ["América", "Europa", "Asia", "Africa", "Oceanía"]
    r = ""
    r += "{:<35}".format("Nombre: " + participante.nombre)
    r += "{:<20}".format("Continente: " + continente[participante.continente])
    r += "{:<15}".format("Ranking: " + str(participante.ranking))
    return r


def display_all(v):
    for x in v:
        print(to_string(x))


def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x.ranking == v[c].ranking:
            return c
        if x.ranking < v[c].ranking:
            der = c - 1
        if x.ranking > v[c].ranking:
            izq = c + 1

    return -1


def carga_orden(v, n):
    carga_participante(v, n)
    shell_sort(v)


def participantes_general(v, n):
    carga_orden(v, n)
    display_all(v)


def continentes(v):
    cont = cont_continente(v)
    display_continente(cont)


def generador_vector_enf(v, num_vector):
    enf1 = int(len(v) / 2)
    vector = [None] * enf1
    for i in range(enf1):
        if num_vector == 0:
            vector[i] = v[i]
        else:
            vector[i] = v[-i-1]

    return vector


def promedio(n, d):
    if d != 0:
        promedio = round(n/d, 2)
        return promedio


def promediar_puntaje(v1, v2):
    n = d = 0
    for i in range(len(v1)):
        n += v1[i].puntaje
        n += v2[i].puntaje
        d += 2
    return promedio(n, d)


def presentar_enfrentamientos(v1, v2, puntaje):
    import random
    for i in range(len(v1)):
        print("-" * 79)
        print(to_string(v1[i]))
        print("\t\t\tV.S.")
        print(to_string(v2[i]))
        print("-" * 79)
        if puntaje == 0:
            v1[i].puntaje = random.randrange(0, 2000)
            v2[i].puntaje = random.randrange(0, 2000)
            print("\t>Puntaje de ", v1[i].nombre, " en octavos: ", v1[i].puntaje)
            print("\t>Puntaje de ", v2[i].nombre, " en octavos: ", v2[i].puntaje)
        else:
            v1[i].puntaje = validate(0, "Ingrese el puntaje que obtuvo " + v1[i].nombre + ": ")
            v2[i].puntaje = validate(0, "Ingrese el puntaje que obtuvo " + v2[i].nombre + ": ")



def enfrentamientos(v, puntaje):
    v1 = generador_vector_enf(v, 0)
    v2 = generador_vector_enf(v, 1)
    presentar_enfrentamientos(v1, v2, puntaje)
    promedio = promediar_puntaje(v1, v2)
    return v1, v2, promedio


def competencia(v1, v2, x=0):
    vr = [None] * len(v1)
    if x != 0:
        vr2 = [None] * len(v1)
    for i in range(len(v1)):
        if v1[i].puntaje > v2[i].puntaje:
            vr[i] = v1[i]
            if x != 0:
                vr2[i] = v2[i]
        else:
            vr[i] = v2[i]
            if x != 0:
                vr2[i] = v1[i]
    if x != 0:
        return vr, vr2
    return vr


def vec_instancias(v, p, instancia, instancia2, x=0):
    print("{:*^79}".format("* " + instancia + " de final *"))
    v1, v2, promedio = enfrentamientos(v, p)
    print("-" * 79)
    print("Promedio de puntaje en " + instancia.lower() + " de final: ", promedio)
    print("-" * 79)
    if x != 0:
        v3, v4 = competencia(v1, v2, 1)
        print("{:^79}".format("Los participantes que pasaron a " + instancia2
              + " son: \n"))
        display_all(v3)
        print("-" * 79)
        print("{:^79}".format("Los participantes que disputaran el tercer "
                              "lugar son: \n"))
        display_all(v4)

        return v3, v4
    else:
        v3 = competencia(v1, v2)
        print("{:^79}".format("Los participantes que pasaron a " + instancia2
                      + " son: \n"))
        display_all(v3)

        return v3


def presentar_enf_podio(v, puntaje):
    import random
    print("-" * 79)
    print(to_string(v[0]))
    print("\t\t\tV.S.")
    print(to_string(v[1]))
    print("-" * 79)
    if puntaje == 0:
        v[0].puntaje = random.randrange(0, 2000)
        v[1].puntaje = random.randrange(0, 2000)
        print("\t>Puntaje de ", v[0].nombre, " en octavos: ", v[0].puntaje)
        print("\t>Puntaje de ", v[1].nombre, " en octavos: ", v[1].puntaje)
    else:
        v[0].puntaje = validate(0, "Ingrese el puntaje que obtuvo " + v[0].nombre + ": ")
        v[1].puntaje = validate(0, "Ingrese el puntaje que obtuvo " + v[1].nombre + ": ")


def competencia_podio(v1, v2):
    if v1[0].puntaje < v1[1].puntaje:
        campeon = v1[1]
        segundo = v1[0]
    else:
        campeon = v1[0]
        segundo = v1[1]
    if v2[0].puntaje < v2[1].puntaje:
        tercero = v2[1]
    else:
        tercero = v2[0]

    return campeon, segundo, tercero


def gen_podio(v1, v2, p):
    presentar_enf_podio(v1, p)
    presentar_enf_podio(v2, p)

    return competencia_podio(v1, v2)


def mostrar_podio(campeon, segundo, tercero):
    print("-" * 79 + "\n" + "{:^79}".format("* Podio *") + "\n" + "-"*79
          + "\n\tGanador: \n" + to_string(campeon) + "\n" + "-"*79 +
          "\n\tSegundo: \n" + to_string(segundo) + "\n" + "-"*79 +
          "\n\tTercero: \n" + to_string(tercero) +  "\n" + "-"*79)


def add_ranking(v, campeon, segundo, tercero):
    i1 = binary_search(v, campeon)
    i2 = binary_search(v, segundo)
    i3 = binary_search(v, tercero)
    v[i1].ranking += 25
    v[i2].ranking += 15
    v[i3].ranking += 5


def podio_add(v, v1, v2, p):
    campeon, segundo, tercero = gen_podio(v1, v2, p)
    mostrar_podio(campeon, segundo, tercero)
    add_ranking(v, campeon, segundo, tercero)
