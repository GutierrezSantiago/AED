__author__ = "Santiago Gutierrez"

# Este programa permite generar un mail
# dependiendo de la coincidencia de la
#primera letra del nombre y del apellido

print("Bienvenido al generador de direcciones")
print("--------------------------------------")

# Ingreso de datos
# Solicitar al usuario nombre, apellido y dominio
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dominio = input("Ingrese el dominio: ")

# Procesos
# Convertir nombre, apellido y dominio a minúsculas
nombre = nombre.lower()
apellido = apellido.lower()
dominio = dominio.lower()

# Vamos a tomar la primera letra del nombre y la primera del apellido
primera_nombre = nombre[0]
primera_apellido = apellido[0]

#Decidir cuál política de nombre vamos a utilizar
if primera_nombre != primera_apellido:
    direccion = primera_nombre + apellido \
                   + "@" + dominio
else:
    direccion = nombre + "." + apellido \
                   + "@" + dominio

#Vuelvo al camino común
# Resultado
print("La dirección de correo generada es: ", direccion)
