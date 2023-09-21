from funciones_programita import *
import time


# Script principal
def principal():
    # Creación del vector, con su bandera
    vector_ventas = []
    vector_creado = False

    # Menú de opciones
    op = -1
    while op != 0:
        print()
        print('=' * 100)
        print('1- Generar el vector de ventas, ordenado por número de venta, y mostrarlo')
        print('2- Cantidad de ventas por artículo y vendedor (MATRIZ)')
        print('3- Recaudación acumulada por artículo y vendedor (ACUMULACIÓN MATRIZ)')
        print('4- Mostrar venta con mayor monto en el vector')
        print('5- Buscar venta por número')
        print('6- Buscar venta por descripción')
        print('7- Monto recaudado por las ventas del artículo 3')
        print('8- Generar archivo con todas las ventas. Mostrar ("todasventas.dat")')
        print('9- Ingresar Monto, generar archivo con las ventas que superen el Monto ingresado. Mostrar')
        print('10- Ingresar código de artículo, y generar un archivo con todas las ventas. Mostrar ("punto10.dat")')
        print('11- A partir del archivo del punto 8, ingresar código de vendedor y generar vector con todas\n'
              '\tsus ventas. Mostrar el vector generado')
        print('12- A partir del archivo del punto 8, calcular la recaudación promedio')
        print('0- SALIR')
        print('=' * 100)

        # Ingreso de opción
        op = int(input('\n-Ingrese una opción: '))
        print()

        # Opciones
        if op == 1:
            if not vector_creado:
                n = validar_intervalo(1, 1000, '-Ingresá la cantidad de ventas: ')

                # Se crea el vector
                crear_vector_ventas(vector_ventas, n)
                vector_creado = True

                input('\n---> El vector se ha creado! Presione ENTER para mostrarlo...')
                print()

                # Se muestra
                mostrar_vector_ventas(vector_ventas)
            else:
                # Como el vector ya estaba creado, sólo se muestra
                mostrar_vector_ventas(vector_ventas)

            time.sleep(2)

        elif op == 2:
            if vector_creado:
                punto2(vector_ventas)

            else:
                print('>>> El vector del punto 1 no existe!')

            time.sleep(2)

        elif op == 3:
            if vector_creado:
                punto3(vector_ventas)

            else:
                print('>>> El vector del punto 1 no fue cargado!')

            time.sleep(2)

        elif op == 4:
            if vector_creado:
                punto4(vector_ventas)

            else:
                print('>>> El vector del punto 1 no fue creado!')

            time.sleep(2)

        elif op == 5:
            if vector_creado:
                punto5(vector_ventas)

            else:
                print('>>> El vector del punto 1 no fue creado!!')

            time.sleep(2)

        elif op == 6:
            if vector_creado:
                punto6(vector_ventas)

            else:
                print('>>> El vector del punto 1 no está cargado!')

            time.sleep(2)

        elif op == 7:
            if vector_creado:
                punto7(vector_ventas)

            else:
                print('>>> El vector del punto 1 no está cargado!')

            time.sleep(2)

        elif op == 8:
            if vector_creado:
                punto8(vector_ventas)

            else:
                print('>>> El vector del punto 1 no está cargado!')

            time.sleep(2)

        elif op == 9:
            if vector_creado:
                punto9(vector_ventas)

            else:
                print('>>> El vector del punto 1 no está cargado!')

            time.sleep(2)

        elif op == 10:
            if vector_creado:
                punto10(vector_ventas)

            else:
                print('>>> El vector del punto 1 no está cargado!')

            time.sleep(2)

        elif op == 11:
            punto11()

            time.sleep(2)

        elif op == 12:
            punto12()

            time.sleep(2)

        elif op == 0:
            print('>>> Chauuuu!')
            time.sleep(2)

        else:
            print('>>> No ingresaste ninguna opción, probá de vuelta')
            time.sleep(1.5)


# Prueba del programa
if __name__ == '__main__':
    principal()
