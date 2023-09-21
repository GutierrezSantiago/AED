# Calculador de Sueldo

print("********************")
print("Calculador de Sueldo")
print("********************")

#Ingreso de datos

nom = input("Ingrese el nombre del empleado: ")
horas = float(input("Ingrese la cantidad de horas trabajadas: "))
monto = float(input("Ingrese el monto ganado por hora: $"))

#Procesos
sueldo = horas * monto

#Resultado
print("Nombre del empleado: ", nom)
print("Sueldo final: $", sueldo)
