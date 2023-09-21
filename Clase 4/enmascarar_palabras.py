# Prueba
"""
s = "Hola"
print(s[1])
print(len(s))
"""

__author__ = "Santiago Gutierrez"

print("Bienvenido al programa que enmascara palabras...")

#Ingreso de datos
# solicitar al usuario la palabra
palabra = input("Ingrese la palabra a enmascarar: ")

#Procesos
#Nos quedamos con el primer y el ultimo caracter de la palabra
primer_caracter = palabra[0]
ultimo_caracter = palabra[-1]

# Vamos a generar los asteriscos necesarios
asteriscos = "*" * (len(palabra) - 2)

# Generar la palabra de resultado
palabra_enmascarada = primer_caracter + asteriscos \
                      + ultimo_caracter

# Mostramos el resultado
print("\nEl resultado es: ", palabra_enmascarada)
