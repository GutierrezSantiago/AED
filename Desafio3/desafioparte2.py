def valor_modal(cont):
    max = 0
    vuelta = 0
    for x in cont:
        if x > max:
            max = x
            max_i = vuelta
        elif x == max:
            max = 0
            max_i = vuelta
        vuelta += 1
    return max, max_i


#
# v = [6, 1, 5 ,6, 6, 6, 6, 6, 6, 6, 5, 3, 3, 3, 3, 3]
# c = 30 * [0]
# for x in v:
#     c[x-1] += 1
# print(c)
# max, max_i = valor_modal(c)
# print("Valor modal: ", max_i+1)
# print("Frecuencia modal: ", max)

import soporte
c = 300000 * [0]
v = soporte.vector_known_range(300000)
cant_dif = 0
for x in v:
    c[x] += 1
for x in range(len(c)):
    if c[x] != 0:
        cant_dif += 1
print(cant_dif)
j, k = valor_modal(c)
print("Valor modal:", k)
print("Frecuencia del valor modal:", j)
print(c[k])
