from registroVenta import *
import random
import pickle
import os.path


# Función para validar un ingreso
def validar_ingreso(lim_inf, mensaje):
    num = lim_inf - 1

    while num < lim_inf:
        num = int(input(mensaje))
        if num < lim_inf:
            print('\n>>> Un número mayor a', lim_inf, 'porfaaaaaaaaa a a')

    return num


# Función para validar el ingreso de un número en un intervalo
def validar_intervalo(lim_inf, lim_sup, mensaje):
    num = lim_inf - 1

    while num < lim_inf or num > lim_sup:
        num = int(input(mensaje))
        if num < lim_inf or num > lim_sup:
            print('\n>>> Un número entre', lim_inf, 'y', lim_sup, 'por favor...')

    return num


# Función add in order por número de venta (de menor a mayor)
def add_in_order_venta(vec_ventas, registro):
    n = len(vec_ventas)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if vec_ventas[c].numero == registro.numero:
            pos = c
            break

        if registro.numero < vec_ventas[c].numero:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec_ventas[pos:pos] = [registro]


# Función para generar el vector de las ventas
def crear_vector_ventas(vec_ventas, n):
    # Variable auxiliar
    descris = ('Big Mac', 'Stacker', 'Alfajor Jorgito', '9 de Oro', 'Una manzana', 'Yerba Mate', 'Whiskas',
               'La vacuna del covid', 'El bigote de Alberto', 'Marcelo Máximo Laxante')

    # Ciclo de generacion
    for i in range(n):
        numero_venta = random.randint(1000, 5000)
        descripcion = random.choice(descris)
        monto = round((random.random() * 10000 + 700), 1)
        articulo = random.randint(0, 9)
        vendedor = random.randint(0, 4)

        # Asignación al vector...
        venta = Venta(numero_venta, descripcion, monto, articulo, vendedor)
        add_in_order_venta(vec_ventas, venta)


# Función para mostrar el vector de ventas
def mostrar_vector_ventas(vec_ventas):
    for venta in vec_ventas:
        print(to_string_venta(venta))


# Función para hacer el conteo en el punto 2
def conteo_articulo_vendedor(vec_ventas):
    # Se crea la matriz de conteo
    matriz_conteo = [[0] * 10 for vendedor in range(5)]

    # Se recorre el vector para hacer el conteo
    for venta in vec_ventas:
        fila = venta.vendedor
        columna = venta.articulo

        # Se cuenta...
        matriz_conteo[fila][columna] += 1

    return matriz_conteo


# Función para mostrar el conteo del punto 2
def mostrar_conteo_punto2(matriz_conteo):
    for f in range(len(matriz_conteo)):
        for c in range(len(matriz_conteo[f])):
            if matriz_conteo[f][c] != 0:
                print('> Vendedor', f, 'y artículo', c, '--->', matriz_conteo[f][c], 'ventas')


# Función completa del punto 2
def punto2(vec_ventas):
    # Se hace el conteo...
    matriz = conteo_articulo_vendedor(vec_ventas)

    # Se muestra la matriz
    mostrar_conteo_punto2(matriz)


# Función para calcular la recaudación del punto 3
def recaudacion_artiuclo_vendedor(vec_ventas):
    # Se crea la matriz de acumulacion
    matriz_acu = [[0] * 10 for vendedor in range(5)]

    # Se recorre el vector para acumular
    for venta in vec_ventas:
        fila = venta.vendedor
        columna = venta.articulo

        # Se acumula
        matriz_acu[fila][columna] += venta.monto

    return matriz_acu


# Función para mostrar la acumulación del punto 3
def mostrar_recaudacion_punto3(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] != 0:
                print('> Vendedor', f, 'y artículo', c, '---> $', matriz[f][c], 'en Ventas')


# Función completa del punto 3
def punto3(vec_ventas):
    # Primero se acumula
    matriz = recaudacion_artiuclo_vendedor(vec_ventas)

    # Se muestra
    mostrar_recaudacion_punto3(matriz)


# Función para determinar la venta con mayor monto (punto 4)
def mayor_venta(vec_ventas):
    # Se supone de antemano que el mayor es el primer elemento
    may = vec_ventas[0]

    # Se usa un ciclo para comparar
    for venta in vec_ventas:
        if venta.monto > may.monto:
            may = venta

    return may


# Función para mostrar el punto 4
def punto4(vec_ventas):
    # Primero, se determina la mayor venta
    mayor = mayor_venta(vec_ventas)

    # Ahora, se muestra
    print('> La mayor venta fue: \n')
    print(to_string_venta(mayor))


