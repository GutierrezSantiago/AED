#Programa desafio 1
#PARTE 1
#Carga de datos
segundos_totales = int(input("Ingrese la cantidad de segundos totales: "))

# Procesos
horas = segundos_totales // 60**2
segundos_menos_horas = segundos_totales % 60**2
minutos = segundos_menos_horas // 60
segundos_restantes = segundos_menos_horas % 60

# Resultados
print("Los segundos ingresados transformados al formato horas:minutos:segundos es: ", horas, ":", minutos, ":", segundos_restantes)

# 2:10:32
# 5:16:33
# 0:41:15
# 7:0:13

#PARTE 2

#Carga de datos
horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))

#Procesos
segundos_totales = horas*60**2 + minutos*60 + segundos

#Resultados
print("La cantidad total de segundos es igual a:", segundos_totales)
