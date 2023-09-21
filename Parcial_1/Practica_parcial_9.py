tiempo_total = 0

id_pc1 = int(input("Ingrese el número de identificación de la primera"
                   " PC: "))
tiempo_rep1 = float(input("Ingrese el tiempo de reparación en minutos"
                          " de la primera PC: "))
causa_mant1 = int(input("Que tipo de problemas tiene la primera PC?\n"
                        "Ingrese 1 para problemas de Hardware y 2 "
                        "para problemas de software: "))
id_pc2 = int(input("Ingrese el número de identificación de la segunda"
                   " PC: "))
tiempo_rep2 = float(input("Ingrese el tiempo de reparación en minutos"
                          " de la segunda PC: "))
causa_mant2 = int(input("Que tipo de problemas tiene la segunda PC?\n"
                        "Ingrese 1 para problemas de Hardware y 2 "
                        "para problemas de software: "))
id_pc3 = int(input("Ingrese el número de identificación de la tercera "
                   " PC: "))
tiempo_rep3 = float(input("Ingrese el tiempo de reparación en minutos"
                          " de la tercera PC: "))
causa_mant3 = int(input("Que tipo de problemas tiene la primera PC?\n"
                        "Ingrese 1 para problemas de Hardware y 2 "
                        "para problemas de software: "))

# Total tiempo de mantenimiento
tiempo_total += tiempo_rep1
tiempo_total += tiempo_rep2
tiempo_total += tiempo_rep3

# Mayor tiempo de mantenimiento
if tiempo_rep1 > tiempo_rep2:
    may = tiempo_rep1
    id_may = id_pc1
else:
    may = tiempo_rep2
    id_may = id_pc2

if tiempo_rep3 > may:
    may = tiempo_rep3
    id_may = id_pc3

tiempo_prom = tiempo_total / 3

print("\nTiempo total de las tareas de mantenimiento: ", \
      tiempo_total)
print("La PC " + str(id_may) + " tuvo mayor tiempo en tareas de"
      " mantenimiento.")
print("Tiempo promedio de tareas de mantenimiento: ", tiempo_prom)
if causa_mant1 == 1 and causa_mant2 == 1 and causa_mant3 == 1:
    print("Todas las PCs a las que se les ha realizado mantenimiento"
          " tuvieron problemas de hardware.")