# Función para buscar venta por número (punto 5)
def buscar_por_numero(vec_ventas, x_numero):
    # Se usa la busqueda binaria
    n = len(vec_ventas)
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if x_numero == vec_ventas[c].numero:
            return c

        if x_numero < vec_ventas[c].numero:
            der = c - 1
        else:
            izq = c + 1

    return -1


# Función del punto 5
def punto5(vec_ventas):
    # Primero, se ingresa el número de venta a buscar
    x_numero = int(input('-Ingresá el número de venta a buscar: '))

    # Se hace la búsqueda
    indice = buscar_por_numero(vec_ventas, x_numero)

    # Nos fijamos...
    if indice > -1:
        print('\n> Se encontró un resultado: ')
        print(to_string_venta(vec_ventas[indice]))
    else:
        print('\n> No se pudo encontrar nada...')


# Función para buscar por descripción
def buscar_por_descripcion(vec_ventas, descripcion_x):
    for i in range(len(vec_ventas)):
        if vec_ventas[i].descripcion.lower() == descripcion_x.lower():
            return i
    return -1


# Función para el punto 6
def punto6(vec_ventas):
    descripcion_x = input('-Ingresá una descripción para buscar: ')

    # Hacemos la busqueda
    indice = buscar_por_descripcion(vec_ventas, descripcion_x)

    # Vemos que pasa
    if indice > -1:
        print('\n> Se encontró un resultado:')
        print(to_string_venta(vec_ventas[indice]))
    else:
        print('\n> No se pudo encontrar ninguna descricpción...')


# Función para calcular el monto recaudado por las ventas del artículo 3
def recaudacion_articulo3(vec_ventas):
    # Acumulador
    acumulador = 0

    # Se recorre el vector para acumular los montos de las ventas del artículo 3
    for venta in vec_ventas:
        if venta.articulo == 3:
            acumulador += venta.monto

    return acumulador


# Función completa del punto 7
def punto7(vec_ventas):
    # Se acumula...
    acu_articulo3 = recaudacion_articulo3(vec_ventas)

    # Se muestra
    if acu_articulo3 > 0:
        print('> La recaudación de las ventas del artículo 3 es: $', acu_articulo3)
    else:
        print('> No hay ventas del artículo 3')


# Función para crear un archivo en el punto 8
def crear_archivo_punto8(vec_ventas, nombre_archivo):
    # Primero, se abre el archivo
    file = open(nombre_archivo, 'wb')

    # Se recorre el vector para exportar todos los datos
    contador = 0
    for venta in vec_ventas:
        pickle.dump(venta, file)
        contador += 1

    # Se cierra el archivo
    file.close()

    print('\n---> Se exportaron', contador, 'datos al archivo ' + '"' + nombre_archivo + '"')


# Función para mostrar el archivo del punto 8
def mostrar_archivo(nombre_archivo):
    # Primero, se verifica que exista
    if not os.path.exists(nombre_archivo):
        print('\n>>> El archivo ' + '"' + nombre_archivo + '" no existe...')
        return

    # Si el archivo existe, se abre
    tam = os.path.getsize(nombre_archivo)
    file = open(nombre_archivo, 'rb')

    # Se recorre y se muestra
    print('\n> Contenido del archivo ' + '"' + nombre_archivo + '": \n')
    while file.tell() < tam:
        reg = pickle.load(file)
        print(to_string_venta(reg))

    # Una vez que se haya mostrado, se cierra el archivo
    file.close()


# Función para el punto 8
def punto8(vec_ventas):
    # Primero, se establece el nombre del archivo
    nombre_archivo = 'todasventas.dat'

    # Despues, se crea
    crear_archivo_punto8(vec_ventas, nombre_archivo)

    # Finalmente, se muestra
    input('---> Presione ENTER para mostrar el archivo...')
    mostrar_archivo(nombre_archivo)


# Función para crear un archivo del punto 9
def crear_archivo_punto9(vec_ventas, nombre_archivo, x_monto):
    # Primero, se abre el archivo
    file = open(nombre_archivo, 'wb')

    # Se recorre el vector para exportar datos
    contador = 0
    for venta in vec_ventas:
        if venta.monto > x_monto:
            contador += 1
            pickle.dump(venta, file)

    # Una vez que se hayan exportado todos los datos, se cierra el archivo y se informa
    file.close()

    return contador


# Función del punto 9
def punto9(vec_ventas):
    # Le pedimos al usuario que ingrese un monto
    x_monto = validar_ingreso(500, '-Ingresá el monto a filtrar (se generará un archivo con las ventas mayores): ')

    # Primero, hacemos el nombre del archivo
    nombre_archivo = 'punto9_' + str(x_monto) + '.dat'

    # Creamos el archivo
    contador = crear_archivo_punto9(vec_ventas, nombre_archivo, x_monto)

    if contador > 0:
        # Mostramos el archivo
        print('\n---> Se exportaron', contador, 'datos al archivo ' + '"' + nombre_archivo + '"')
        input('---> Presioná ENTER para mostrar el archivo generado...')
        mostrar_archivo(nombre_archivo)
    else:
        print('---> No se puede mostrar el archivo, porque ninguna venta era mayor a $' + str(x_monto))


