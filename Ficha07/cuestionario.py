t4 = ()
for c in 'Python':
     t4 += c,
print(t4)

t1 = tuple('Python')
print(t1)
t3 = ('P', 'y', 't', 'h', 'o', 'n')
print(t3)
t2 = 'P', 'y', 't', 'h', 'o', 'n'
print(t2)
Python = 'Java'
t5 = tuple(Python)
print(t5)

print('Determinacion del mayor de una sucesion (variante 3)...')

# may = None
b = False
num = int(input('Ingrese un numero (con 0 finaliza): '))
while num != 0:
    if b == False:
        may = num
        b = True
    elif num > may:
        may = num
    num = int(input('Ingrese otro (con 0 finaliza): '))

print('El mayor es:', may)
