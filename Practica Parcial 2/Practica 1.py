#1 - Determinar el porcentaje de palabras que incluyeron alguna consonante.
#2 - Determinar el porcentaje de palabras que contienen 'si' y 'no'.
#3 - Determinar el porcentaje de las plabras que finalizaron en "on" sobre el total de palabras del texto.
#4 - Determinar la cantidad de palabras que comienzan con 'le' y terminan en 'to'.
def es_consonante(c):
    consonante = "bcdfghjklmnpqrstvwxyz"
    return (c in consonante)

def porcentaje(n, d):
    porcentaje_final = "No hubo palabras por lo tanto no se calculo un porcentaje"
    if d != 0:
        porcentaje = (n/d) * 100
        porcentaje_final = round(porcentaje, 2)
    return porcentaje_final


def test():
    # Inicializacion de variables
    cont_letras_palabras = 0
    cont_palabras = 0
    hay_consonante = False
    cant_hay_consonante = False
    s_si = False
    hay_si = False
    n_no = False
    hay_no = False
    cant_hay_si_no = 0
    o_on = False
    hay_on = False
    cant_hay_on = 0
    empieza_l = False
    empieza_le = False
    termina_t = False
    termina_to = False
    cant_le_to = 0
    posicion_n_on = 0
    posicion_o_to = 0

    # Ingreso de cadena
    texto = input("Ingrese un texto a procesar (Finaliza con '.'): ")
    texto = texto.lower()

    # Proceso de cadena
    for car in texto:
        if car != " " and car != ".":
            cont_letras_palabras += 1
            if es_consonante(car):
                hay_consonante = True
            if car == "s":
                s_si = True
            else:
                if s_si and (car == "i" or car == "í"):
                    hay_si = True
                s_si = False
            if car == "n":
                n_no = True
            else:
                if n_no and (car == "o" or car == "ó"):
                    hay_no = True
                n_no = False
            if car == "o" or car == "ó":
                o_on = True
            else:
                if o_on and car == "n":
                    hay_on = True
                    posicion_n_on = cont_letras_palabras
            if cont_letras_palabras != 1 and posicion_n_on != cont_letras_palabras:
                hay_on: False
            if car == "l" and cont_letras_palabras == 1:
                empieza_l = True
            else:
                if empieza_l and car == "e":
                    empieza_le = True
                empieza_l = False
            if car == "t":
                termina_t = True
            else:
                if termina_t and car == "o":
                    termina_to = True
                    posicion_o_to = cont_letras_palabras
                termina_t = False
            if cont_letras_palabras != 1 and posicion_o_to != cont_letras_palabras:
                termina_to = False
        else:
            if cont_letras_palabras > 0:
                cont_palabras += 1
                if hay_consonante:
                    cant_hay_consonante += 1
                if hay_si and hay_no:
                    cant_hay_si_no += 1
                if hay_on:
                    cant_hay_on += 1
                if empieza_le and termina_to:
                    cant_le_to += 1

            # Reinicializacion de variables que dependen
            # de cada palabra
            cont_letras_palabras = 0
            hay_consonante = False
            s_si = False
            hay_si = False
            n_no = False
            hay_no = False
            o_on = False
            hay_on = False
            empieza_le = False
            termina_to = False

    # Procesar Resultados
    porc_consonante = porcentaje(cant_hay_consonante, cont_palabras)
    porc_si_no = porcentaje(cant_hay_on, cont_palabras)
    porc_termina_on = porcentaje(cant_hay_si_no, cont_palabras)

    #Mostrar Resultados
    print("El porcentaje de palabras que contienen al menos una consonante es:", porc_consonante)
    print("El porcentajes de palabras que contiene 'si' y 'no' es:", porc_si_no)
    print("El porcentaje de palabras que termina con 'on':", porc_termina_on)
    print("La cantidad de palabras que empiezan con 'le' y termina con 'to' es:", cant_le_to)

if __name__ == "__main__":
    test()
