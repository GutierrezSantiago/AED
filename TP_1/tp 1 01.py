__author__ = "Assale_85742[1K06]_Gorsd_85861[1K03]_Gutierrez_85828[1K06]"

# Título
print("*" * 30)
print("Cuadro de Diagnostico COVID-19")
print("*" * 30)
print()
# Se asigna el valor None a la variable exterior para determinar
# Mas adelante si un caso es autoctono
# La definición de caso autoctono que se considerara es un caso que
# cumpla con la definicion de caso sospechoso y no tenga historial de
# viaje fuera del país
viaje_exterior = None

# Ingreso de edad, temperatura corporal y neumonia
edad = int(input("Ingrese la edad del paciente: "))
temperatura_corporal = float(input("Ingrese la temperatura corporal\
 del paciente: "))
neumonia = input("Indique si el paciente presenta neumonia,\
 responda con 'Si' o 'No': ")

# Se transforma la cadena de datos cargada en la variable neumonia
# a minuscula para asegurar el correcto funcionamiento del programa
neumonia = neumonia.lower()
print()

# Procesos
# Si el paciente presenta neumonia es un caso sospechoso
# Si no presenta neumonia el paciente se vera si presenta fiebre
# para continuar analizando si el paciente es un caso sospechoso
if neumonia == "si":
    estado = "sospechoso"
else:
    # Si no presenta fiebre el paciente no es sospechoso
    # Si el paciente presenta fiebre se vera la presencia de los
    # sintomas respiratorios para continuar analizando si el paciente
    # es un caso sospechoso
    if temperatura_corporal <= 37:
        estado = "no sospechoso"
    else:
        # Se ingresan los sintomas respiratorios si se presenta fiebre
        print("Responda las siguientes preguntas con 'Si' o 'No'")
        tos = input("¿Presenta tos?: ")
        odinofagia = input("¿Presenta odinofagia?: ")
        dificultad_respiratoria = input("¿Presenta dificultad respiratoria?: ")

        # Se transforman las cadenas de caracteres a minuscula para
        # asegurar el correcto funcionamiento del programa
        tos = tos.lower()
        odinofagia = odinofagia.lower()
        dificultad_respiratoria = dificultad_respiratoria.lower()

        # Si el paciente no presenta sintomas el estado del mismo
        # es no sospechoso. Si el paciente presenta uno o mas
        # sintomas se continuara analizando para verificar si es un
        # caso sospechoso o no
        print()
        if tos == "no" and odinofagia == "no" and\
                dificultad_respiratoria == "no":
            estado = "no sospechoso"
        else:
            # Se carga si el paciente es personal de salud
            personal_salud = input("Responda con 'Si' o 'No' si el \
paciente es un personal de salud: ")
            print()
            # Se transforma a minuscula la cadena de caracteres
            # ingresada en la variable personal_salud para asegurar
            # el correcto funcionamiento del programa
            personal_salud = personal_salud.lower()

            # Si el paciente es un personal de salud se considera
            # sospechoso si presenta fiebre y uno o mas sintomas
            # respiratorios
            if personal_salud == "si":
                estado = "sospechoso"
            else:
                # Se analizan otras variables que indican si
                # un caso es sospechoso o no
                print("Responda las siguientes preguntas con 'Si' o 'No' \n Dentro de los últimos 14 días:")
                contacto_con_confirmado = input("¿El paciente ha estado \
en contacto con casos confirmados de COVID-19? :")
                viaje_exterior = input("¿El paciente tiene un historial \
de viaje fuera del país?: ")
                zona_contacto_local = input("¿El paciente tiene un \
historial de viaje o residencia en zona de transmisión local de \
COVID-19 en Argentina?: ")
                # Se transforman las cadenas de caracteres cargadas
                # a minuscula para asegurar el correcto funcionamiento
                # del programa
                contacto_con_confirmado = contacto_con_confirmado.lower()
                viaje_exterior = viaje_exterior.lower()
                zona_contacto_local = zona_contacto_local.lower()

                # Si no se cumple ninguna de las variables entonces
                # el paciente es un caso no sospechoso. Como se
                # considera que la presencia de la fiebre y uno o mas
                # síntomas respiratorios es verdadera se ingresa
                # directamente el valor booleano True para establecer
                # el siguiente condicional
                if True and (contacto_con_confirmado == "no" or\
                             viaje_exterior == "no" or\
                             zona_contacto_local == "no"):
                    estado = "no sospechoso"
                else:
                    estado = "sospechoso"
# Se carga si el paciente tiene historial de viaje para definir si
# es un caso autoctono o no es posible clasificarlo como autoctono
print()
if estado == "sospechoso":
    if viaje_exterior == None:
        viaje_exterior = input("¿El paciente tiene historial de viaje \
fuera del país en los últimos 14 dias? Responda con 'Si' o 'No': ")
        viaje_exterior = viaje_exterior.lower()
# Se determina si un paciente es de riesgo dependiendo de su edad
else:
    if edad >= 60:
        tipo_de_paciente = "riesgo"
    else:
        tipo_de_paciente = "no riesgo"
# Se determina si el caso es autoctono
if viaje_exterior == "si":
    caso_autoctono = True
else:
    caso_autoctono = False

# Cuadro de Diagnostico
print()
print()
print("-" * 40)
print("El paciente es un caso", estado)
if estado == "no sospechoso":
    if tipo_de_paciente == "riesgo":
        print("El paciente forma parte del grupo de riesgo por su edad(", edad, ")")
else:
    if caso_autoctono == True:
        print("El paciente es un caso autoctono.")
        if (tos == "si" and dificultad_respiratoria == "si") or (tos \
== "si" and odinofagia == "si") or (dificultad_respiratoria == "si" \
and odinofagia == "si"):
            print("El paciente presenta al menos 2 sintomas respiratorios de los consultados.")
        if (contacto_con_confirmado == "no" and viaje_exterior == "no" and zona_contacto_local == "si"):
            print("El paciente no ha estado en contacto con casos \
confirmados ni tiene historial de viaje fuera del país, pero estuvo \
en zonas de transmisión local.")
print("-" * 40)

