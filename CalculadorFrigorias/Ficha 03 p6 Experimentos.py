#Experimento 1
nombre = input("Ingrese un nombre de 4 letras: ")
nombre2 = nombre[3] + nombre[2] + nombre[1] + nombre[0]
nombre3 = nombre[-1] + nombre[-2] + nombre[-3] + nombre[-4]
print(nombre)
print(nombre2)
print(nombre3)

#Experimento 2
a = int(input("Ingrese un valor: "))
b = int(input("Ingrese un valor: "))
c = int(input("Ingrese un valor: "))
t = (a, b, c)
suma = t[0] + t[1] + t[2]
print("La tupla es: ", t)
print("La suma de los elementos de la tupla es: ", suma)
print(t[0+2])
