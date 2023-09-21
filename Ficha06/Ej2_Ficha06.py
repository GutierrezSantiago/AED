"""Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas
 en las diferentes sucursales de un país de una determinada empresa.
Los requerimientos funcionales del programa son:
a) Informar la cantidad de ventas ingresadas.
b) Total de ventas.
c) Cantidad de ventas cuyo valor este comprendido entre 100 y 300 unidades.
d) cccccccc
e) Indicar si hubo una cantidad de ventas inferior a 50 unidades.
Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor negativo."""
vent_total = 0
vent_ingresadas = 0
ventas_rango1 = 0
ventas_rango2 = 0
vent_inf = False
ventas = int(input("Ingrese la cantidad de unidades vendidas de una de "
               "las sucursales: "))

while ventas >= 0:
    vent_total += ventas
    vent_ingresadas += 1
    if ventas >= 100 and ventas <= 300:
        ventas_rango1 += 1
    elif ventas == 400 or ventas == 500 or ventas == 600:
        ventas_rango2 += 1
    elif ventas < 50:
        vent_inf = True
    ventas = int(input("Ingrese la cantidad de unidades vendidas de otra "
               "las sucursales: "))

print("\nLa cantidad de ventas ingresadas es: ", vent_ingresadas)
print("La cantidad de ventas totales es: ", vent_total)
print("La cantidad de ventas cuyo valor este comprendido entre 100 y"
      " \n300 unidades es: ", ventas_rango1)
print("La cantidad de ventas con 400, 500 y 600 unidades es: ", ventas_rango2)
if vent_inf:
    print("En una sucursal la cantidad de unidades vendidas fue menor"
          " a 50")
