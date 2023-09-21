def test():
    # Inicializacion de variables
    cont_letras_palabras = 0
    cont_palabras = 0

    # Ingreso de cadena
    texto = input("Ingrese un texto a procesar (Finaliza con '.'): ")
    texto = texto.lower()

    # Proceso de cadena
    for car in texto:
        if car != " " and if car != ".":
            cont_letras_palabras += 1
        else:
            if cont_letras_palabras > 0:
                cont_palabras += 1

        # Reinicializacion de variables que dependen
        # de cada palabra
        cont_letras_palabras = 0

    # Procesar Resultados


    #Mostrar Resultados


if __name__ == "__main__":
    test()
