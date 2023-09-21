"""Según la Ley Electoral de la República ArgenƟna, el Presidente y el Vicepresidente se eligen de
acuerdo a las siguientes reglas:
Arơculo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %)
de los votos afirmaƟvos válidamente emiƟdos; en su defecto, aquella que hubiere obtenido el cuarenta
por ciento (40 %) por lo menos de los votos afirmaƟvos válidamente emiƟdos y, además, exisƟere una
diferencia mayor de diez puntos porcentuales respecto del total de los votos afirmaƟvos válidamente
emiƟdos, sobre la fórmula que le sigue en número de votos.
Arơculo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escruƟnio
ejecutado por las Juntas Electorales, y cuyo resultado único para toda la Nación será anunciado por la
Asamblea LegislaƟva atento lo dispuesto por el arơculo 120 de la presente ley, se realizará una segunda
vuelta dentro de los treinta (30) días.
Arơculo 151. — En la segunda vuelta parƟciparán solamente las dos fórmulas más votadas en la
primera, resultando electa la que obtenga mayor número de votos afirmaƟvos válidamente emiƟdos.
Desarrollar un programa que permita ingresar, para los 3 parƟdos más votados: fórmula (presidente + vice) y canƟdad de votos obtenidos.
Luego determinar:
Qué fórmula obtuvo el mayor porcentaje.
Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso, indicar también quienes
parƟcipan de la segunda vuelta"""
elecc_efec = False

# Ingreso de datos
print("Ingrese los siguientes datos:")
p1_formula = input("Formula del primer partido: ")
p1_cant = float(input("Porcentaje de votantes del primer partido: "))
p2_formula = input("Formula del segundo partido: ")
p2_cant = float(input("Porcentaje de votantes del segundo partido: "))
p3_formula = input("Formula del tercer partido: ")
p3_cant = float(input("Porcentaje de votantes del tercer partido: "))

if p1_cant > p2_cant:
    may = p1_cant
    f_may = p1_formula
    men = p2_cant
    f_men = p2_formula
else:
    may = p2_cant
    f_may = p2_formula
    men = p1_cant
    f_men = p1_formula
if p3_cant > may:
    med = may
    f_med = f_may
    may = p3_cant
    f_may = p3_formula
elif p3_cant < men:
    med = men
    f_med = f_men
    men = p3_cant
    f_men = p3_formula
else:
    med = p3_cant
    f_med = p3_formula

if may > 45 or may - med > 10:
    elecc_efec = True

if not elecc_efec:
    print("No se cumplieron los requisitos para que una fórmula "
          "fuera efectivamente electa.")
    print("Segunda vuelta entre " + f_may + " y " + f_med)
else:
    print("Se cumplieron los requisitos para que una fórmula fuera"
          " efectivamente electa")
    if may > 45:
        print("Ganó con más del 45% de los votos" + f_may)
    else:
        print("Ganó con mas de 40% la fórmula " + f_may + " por "
        "diferencia de mas de 10 puntos con " + f_med)
