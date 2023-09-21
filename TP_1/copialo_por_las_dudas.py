# Datos personales del paciente
"""
print("Responda las siguientes preguntas con si o no")
tos = input("¿Presenta Tos? :")
tos = tos.lower()
print(tos)

tos_verdadera = tos == "si"
print(tos_verdadera)

print("Indique mediante el numero 0 un sintoma ausente\
 y mediante 1 un sintoma presente")
tos = int(input("Tos: "))
odinofagia = int(input("Odinofagia: "))
dificultad_respiratoria = int(input("Dificultad_respiratoria: "))

sintomas = tos + odinofagia + dificultad_respiratoria

if sintomas == 0:

else sintomas >= 2:
    print("El paciente es un caso autoctono que presenta al menos 2 sintomas")
else:
    print( " El paciente tiene fibre y tien |1 sintoma")
"""
#constante exterior hasta que se pregunte en un determinado punto
exterior = None
x = input("Viajaste al exterior?: ")
if x == "si":
    exterior = input("A donde viajaste?: ")
else:
    print("Que pena")
sospechoso = input("Estas enfermo?:")
if sospechoso == "si":
    print("Estas enfermo")
else:
    print("No estas enfermo")
if exterior == None:
    exterior = input("Donde te enfermaste?")
print("Te enfermaste en ", exterior)

if (s1 and s2) or (s2 and s3) or (s1 and s3)
    print("Presenta al menos 2 de los síntomas respiratorios consultados")
if (contacto == "no" and exterior == "no") and zona de contacto == "si"
    print("No tiene historial exterior ni contacto activos pero si zona")

# ES IMPORTANTE ACLARAR EN COMENTARIOS QUE UN CASO SE CONSIDERARA AUTOCTONO
# SI EL HISTORIAL DE VIAJE ES NULO, SINO SIMPLEMENTE SE CONSIDERARA SOSPECHOSO
# SIN CONSIDERAR EL ORIGEN DEL CONTAGIO
