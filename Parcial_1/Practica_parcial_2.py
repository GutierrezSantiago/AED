'''Desarrolle un programa completo en Python, sin usar funciones predefinidas
min() y max(), que permita cargar por teclado un número que representa un día
de la semana (un valor entero). Muestre por pantalla el día de la semana al que
corresponde (por ejemplo: 1-Domingo, 2-Lunes, etc). En el caso de no ser un
valor entre 1 a 7, mostrar un mensaje de “Error”.
Si el valor ingresado corresponde al día Sábado o Domingo, mostrar por pantalla
el mensaje: “Fin de semana”.
'''
fin_de_semana = False
error = False
print("Cada número representa un día de la semana:")
print("1-Lunes \n2-Martes \n3-Miercoles \n4-Jueves \n5-Viernes \n6-Sábado \
\n7-Domingo")
carga = int(input("Ingrese un número que represente un día de la semana:"))

if carga < 1 or carga > 7:
    error = True
else:
    if carga == 1:
        dia = "Lunes"
    elif carga == 2:
        dia = "Martes"
    elif carga == 3:
        dia = "Miercoles"
    elif carga == 4:
        dia = "Jueves"
    elif carga == 5:
        dia = "Viernes"
    elif carga == 6:
        dia = "Sábado"
        fin_de_semana = True
    elif carga == 7:
        dia = "Domingo"
        fin_de_semana = True

if error:
    print("El número '", carga, "'no corresponde a un día de la semana")
else:
    print("\nEl número ingresado es '", carga,"' que corresponde al día ", dia)
    if fin_de_semana:
        print("Fin de semana")
