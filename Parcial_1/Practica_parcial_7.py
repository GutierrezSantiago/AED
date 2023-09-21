"""Realizar un programa que tome tres números, los ordene de mayor a menor, y diga si el tercero es
el resto de la división de los dos primeros."""

n1 = int(input("Ingrese un primer número: "))
n2 = int(input("Ingrese un segundo número: "))
n3 = int(input("Ingrese un tercer número: "))

if n1 > n2:
    may = n1
    men = n2
else:
    may = n2
    men = n1

if n3 > may:
    med = may
    may = n3
elif n3 < men:
    med = men
    men = n3
else:
    med = n3
"""
print("\nOrden de mayor a menor:")
print("\t1.", may)
print("\t2.", med)
print("\t3.", men)
if n1 % n2 == n3:
    print("El tercer número ingresado es el resto de la división de "
          "los dos primeros números ingresados.")
"""
if may % med == men:
    print("El tercer número es el resto de la división de "
          "los dos primeros números.")
