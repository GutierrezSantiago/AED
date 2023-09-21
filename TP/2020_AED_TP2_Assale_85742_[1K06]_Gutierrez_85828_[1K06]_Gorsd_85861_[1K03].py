def validacion_pacientes(n):
    while n <= 0:
        print("El número de pacientes a procesar debe ser mayor a 0.")
        n = int(input("Ingrese el cantidad de pacientes a procesar: "))
    return n


def ingreso_validacion_mail():
    error = True
    error_primer_ultimo = False
    error_arroba = False
    error_puntos = False
    n = 0
    cc = 0
    c_arroba = 0
    mail = input("Ingrese su cuenta(Recuerde que no deben ir dos puntos seguidos"
                 " y no debe \ncomenzar ni terminar con un punto o un arroba. "
                 "Este ultimo debe ser un valor \nintermedio): ")
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
    print("-" * 79)
    print("La cuenta a sido validada. La cuenta ingresada es", mail)
    print("-" * 79)

def porcentaje(a, b):
    if b == 0:
        return "0"
    porcentaje_sin_redondeado = (a/b) * 100
    porcentaje = round(porcentaje_sin_redondeado, 2)
    return porcentaje


def promedio(a, b):
    if b == 0:
        return "0"
    promedio_sin_redondeo = a / b
    promedio = round(promedio_sin_redondeo, 2)
    return promedio


def generacion_datos():
    import random
    edad = random.randint(0, 122)
    resultado = random.choice(("Positivo", "Negativo"))
    region = random.choice(("Capital", "Gran Córdoba", "Norte", "Sur"))
    contacto_casos_confirmados = random.choice(("Positivo", "Negativo"))
    if edad < 18:
        personal_de_salud = "Negativo"
    else:
        personal_de_salud = random.choice(("Positivo", "Negativo"))
    viaje_exterior = random.choice(("Positivo", "Negativo"))
    if resultado == "Positivo" and contacto_casos_confirmados == "Negativo" and\
            personal_de_salud == "Negativo" and viaje_exterior == "Negativo":
        caso_autoctono = "Positivo"
    else:
        caso_autoctono = "Negativo"
    return (edad, resultado, region, contacto_casos_confirmados, personal_de_salud,
           viaje_exterior, caso_autoctono)


def impresion_datos(i, edad, resultado, region, contacto_casos_confirmados,
                    personal_de_salud, viaje_exterior, caso_autoctono):
    if i == 0:
        print("-" * 79)
    print("Paciente número ", str(i+1))
    print(">Edad: ", str(edad))
    print(">Resultado del test: ", str(resultado))
    print(">Región: ", str(region))
    print(">Contacto con casos confirmados: ", str(contacto_casos_confirmados))
    print(">Personal de salud: ", str(personal_de_salud))
    print(">Viajo al exterior: ", str(viaje_exterior))
    print(">Caso autoctono: ", str(caso_autoctono))
    print("-" * 79)


