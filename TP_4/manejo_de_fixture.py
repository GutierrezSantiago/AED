"""Funciones para el manejo del fixture para el Mundial.

Lista de funciones incluidas:
:validador_pais(mensaje, error): Retorna un pais cuya existencia fue validada
:formato_nom_pais(pais): Le da formato a un string
:cabeza_de_serie(org, v): Retorna un vector con los cabeza de serie de cada
grupo
:sorteo_mej_restantes(v, w): Agrega al vector cabezas de serie los paises
restantes para completar el fixture
:contenido_mat(v): Retorna el contenido del fixture en un vector
:generar_fixture(w): Genera el fixture del mundial.
:mostrar_fixture(mat): Retorna un string con el fixture listo para mostrar
:buscar_fixture(mat, x): Busca un pais en el fixture
:mostrar_grupo(pais, c): Muestra el grupo de un pais desde el indice de
columna del fixture
"""

import random

def validador_pais(mensaje, error):
     """Valida si el país ingresado existe.

     :param mensaje: El mensaje al pedir un país por teclado
     :param error: El mensaje que se muestra si el pais no existe
     :return: país ingresado por teclado validado
     """
     v = ['afganistan', 'albania', 'alemania', 'andorra', 'angola', 'anguila',
          'antigua y barbuda', 'arabia saudi', 'argelia', 'argentina',
          'armenia', 'aruba', 'australia', 'austria', 'azerbaiyan',
          'bahamas', 'bahrein', 'bangladesh', 'barbados', 'belgica',
          'belice', 'benin', 'bermudas', 'bielorrusia', 'bolivia',
          'bosnia y herzegovina', 'botsuana', 'brasil', 'brunei darussalam',
          'bulgaria', 'burkina faso', 'burundi', 'butan', 'cabo verde',
          'camboya', 'camerun', 'canada', 'chad', 'chile', 'chinese taipei',
          'chipre', 'colombia', 'comoras', 'congo', 'costa rica', 'croacia',
          'cuba', 'curaçao', "côte d'ivoire", 'dinamarca', 'dominica',
          'ecuador', 'eeuu', 'egipto', 'el salvador',
          'emiratos arabes unidos', 'escocia', 'eslovaquia', 'eslovenia',
          'españa', 'estonia', 'esuatini', 'etiopia', 'filipinas',
          'finlandia', 'fiyi', 'francia', 'gabon', 'gales', 'gambia',
          'georgia', 'ghana', 'granada', 'grecia', 'guam', 'guatemala',
          'guinea', 'guinea ecuatorial', 'guinea-bissau', 'guyana', 'haiti',
          'honduras', 'hong kong', 'hungria', 'india', 'indonesia',
          'inglaterra', 'irak', 'irlanda del norte', 'islandia',
          'islas caiman', 'islas feroe', 'islas salomon',
          'islas virgenes britanicas', 'islas virgenes estadounidenses',
          'israel', 'italia', 'jamaica', 'japon', 'jordania', 'kazajstan',
          'kenia', 'kosovo', 'kuwait', 'laos', 'lesoto', 'letonia', 'libano',
          'liberia', 'libia', 'lituania', 'luxemburgo', 'macao',
          'macedonia del norte', 'madagascar', 'malasia', 'malaui', 'maldivas',
          'mali', 'marruecos', 'mauricio', 'mauritania', 'mexico', 'mongolia',
          'montenegro', 'montserrat', 'mozambique', 'myanmar', 'namibia',
          'nepal', 'nicaragua', 'niger', 'nigeria', 'noruega',
          'nueva caledonia', 'nueva zelanda', 'oman', 'paises bajos',
          'pakistan', 'palestina', 'panama', 'papua nueva guinea', 'paraguay',
          'peru', 'polonia', 'portugal', 'puerto rico', 'qatar', 'rd del congo',
          'rdp de corea', 'republica centroafricana', 'republica checa',
          'republica de corea', 'republica de irlanda', 'republica dominicana',
          'republica kirguisa', 'ri de iran', 'rp china', 'ruanda', 'rumania',
          'rusia', 'samoa', 'samoa estadounidense', 'san cristobal y nieves',
          'san vicente y las granadinas', 'santa lucia', 'santo tome y principe',
          'senegal', 'serbia', 'sierra leona', 'singapur', 'siria', 'sri lanka',
          'sudafrica', 'sudan', 'sudan del sur', 'suecia', 'suiza', 'surinam',
          'tahiti', 'tailandia', 'tanzania', 'tayikistan', 'timor oriental',
          'togo', 'tonga', 'trinidad y tobago', 'tunez', 'turcas y caicos',
          'turkmenistan', 'turquia', 'ucrania', 'uganda', 'uruguay', 'uzbekistan',
          'vanuatu', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabue']

     n = "aaa"

     while (n.lower() not in v):
         n = input(mensaje)
         if n.lower() not in v:
              print(error)
     return n


def formato_nom_pais(pais):
     """Le da formato a un pais para mostrarlo por pantalla.

     :param pais: El pais que va a tomar el formato
     :return: El pais bajo el formato
     """
     div = pais.split(" ")
     for i in range(len(div)):
          x = div[i]
          div[i] = x.capitalize()
     pais = " ".join(div)

     return pais


def cabeza_de_serie(org, v):
     """Define los cabeza de serie de cada grupo.

     :param org: El país organizador
     :param v: El vector de registros Equipo
     :return: Un vector con los cabeza de serie
     """
     w = [org]
     i = 0
     while len(w) != 8:
          if not(org == v[i].nom):
               w.append(v[i].nom)

          i += 1

     return w


def sorteo_mej_restantes(v, w):
     """Agrega al vector de cabezas de serie los paises restantes en cada
     grupo.

     :param v: El vector de registros Equipo
     :param w: El vector de cabezas de serie
     """
     while len(w) != 36:
          x = random.randint(0, 35)
          if not(v[x].nom in w):
               w.append(v[x].nom)


def contenido_mat(v):
     """Genera el contenido de la matriz y lo almacena en un vector.

     :param v: El vector de registros Equipo
     :return: El vector que tiene el contenido de la matriz
     """
     org = validador_pais("Ingrese el nombre del país organizador: ",
                           "Recuerde ingresar un país existente.")
     w = cabeza_de_serie(org, v)
     sorteo_mej_restantes(v, w)

     return w


def generar_fixture(w):
     """Genera el fixture del mundial.

     :param w: El vector que contiene los paises de la matriz
     :return: La matriz conteniendo el fixture del mundial
     """
     mat = [[""] * 8 for f in range(4)]
     i = 0
     for f in range(len(mat)):
          for c in range(len(mat[0])):
               mat[f][c] = w[i]
               i += 1

     return mat


def mostrar_fixture(mat):
     """Genera un string con el fixture listo para mostrar por pantalla.

     :param mat: La matriz conteniendo el fixture
     :return: Un string conteniendo el fixture
     """
     r = ("-" * 79) + "\n"
     r += "{:^18}".format("Grupo A") + "|" +  "{:^18}".format("Grupo B") + \
         "|" + "{:^18}".format("Grupo C") + "|" + "{:^18}".format("Grupo D") + \
         "\n"
     r += ("-" * 79) + "\n"
     for f in range(len(mat)):
          for c in range(4):
               if f == 0 and c == 0:
                    mat[0][0] = formato_nom_pais(mat[0][0])
               if mat[f][c] == "EspaÃ±a":
                    mat[f][c] = "España"
               if mat[f][c] == "CuraÃ§ao":
                    mat[f][c] = "Curaçao"
               if mat[f][c] == "CÃ´te d'Ivoire":
                    mat[f][c] = "Côte d'Ivoire"

               r += "{:^18}".format(mat[f][c])
               if c == 3:
                    r += "\n"
               else:
                    r += "|"
     r += ("-" * 79) + "\n"
     r += "{:^18}".format("Grupo E") + "|" +  "{:^18}".format("Grupo F") + \
         "|" + "{:^18}".format("Grupo G") + "|" + "{:^18}".format("Grupo H") + \
         "\n"
     r += ("-" * 79) + "\n"
     for f in range(len(mat)):
          for c in range(4, len(mat[0])):
               if mat[f][c] == "EspaÃ±a":
                    mat[f][c] = "España"
               if mat[f][c] == "CuraÃ§ao":
                    mat[f][c] = "Curaçao"
               if mat[f][c] == "CÃ´te d'Ivoire":
                    mat[f][c] = "Côte d'Ivoire"

               r += "{:^18}".format(mat[f][c])
               if c == 7:
                    r += "\n"
               else:
                    r += "|"


     return r


def buscar_fixture(mat, x):
     """Busca en el fixture un pais.

     :param mat: La matriz que contiene el fixture
     :param x: El pais a buscar
     :return: La columna donde se encuentra el pais o -1 si no lo encuentra
     """
     for c in range(len(mat[0])):
          for f in range(len(mat)):
               if x.lower() == mat[f][c].lower():
                    return c

     return -1


def mostrar_grupo(pais, c):
     """Muestra un mensaje con el pais y el grupo al que pertenece este.

     :param pais: Un pais
     :param c: La columna de la matriz en la que se encuentra el país
     """
     if c == 0:
          grupo = "A"
     elif c == 1:
          grupo = "B"
     elif c == 2:
          grupo = "C"
     elif c == 3:
          grupo = "D"
     elif c == 4:
          grupo = "E"
     elif c == 5:
          grupo = "F"
     elif c == 6:
          grupo = "G"
     elif c == 7:
          grupo = "H"

     print("El pais buscado (", formato_nom_pais(pais) ,") pertenece al grupo", grupo, ".")
