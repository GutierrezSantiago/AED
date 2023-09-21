# Programa para calcular las frigorias necesarias para un ambiente
# Dados la altura, el ancho y el largo

# Constante de cálculo de acuerdo a la formula del planteo
constante_frigorias = 40

# Titulo
print("*************************")
print("*Calculador de Frigorias*")
print("*************************")

# Ingreso de datos
ancho = float(input("Ingrese el ancho (en Metros): "))
alto = float(input("Ingrese el alto (En Metros): "))
largo = float(input("Ingrese el largo (En Metros): "))

# Proceso
area = ancho * largo
volumen = area * alto
cantidad_frigorias = volumen * constante_frigorias

# Resultados
print()
print("# Resultados             #")
print("##########################")

print("Cantidad de frigorias necesarias:", cantidad_frigorias)

print()
print("Fin")