def menu_de_opciones(cant_conf, porc_conf_total, prom_edad_riesgo, cant_salud,
                     porc_salud_total, prom_edad_conf, edad_men_autoctono,
                     cant_conf_capital, porc_conf_capital_total,
                     cant_conf_gran_cordoba, porc_conf_gran_cordoba_total,
                     cant_conf_norte, porc_conf_norte_total, cant_conf_sur,
                     porc_conf_sur_total, cant_conf_exterior, cant_contacto_conf,
                     capital_con_casos, gran_cordoba_con_casos, norte_con_casos,
                     sur_con_casos, porc_autoctono_conf):
    opcion = 1
    while opcion != 11:
        print("Menu de opciones")
        print("Opción 1 - Cantidad de casos confirmados y porcentaje sobre el "
              "total de casos.")
        print("Opción 2 - Edad promedio de los pacientes que pertenecen al grupo "
              "de riesgo.")
        print("Opción 3 - Cantidad y porcentaje que el personal de salud "
              "representa sobre el \ntotal de casos.")
        print("Opción 4 - Edad promedio entre los casos confirmados.")
        print("Opción 5 - Menor edad entre los casos autóctonos.")
        print("Opción 6 - Cantidad de casos confirmados por región y porcentaje "
              "que representa \ncada uno sobre el total de casos.")
        print("Opción 7 - Cantidad de casos confirmados con viaje al exterior.")
        print("Opción 8 - Cantidad de casos sospechosos en contacto con casos "
              "confirmados.")
        print("Opción 9 - Las regiones sin casos confirmados.")
        print("Opción 10 - Porcentaje de casos positivos autóctonos sobre el "
              "total de casos \n confirmados.")
        print("Opción 11 - Salir.")

        if opcion != 11:
            print("-" * 79)
        if opcion < 1 and opcion > 11:
            print("El número previamente ingresado no esta asociado a ninguna "
                  "opción valida")
            print("Recuerde que el rango de opciones validos es de 1 a 11 "
                  "inclusive.")

        opcion = int(input("Ingrese el número de opción que quiere utilizar: "))

        if opcion == 1:
            print("Cantidad de casos confirmados: ", str(cant_conf))
            print("Porcentaje de casos confirmados sobre el total de casos: ",
                  str(porc_conf_total), "%")
        elif opcion == 2:
            if float(prom_edad_riesgo) > 60:
                print("Edad promedio de los pacientes pertenecientes al grupo de"
                      " riesgo: ", str(prom_edad_riesgo))
            else:
                print("No hubo pacientes de riesgo.")
        elif opcion == 3:
            print("Cantidad de casos que son personal de la salud: ",
                  str(cant_salud))
            print("Porcentaje de casos que son personal de la salud sobre"
                  " el total de casos: ",
                  str(porc_salud_total), "%")
        elif opcion == 4:
            if cant_conf != 0:
                print("Edad promedio entre los casos confirmados: ",
                      str(prom_edad_conf))
            else:
                print("No hubo casos confirmados.")
        elif opcion == 5:
            if edad_men_autoctono == None:
                print("No hubo casos autoctonos.")
            else:
                print("Menor edad entre los casos autoctonos: ", str(edad_men_autoctono))
        elif opcion == 6:
            if cant_conf != 0:
                print("Cantidad de casos confirmados por región y porcentaje que "
                      "representa sobre el \ntotal de casos:")
                print(">Capital: -", str(cant_conf_capital), "casos confirmados.")
                print("          -Representa el ", str(porc_conf_capital_total),
                      "% del total de casos confirmados.")
                print(">Gran Córdoba: -", str(cant_conf_gran_cordoba), "casos confirmados.")
                print("               -Representa el ", str(porc_conf_gran_cordoba_total),
                      "% del total de casos confirmados.")
                print(">Norte: -", str(cant_conf_norte), "casos confirmados.")
                print("        -Representa el ", str(porc_conf_norte_total),
                      "% del total de casos confirmados.")
                print(">Sur: -", str(cant_conf_sur), "casos confirmados.")
                print("      -Representa el ", str(porc_conf_sur_total),
                      "% del total de casos confirmados.")
            else:
                print("No hubo casos confirmados.")
        elif opcion == 7:
            print("Cantidad de casos confirmados con viaje al exterior: ",
                  str(cant_conf_exterior))
        elif opcion == 8:
            print("Cantidad de casos sospechosos en contacto con casos "
                  "confirmados: ", str(cant_contacto_conf))
        elif opcion == 9:
            print("Regiones sin casos confirmados:")
            if not capital_con_casos:
                print(">Capital.")
            if not gran_cordoba_con_casos:
                print(">Gran Córdoba.")
            if not norte_con_casos:
                print(">Norte")
            if not sur_con_casos:
                print(">Sur")
            if capital_con_casos and gran_cordoba_con_casos\
                   and norte_con_casos and sur_con_casos:
                print(">No existen regiones sin casos confirmados.")
        elif opcion == 10:
            if cant_conf != 0:
                print("Porcentaje de casos autoctonos sobre el total de casos "
                      "confirmados ", str(porc_autoctono_conf), "%.")
            else:
                print("No hubo casos confirmados por lo tanto no hay casos "
                      "autoctonos.")

        if opcion != 11:
            input("Presione enter para cerrar la opción elegida...")
            print("-" * 79)


