print("Ingrese las temperaturas medidas en el depósito de químicos")

Temp1 = float(input("1ra Medición: "))
Temp2 = float(input("2da Medición: "))
Temp3 = float(input("3ra Medición: "))

Prom = (Temp1 + Temp2 + Temp3)/3

print("La temperatura promedio con decimales del depósito de químicos es ", Prom)
print("La temperatura promedio entera del depósito de químicos es ", int(Prom))
print("Alt + 92 = \ ")
