"""cree un programa que ingresando 4 numeros los ordene de mayor a menor y
viceversa, dceterminar si la suma de los dos primeros es un numero par, y
determinar si la suma de los dos ultimos son numero impar. no usar max() ni
min()"""

n1 = int(input("Ingrese un primer número: "))
n2 = int(input("Ingrese un segundo número: "))
n3 = int(input("Ingrese un tercer número: "))
n4 = int(input("Ingrese un cuarto número: "))

if n1 > n2:
    may1 = n1
    men1 = n2
else:
    may1 = n2
    men1 = n1

if n3 > n4:
    may2 = n3
    men2 = n4
else:
    may2 = n4
    men2 = n3

if may1 > may2:
    may = may1
    med1 = may2
else:
    may = may2
    med1 = may1

if men1 > men2:
    men = men2
    med2 = men1
else:
    men = men1
    med2 = men2
if med1 > med2:
    med_may = med1
    med_men = med2
else:
    med_may = med2
    med_men = med1

print("\nOrden de los números de mayor a menor:")
print("\t", may)
print("\t", med_may)
print("\t", med_men)
print("\t", men)
print("\n Orden a los números de menor a mayor:")
print("\t", men)
print("\t", med_men)
print("\t", med_may)
print("\t", may)

if (n1 + n2) % 2 == 0 or (n3 + n4) % 2 != 0:
    print("\nOtras aclaraciones:")
    if (n1 + n2) % 2 == 0:
        print("La suma de los dos primeros números ingresados da como"
              " resultado un número par.")
    if (n3 + n4) % 2 != 0:
        print("La suma de los dos ultimos números ingresados da como "
              "resultado un número impar.")
