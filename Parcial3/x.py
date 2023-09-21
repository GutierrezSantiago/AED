from Gutierrez_Santiago_85828_1K06_Parcial_3 import *
def costo(v, p, *tipo):
    d = costo = 0
    for i in range(len(v)):
        if (v[i].tipo in tipo) and v[i].costo < p:
            print(to_string(v[i]))
