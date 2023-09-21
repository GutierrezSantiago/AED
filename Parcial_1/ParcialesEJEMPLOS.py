#=================================EJERCICIO 1====================================
'''Desarrolle un programa completo en Python, sin usar funciones predefinidas
min() y max(), que permita cargar por teclado 3 valores (3 números reales).
Si el primer valor ingresado es Par, determinar y mostrar el mayor y menor
entre el segundo y tercer valor ingresado. Caso contrario, determinar y
mostrar el mayor y menor entre el primer y segundo valor ingresado. Además,
calcular y mostrar el promedio entre el mayor y el menor.
'''
print('TITULO = "Ojala este sea mi parcial."')
num1 = int(input('Ingrese el primer valor: '))
num2 = int(input('Ingrese el primer valor: '))
num3 = int(input('Ingrese el primer valor: '))

if num1 % 2 == 0:
    print('\n->El primer numero es par, se calculara mayor y menor entre'
          ' el segundo y el tercer numero:')
    if num2 > num3:
        may = num2
        men = num3
    else:
        may = num3
        men = num2
else:
    print('\n->El primer numero NO es par, se calculara mayor y menor entre'
          ' el primer y el segundo numero:')
    if num1 > num2:
        may = num1
        men = num2
    else:
        may = num2
        men = num1

promedio = (may + men) / 2
print('\n>>El mayor numero es:', may, '\n>>El menor numero es:', men,
      '\n>>El promedio entre el mayor y el menor es de:', promedio)

#=================================EJERCICIO 2====================================

'''Desarrolle un programa completo en Python, sin usar funciones predefinidas
min() y max(), que permita cargar por teclado un número que representa un día
de la semana (un valor entero). Muestre por pantalla el día de la semana al que
corresponde (por ejemplo: 1-Domingo, 2-Lunes, etc). En el caso de no ser un
valor entre 1 a 7, mostrar un mensaje de “Error”.
Si el valor ingresado corresponde al día Sábado o Domingo, mostrar por pantalla
el mensaje: “Fin de semana”.
'''
dia_cargado = int(input('Ingrese el dia segun el numero que corresponda:'
                        '\033[1;34m\n1.Domingo\t|\t2.Lunes\n3.Martes\t|'
                        '\t4.Miercoles\n5.Jueves\t|\t6.Viernes\n7.Sabado'
                        '\t|\033[0m\tNumero: '))
#==================BANDERA=======================
fin_de_semana = False
#==================BANDERA=======================
dia_semana = 0
if 0 < dia_cargado > 8:
    if dia_cargado == 1:
        dia_semana = 'Domingo'
        fin_de_semana = True
    elif dia_cargado == 2:
        dia_semana = 'Lunes'
    elif dia_cargado == 3:
        dia_semana = 'Martes'
    elif dia_cargado == 4:
        dia_semana = 'Miercoles'
    elif dia_cargado == 5:
        dia_semana = 'Jueves'
    elif dia_cargado == 6:
        dia_semana = 'Viernes'
    elif dia_cargado == 7:
        dia_semana = 'Sabado'
        fin_de_semana = True
    if fin_de_semana:
        print('\n\t\033[1;35m>>Fin de Semana<<\033[0m')
    else:
        print('\n\t\033[1;35m>>Dia de Semana<<\033[0m')
    print('El dia es:', dia_semana)
else:
    print('\n\033[1;31mERROR: Ha seleccionado un numero no valido.')


#=================================EJERCICIO 3====================================
'''Desarrolle un programa completo en Python, sin usar funciones predefinidas
min() y max(), que permita cargar por teclado 3 variables (3 valores enteros).
Si el primer valor ingresado es igual a cero, calcule y muestre
la siguiente fórmula: √ bᶟ + cᶟ .
Si el primer valor ingresado es mayor a la suma del segundo y tercer valor,
calcule y muestre el cociente entre b/c. Caso contrario, mostrar el mayor
valor entre el segundo valor ingresado y el tercero.'''
print('Ejercicio 3')
num1 = int(input('Ingrese el Primer valor: '))
num2 = int(input('Ingrese el Segundo valor: '))
num3 = int(input('Ingrese el Tercer valor: '))

