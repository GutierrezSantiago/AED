def ingreso_validacion_mail():
    error = True
    error_primer_ultimo = False
    error_arroba = False
    error_puntos = False
    n = 0
    cc = 0
    c_arroba = 0
    mail = input("Ingrese su cuenta(Recuerde que no deben ir dos puntos seguidos"
                 " y no debe comenzar ni \nterminar con un punto o un arroba. "
                 "Este ultimo debe ser un valor intermedio): ")
    cf = len(mail)
    while n <= 3 and error:
        n += 1
        error = False

        for c in mail:
            cc += 1
            if (cc == 1 or cc == cf) and (c == "." or c == "@"):
                error_primer_ultimo = True
            if c == "@":
                c_arroba += 1

            if c_arroba == 1:
                error_arroba = False
            else:
                error_arroba = True
            if cc != 1:
                if ca == "." and c == ".":
                    error_puntos = True

            ca = c

        if error_primer_ultimo or error_arroba or error_puntos:
            error = True

        if n == 3 and error:
            print("\nLa cantidad de intentos se ha agotado.")
            input("Presione enter para cerrar el programa.")
            exit()
        if error:
            print("\nEl mail ingresado es invalido. Al tercer intento invalido "
                  "o se le permitiran \ningresar nuevamente el mail.")
            mail = input("Ingrese su cuenta(Recuerde que no deben ir dos puntos "
                         "seguidos y no debe comenzar ni \nterminar con un punto "
                         "o un arroba. Este arroba debe ser unico y ademas debe "
                         "ser \nun valor intermedio): ")
    print("\nLa cuenta a sido validada. La cuenta ingresada es", mail)


mail = ingreso_validacion_mail()
