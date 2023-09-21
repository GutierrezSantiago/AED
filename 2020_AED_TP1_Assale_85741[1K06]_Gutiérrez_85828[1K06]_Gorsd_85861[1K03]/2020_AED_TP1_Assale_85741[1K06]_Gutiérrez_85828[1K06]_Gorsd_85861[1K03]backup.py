# Inicio
print("- "*35)
print()
print("-"*70)
print("   Programa para facilitar el Diagnóstico de COVID-19 \
(Coronavirus)   ")
print("-"*70)
print("Utilice el número '0' para indicar una respuesta negativa y el\
 número \n'1' para indicar una respuesta afirmativa.")
# Valores iniciales y banderas
sintomas = 0
estado = False
riesgo = False
autoctono = False

# Primer ingreso de datos (edad, temperatura corporal, neumonia)
print("Ingrese los siguientes datos del paciente:")
print("_"*70)
edad = int(input("Edad: "))
temperatura_corporal = float(input("Temperatura Corporal en grados\
 centígrados: "))
neumonia = int(input("¿Presenta neumonia?: "))

# Primer proceso
if not(neumonia == 1 or neumonia == 0):
    print("*"*42)
    print("*No ha ingresado los datos correctamente.*")
    print("*"*42)
else:
    if neumonia == 1:
        estado = True
    else:
        if temperatura_corporal > 37:
# Segundo ingreso de datos (sintomas respiratorios)

            print("_"*70)
            print("Se le realizaran preguntas acerca de los sintomas\
 respiratorios que \npresenta el paciente.")
            print("_"*70)
            tos = int(input("¿Presenta tos?: "))
            odinofagia = int(input("¿Presenta odinofagia?: "))
            dificultad_respiratoria = int(input("¿Presenta dificultad\
 respiratoria?: "))
# Segundo proceso

            if not((tos == 0 or tos == 1) and (odinofagia == 0 or\
odinofagia == 1) and (dificultad_respiratoria == 0 or\
dificultad_respiratoria == 1)):
                print("*"*42)
                print("*No ha ingresado los datos correctamente.*")
                print("*"*42)
            else:
                sintomas += tos
                sintomas += odinofagia
                sintomas += dificultad_respiratoria
                if not(sintomas < 1):
# Tercer ingreso de datos (personal de salud)

                    print("_"*70)
                    personal_salud = int(input("¿El paciente es\
 personal de salud?: "))
                    print("_"*70)
# Tercer proceso

                    if not(personal_salud == 0 or personal_salud == 1):
                        print("*"*42)
                        print("*No ha ingresado los datos correctamente.*")
                        print("*"*42)
                    else:
                        if personal_salud == 1:
                            estado = True
                        else:
                            print("Dentro de los ultimos 14 dias:")
                            print()
# Cuarto ingreso de datos (contacto, viaje al exterior, zona de
# transmision local)

                            contacto_confirmados = int(input("¿El paciente\
 ha estado en contacto con casos confirmados de COVID-19?: "))
                            viaje_exterior = int(input("¿El paciente tiene\
 un historial de viaje fuera del país?: "))
                            zona_transmision_local = int(input("¿El paciente\
 tiene un historial de viaje o residencia en zonas de \ntransmisión local\
 de COVID-19 en Argentina?: "))
# Cuarto proceso

                            if not((contacto_confirmados == 0 or\
contacto_confirmados == 1) and (viaje_exterior == 1 or viaje_exterior\
== 0) and (zona_transmision_local == 0 or zona_transmision_local == 1)):
                                print("*"*42)
                                print("*No ha ingresado los datos correctamente.*")
                                print("*"*42)
                            else:
                                if contacto_confirmados == 1 or\
 zona_transmision_local == 1 or viaje_exterior == 1:
                                    estado = True
                                if estado and sintomas >= 2 and\
 contacto_confirmados == 0 and viaje_exterior == 0 and\
 zona_transmision_local == 1:
                                    autoctono = True
if not estado and edad >= 60:
    riesgo = True

# Resultados
print("_"*70)
print("-"*70)
print(" "*24 + "Cuadro de Diagnóstico" + " "*24)
print("-"*70)
if estado:
    print("Estado del paciente: Sospechoso")
    if autoctono:
        print("Tipo de caso: Autoctono")
    else:
        print("Tipo de caso: No autoctono")
else:
    print("Estado del paciente: No sospechoso")
    if riesgo:
        print("Por su edad el paciente pertenece al grupo de riesgo.")
print()
print("El programa a finalizado.")
print("- "*35)

# Fin
