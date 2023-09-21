'''Para calcular el premio de un vendedor, se ingresan 3 montos
correspondientes a sus ventas mensuales del ultimo trimestre.
El premio es quivalente al 50% del menor monto vendido. Si ademas todos
los montos superan los $1000, se agrega un 10% adicional al premio calculado.'''
print("Programa para calcular el premio de un vendedor para un trimestre")
m1 = float(input("Ingrese el monto correspondiente al primer mes del "
                 "trimestre: "))
m2 = float(input("Ingrese el monto correspondiente al segundo mes del "
                 "trimestre: "))
m3 = float(input("Ingrese el monto correspondiente al segundo mes del "
                 "trimestre: "))
m_trimestre = m1 + m2 + m3

if m1 < m2 and m1 < m3:
    men = m1
elif m2 < m3:
    men = m2
else:
    men = m3

if m_trimestre > 1000:
    premio = men * 0.6
else:
    premio = men * 0.5

print("El premio para el vendedor es igual a $", premio)
