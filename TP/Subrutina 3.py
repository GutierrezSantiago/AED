# Menu de opciones
def generacion_proceso(n):
    import random
    casos_confirmados = 0
    sumatoria_edad_confirmados = 0
    cant_confirmados_exterior = 0
    cant_confirmados_capital = 0
    cant_confirmados_gran_cordoba = 0
    cant_confirmados_norte = 0
    cant_confirmados_sur = 0
    cant_riesgo = 0
    sumatoria_edad_riesgo = 0
    cant_personal_de_salud = 0
    cant_casos_autoctonos = 0
    edad_men_autoctono = 0
    cant_contacto_confirmados= 0
    capital_sin_casos = False
    gran_cordoba_sin_casos = False
    norte_sin_casos = False
    sur_sin_casos = False

    for i in range(n):
        # Generacion de datos
        edad, resultado, region, contacto_casos_confirmados, personal_de_salud,\
        viaje_exterior, caso_autoctono = generacion_datos()

        # Impresion de datos generados
        impresion_datos(i, edad, resultado, region, contacto_casos_confirmados,\
                        personal_de_salud, viaje_exterior, caso_autoctono)

        # Proceso de datos generados
        if resultado == "Positivo":
            casos_confirmados += 1
            sumatoria_edad_confirmados += edad
            if viaje_exterior == "Positivo":
                cant_confirmados_exterior += 1
            if region == "Capital":
                cant_confirmados_capital += 1
            elif region == "Gran Córdoba":
                cant_confirmados_gran_cordoba += 1
            elif region == "Norte":
                cant_confirmados_norte += 1
            elif region == "Sur":
                cant_confirmados_sur += 1

        else:
            if edad > 60:
                cant_riesgo += 1
                sumatoria_edad_riesgo += edad

        if personal_de_salud == "Positivo":
            cant_personal_de_salud += 1

        if caso_autoctono == "Positivo":
            cant_casos_autoctonos += 1
            if i == 0:
                edad_men_autoctono = edad
            else:
                if edad_men_autoctono < edad:
                    edad_men_autoctono = edad

        if contacto_casos_confirmados == "Positivo":
            cant_contacto_confirmados += 1

        if cant_confirmados_capital != 0:
            capital_sin_casos = True
        if cant_confirmados_gran_cordoba != 0:
            gran_cordoba_sin_casos = True
        if cant_confirmados_norte != 0:
            norte_sin_casos = True
        if cant_confirmados_sur != 0:
            sur_sin_casos = True

print("hola" \
      "dame bola")
print("hola"
      "dame bola")
