#Intercambios#
#Un intercambio de  dos variables requiere el uso de una tercera variable a modo auxiliar#

#Valores iniciales
a = 12
b = 4
#Secuencia de intercambio
c = a
a = b
b = c
print(a)
print(b)
# En el siguiente caso se forma una tupla con el operador de empaquetado(a la derecha del igual) pero asimismo
# se usa el operador de desempaquetado(a la izquierda del igual) por lo que en el fondo ocurren esos procesos y
#a toma el valor de 4 y b el valor de 12
a = 12
b = 4
a, b = b, a
print(a)
print(b)