def generacion_proceso(n):
    cant_conf = 0
    suma_edad_conf = 0
    cant_conf_exterior = 0
    cant_conf_capital = 0
    cant_conf_gran_cordoba = 0
    cant_conf_norte = 0
    cant_conf_sur = 0
    cant_edad_riesgo = 0
    suma_edad_riesgo = 0
    edad_men_autoctono = None
    cant_salud = 0
    cant_casos_autoctonos = 0
    cant_contacto_conf= 0
    capital_con_casos = False
    gran_cordoba_con_casos = False
    norte_con_casos = False
    sur_con_casos = False
    for i in range(n):

        # Generacion de datos
        edad, resultado, region, contacto_casos_confirmados, personal_de_salud,\
        viaje_exterior, caso_autoctono = generacion_datos()

        # Impresion de datos generados
        impresion_datos(i, edad, resultado, region, contacto_casos_confirmados,
                        personal_de_salud, viaje_exterior, caso_autoctono)
        # Inicializacion de variables a utilizar


        # Proceso de datos generados
        if resultado == "Positivo":
            cant_conf += 1
            suma_edad_conf += edad
            if viaje_exterior == "Positivo":
                cant_conf_exterior += 1
            if region == "Capital":
                cant_conf_capital += 1
            elif region == "Gran Córdoba":
                cant_conf_gran_cordoba += 1
            elif region == "Norte":
                cant_conf_norte += 1
            elif region == "Sur":
                cant_conf_sur += 1

        else:
            if edad > 60:
                cant_edad_riesgo += 1
                suma_edad_riesgo += edad

        if personal_de_salud == "Positivo":
            cant_salud += 1

        if caso_autoctono == "Positivo":
            cant_casos_autoctonos += 1
            if edad_men_autoctono == None:
                edad_men_autoctono = edad
            else:
                if edad_men_autoctono > edad:
                    edad_men_autoctono = edad

        if contacto_casos_confirmados == "Positivo":
            cant_contacto_conf += 1

        if cant_conf_capital != 0:
            capital_con_casos = True
        if cant_conf_gran_cordoba != 0:
            gran_cordoba_con_casos = True
        if cant_conf_norte != 0:
            norte_con_casos = True
        if cant_conf_sur != 0:
            sur_con_casos = True

        porc_conf_total = porcentaje(cant_conf, n)
        prom_edad_riesgo = promedio(suma_edad_riesgo, cant_edad_riesgo)
        porc_salud_total = porcentaje(cant_salud, n)
        prom_edad_conf = promedio(suma_edad_conf, cant_conf)
        porc_conf_capital_total = porcentaje(cant_conf_capital, cant_conf)
        porc_conf_gran_cordoba_total = porcentaje(cant_conf_gran_cordoba, cant_conf)
        porc_conf_norte_total = porcentaje(cant_conf_norte, cant_conf)
        porc_conf_sur_total = porcentaje(cant_conf_sur, cant_conf)
        porc_autoctono_conf = porcentaje(cant_casos_autoctonos, cant_conf)

    return (cant_conf, porc_conf_total, prom_edad_riesgo, cant_salud,
           porc_salud_total ,prom_edad_conf, edad_men_autoctono,
           cant_conf_capital, porc_conf_capital_total, cant_conf_gran_cordoba,
           porc_conf_gran_cordoba_total, cant_conf_norte, porc_conf_norte_total,
           cant_conf_sur, porc_conf_sur_total, cant_conf_exterior,
           cant_contacto_conf, capital_con_casos, gran_cordoba_con_casos,
           norte_con_casos, sur_con_casos, porc_autoctono_conf)


def test():
    # Validación mail
    ingreso_validacion_mail()

    n = int(input("Ingrese el cantidad de pacientes a procesar: "))
    n = validacion_pacientes(n)

    # Generación y proceso de datos
    cant_conf, porc_conf_total, prom_edad_riesgo, cant_salud, porc_salud_total ,\
    prom_edad_conf, edad_men_autoctono, cant_conf_capital, porc_conf_capital_total,\
    cant_conf_gran_cordoba,porc_conf_gran_cordoba_total, cant_conf_norte, \
    porc_conf_norte_total, cant_conf_sur, porc_conf_sur_total, cant_conf_exterior,\
    cant_contacto_conf, capital_con_casos, gran_cordoba_con_casos, norte_con_casos, \
    sur_con_casos, porc_autoctono_conf = generacion_proceso(n)

    # Menu de opciones
    menu_de_opciones(cant_conf, porc_conf_total, prom_edad_riesgo, cant_salud,
                     porc_salud_total ,prom_edad_conf, edad_men_autoctono,
                     cant_conf_capital, porc_conf_capital_total,
                     cant_conf_gran_cordoba,porc_conf_gran_cordoba_total,
                     cant_conf_norte, porc_conf_norte_total,cant_conf_sur,
                     porc_conf_sur_total, cant_conf_exterior, cant_contacto_conf,
                     capital_con_casos, gran_cordoba_con_casos, norte_con_casos,
                     sur_con_casos, porc_autoctono_conf)

test()