# Función para crear un archivo según artículo (punto 10)
def crear_archivo_punto10(vec_ventas, nombre_archivo, x_articulo):
    # Abro el archivo
    file = open(nombre_archivo, 'wb')

    # El mismo recorrido de siempre
    contador = 0
    for venta in vec_ventas:
        if venta.articulo == x_articulo:
            contador += 1
            pickle.dump(venta, file)

    # Cuando ya se recorre se cierra el archivo
    file.close()

    return contador


# Función del punto 10
def punto10(vec_ventas):
    # Se pide el artículo para generar el archivo
    x_articulo = validar_intervalo(0, 9, '-Ingresá el código del artículo para generar el archivo (0 a 9): ')

    # Se crea el nombre del archivo
    nombre_archivo = 'punto10_articulo' + str(x_articulo) + '.dat'

    # Se crea el archivo, guardando la cantidad de datos que se exportaron
    contador = crear_archivo_punto10(vec_ventas, nombre_archivo, x_articulo)

    # Se muestra
    if contador > 0:
        # Mostramos el archivo
        print('\n---> Se exportaron', contador, 'datos al archivo ' + '"' + nombre_archivo + '"')
        input('---> Presioná ENTER para mostrar el archivo generado...')
        mostrar_archivo(nombre_archivo)
    else:
        print('---> No se puede mostrar el archivo, porque ninguna venta correspondía al artículo', x_articulo)


# Función para generar un vector de un vendedor x (punto 11)
def generar_vector_vendedor(nombre_archivo, vector_vendedor, x_vendedor):
    # Primero, sabiendo que el archivo existe, lo abrimos y obtenemos su tamaño
    file = open(nombre_archivo, 'rb')
    tam = os.path.exists(nombre_archivo)

    # Recorrido del archivo
    while file.tell() < tam:
        registro = pickle.load(file)

        # Nos fijamos si ese registro coincide con el número de vendedor
        if registro.vendedor == x_vendedor:
            vector_vendedor.append(registro)

    # Una vez recorrido el archivo, se cierra
    file.close()


# Función del punto 11
def punto11():
    # Primero, el nombre del archivo (se podría pasar por parámteros tambien)
    nombre_archivo = 'todasventas.dat'

    # Después, verificamos que el archivo exista, si no existe, entonces la función no se ejecuta
    if not os.path.exists(nombre_archivo):
        print('>>> El archivo ' + '"' + nombre_archivo + '" no existe...')
        return

    # Si efectivamente existe...
    vector_vendedor = []
    x_vendedor = validar_intervalo(0, 4, '-Ingrese el código del vendedor a filtrar (0 a 4): ')

    # Se crea el vector, y se verifica antes de mostrarlo
    generar_vector_vendedor(nombre_archivo, vector_vendedor, x_vendedor)

    if len(vector_vendedor) == 0:
        print('\n> No hay ningún vendedor código', x_vendedor)
    else:
        print('\n> Ventas del vendedor', x_vendedor, ': \n')
        mostrar_vector_ventas(vector_vendedor)


# Función para calcular la recaudación promedio del punto 12
def recaudacion_promedio(nombre_archivo):
    # el archivo existe, entonces se puede trabajar
    tam = os.path.getsize(nombre_archivo)
    file = open(nombre_archivo, 'rb')

    # Variables auxiliares
    acumulacion = 0
    cantidad = 0

    # Ciclo
    while file.tell() < tam:
        registro = pickle.load(file)

        # Hacemos las cuentas
        cantidad += 1
        acumulacion += registro.monto

    # Cuando se haya recorrido el archivo, se cierra, y se terminan de hacer las cuentas
    file.close()

    # Calculo
    if cantidad != 0:
        recaudacion_prom = acumulacion / cantidad
    else:
        recaudacion_prom = 0

    return recaudacion_prom


# Función para el punto 12
def punto12():
    # El nombre del archivo del punto 8
    nombre_archivo = 'todasventas.dat'

    # Verificamos si el archivo existe...
    if not os.path.exists(nombre_archivo):
        print('>>> El archivo ' + '"' + nombre_archivo + '" no existe')
        return

    # Si el archivo existe, entonces se calcula
    rec_prom = recaudacion_promedio(nombre_archivo)

    # Mostramos los resultados
    print('> La recaudación promedio de las ventas del archivo ' + '"' + nombre_archivo + '" es: $', rec_prom)
