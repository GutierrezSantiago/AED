"""Desarrollar un programa que permita procesar funciones de un complejo de cines.
Por cada función se conoce: cantidad de espectadores y descuento (S/N).
La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).
El programa deberá:
a) Calcular la recaudación total del complejo, considerando que el valor de
la entrada es de $50 en los días con descuento y $75 en los días sin descuento.
b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje
representan sobre el total de funciones."""

# Titulo
print("-" * 70)
print(" " * 27 + "Complejo de Cine" + " " * 27)
print("-" * 70)
# Inicializacion de variables
recaudacion = 0
funciones = 0
funciones_desc = 0

# Carga de datos
cant_esp = int(input("Ingrese la cantidad de espectadores de la "
                     "primera función. Con 0(cero) \nse termina la"
                     " carga): "))
if cant_esp != 0:
    desc = input("La función es en un día con descuento? (S para si, N para"
             " no):")
# Ciclo
while cant_esp != 0:
    funciones += 1
    if desc == "S" or desc == "s":
        recaudacion += cant_esp * 50
        funciones_desc += 1
    elif desc == "N" or desc == "n":
        recaudacion += cant_esp * 70
    cant_esp = int(input("Ingrese la cantidad de espectadores de al "
                         "siguiente función. Con 0(cero) se termina"
                         " la carga): "))
    if cant_esp != 0:
        desc = input("La función es en un día con descuento? (S para si, N para"
             " no):")

if funciones != 0:
    func_porc_des = funciones_desc / funciones

# Resultados
print("\nLa recaudación total del complejo es: ", recaudacion)
if funciones != 0:
    print("Hubo ", funciones_desc, " funciones con descuento y"
      " representan el ", func_porc_des, " del total de"
      " funciones.")
