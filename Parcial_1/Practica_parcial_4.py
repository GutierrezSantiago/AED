'''Desarrollar un programa en Pyhton, sin usar las funciones min() y max(),
que cargue el numero de materias que han cursado 3 estudiantes en sus carreras.
Determinar y mostrar la mayor y la menor cantidad. Si la diferencia entre
la mayor y la menor supera a la menor en mas de 10, indicar con un mensaje que
los estudiantes analizados avanzan en forma despareja'''

cant_mat1 = int(input("Ingrese la cantidad de materias que ha cursado"
                      " el primer estudiante: "))
cant_mat2 = int(input("Ingrese la cantidad de materias que ha cursado"
                      " el segundo estudiante: "))
cant_mat3 = int(input("Ingrese la cantidad de materias que ha cursado"
                      " el tercer estudiante: "))

if cant_mat1 > cant_mat2:
    may = cant_mat1
    men = cant_mat2
else:
    may = cant_mat2
    men = cant_mat1

if cant_mat3 > may:
    may = cant_mat3
elif cant_mat3 < men:
    men = cant_mat3

print("\nLa mayor cantidad de materias cursadas por un estudiante es: ", may)
print("La menor cantidad de materias cursadas por un estudiante es: ", men)

diferencia = may - men

if diferencia > 10:
    print("\nLos estudiantes analizados avanzan en forma despareja.")

x = input("Presione enter para finalizar...")
