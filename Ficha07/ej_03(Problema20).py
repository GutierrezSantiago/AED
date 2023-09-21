"""Un pequeño comercio de papelería cuenta con dos vendedores. Cada vendedor está
codificado con los números 1 y 2. Considere que la carga de datos se realizará desde teclado, de
forma que una entrada consta de 3 variables que representan una venta realizada: por cada venta,
cargar el código del vendedor (1 o 2) que hizo la venta, cantidad de artículos vendida en esa
operación, e importe de la venta. El fin de datos se indicará con código de vendedor igual a 0 (cero).
El dueño del comercio desea cierta información estadística y para ello solicita un programa que
obtenga lo siguiente:
a.) La cantidad de productos vendida por cada vendedor (dos totales).
b.) El importe total vendido por cada vendedor (otros dos totales).
c.) El importe de la menor venta realizada por el vendedor 2.
d.) El importe promedio de ventas por vendedor (importe total acumulado / 2)."""

print("-" * 70)
print("Programa para calcular los datos de las operaciones hechas por"
      " \nvendedores")
print("-" * 70)

cantidad1 = 0
importe1 = 0
cantidad2 = 0
importe2 = 0
men = None
codigo_vendedor = int(input("Ingrese el código del vendedor (recuerde"
                            " que con cero termina la carga \nde datos): "))
while codigo_vendedor < 0 or codigo_vendedor > 2:
    print("La carga de datos es erronea. Recuerde que los posibles "
          "valores para \nel codigo de vendedor es 1, 2 o 0. Este"
          " ultimo funciona para terminar \nla carga de datos.")
    codigo_vendedor = int(input("Ingrese el código del vendedor (recuerde"
                            " que con cero termina la carga \nde datos): "))
while codigo_vendedor != 0:
    cantidad_vendida = int(input("Ingrese la cantidad de artículos"
                                 " vendida en la venta realizada: "))
    importe_venta = float(input("Ingrese el importe de la venta "
                                 "realizada: "))
    if codigo_vendedor == 1:
        cantidad1 += cantidad_vendida
        importe1 += importe_venta
    else:
        cantidad2 += cantidad_vendida
        importe2 += importe_venta
        if men == None or men > importe_venta:
            men = importe_venta
    codigo_vendedor = int(input("Ingrese el código del vendedor "
                                "(recuerde que con cero termina "
                               "la carga \nde datos): "))
if men == None:
    men = 0
importe_promedio = (importe1+importe2)/2
importe1 = round(importe1, 2)
importe2 = round(importe2, 2)
importe_promedio = round(importe_promedio, 2)

print("-" * 70)
print(" "*30 + "Resultados" + " "*30)
print("-" * 70)
print("Cantidad de productos vendidos por el vendedor 1: ", cantidad1)
print("Cantidad de productos vendidos por el vendedor 2: ", cantidad2)
print("Importe total vendido por el vendedor 1: ", importe1)
print("Importe total vendido por el vendedor 2: ", importe2)
print("Menor importe de las ventas realizadas por el vendedor 2: ", men)
print("Importe promedio de ventas por vendedor: ", importe_promedio)