if num1 == 0:
    formula = (num2 ** 3 + num3 ** 3) ** 0.5
    print('\nEl numero ingresado ha sido = 0:\n>>El resultado de '
          '\033[1;31m√ bᶟ + cᶟ\033[0m: ', round(formula, 2))
elif num1 > (num2 + num3):
    formula = num2 / num3
    print('\nEl primer numero ingresado ha sido mayor a la suma de los 2 '
          'siguientes:\n>>El resultado de \033[1;31mb/c\033[0m: ',
          round(formula,2))
else:
    if num2 > num3:
        may = num2
    else:
        may = num3
    print('\nEl primer numero ingresado NO ha sido mayor a la suma de los 2 '
          'siguientes:\n>>El \033[1;31mmayor entre b y c\033[0m es:', may)

#=================================EJERCICIO 4====================================
'''Desarrollar un programa en Pyhton, sin usar las funciones min() y max(),
que cargue el numero de materias que han cursado 3 estudiantes en sus carreras.
Determinar y mostrar la mayor y la menor cantidad. Si la diferencia entre
la mayor y la menor supera a la menor en mas de 10, indicar con un mensaje que
los estudiantes analizados avanzan en forma despareja'''
print('\t\033[1;35mMATERIAS.\033[0m')
nombre1 = input('Ingrese su nombre: ')
alumno1 = int(input('Cuantas materias curso el alumno/a ' + nombre1 + ':'))
nombre2 = input('Ingrese su nombre: ')
alumno2 = int(input('Cuantas materias curso el alumno/a ' + nombre2 + ':'))
nombre3 = input('Ingrese su nombre: ')
alumno3 = int(input('Cuantas materias curso el alumno/a ' + nombre3 + ':'))

if alumno1 > alumno2:
    may, mayname = alumno1, nombre1
    men, miname = alumno2, nombre2
else:
    may, mayname = alumno2, nombre2
    men, miname = alumno1, nombre1
if alumno3 > may:
    med, medname = may, mayname
    may, mayname = alumno3, nombre3
elif alumno3 < men:
    med, medname = men, miname
    men, miname = alumno3, nombre3
else:
    med, medname = alumno3, nombre3

print('\n-El estudiante que\033[1;35m mas\033[0m materias curso es', mayname,
      'con', may, 'materias cursadas.'
      '\n-El estudiante que\033[1;35m menos\033[0m materias curso es', miname,
      'con', men,'materias cursadas. '
      '\n-El estudiante que se encuentra en el\033[1;35m medio\033[0m es', medname,
      'con', med, 'materias cursadas.')

diferencia = may - men
if diferencia > 10:
    print('\n>>Los estudiantes analizados avanzan en forma despareja.<<')

#=================================EJERCICIO 5====================================
'''Para calcular el premio de un vendedor, se ingresan 3 montos
correspondientes a sus ventas mensuales del ultimo trimestre.
El premio es quivalente al 50% del menor monto vendido. Si ademas todos
los montos superan los $1000, se agrega un 10% adicional al premio calculado.'''

monto1 = int(input('Ingrese el monto 1:'))
monto2 = int(input('Ingrese el monto 2:'))
monto3 = int(input('Ingrese el monto 3:'))

if monto2 > monto1 < monto3:
    men = monto1
elif monto3 < monto2:
    men = monto3
else:
    men = monto3

premio = men * 50 / 100

if (monto1 and monto2 and monto3) > 1000:
    print('Se ha añadido un 10% EXTRA!')
    premio += (men * 10 / 100)

print('/'*50)
print('El premio es de >>', premio, '<<')


a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
d = int(input('D: '))

m1 = a
if b > a:
    m1 = b

m2 = c
if d > c:
    m2 = d

if m1 > m2:
    print(m1)
else:
    print(m2)
