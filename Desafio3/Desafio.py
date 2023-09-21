import soporte
v = soporte.vector_unknown_range(300000)


def validate(inf):
    n = inf
    while n <= inf:
        n = int(input("Ingrese un número mayor a 0 para buscar en el arreglo:"))
        if n <= inf:
            print("¡Error! Se pidio mayor a 0.")
    return n


def search(x, num):
    for i in range(len(num)):
        if num[i] == x:
            return i
    return -1


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


def principal():
    num = []
    cont = []
    v = soporte.vector_unknown_range(300000)
    for i in range(len(v)):
        n = search(v[i], num)
        if n == -1:
            num.append(v[i])
            cont.append(1)
        else:
            cont[n] += 1
    print(num)
    print(cont)
    print(len(num))
    j, k = valor_modal(cont)
    print("Valor modal: ", num[k])
    print("Frecuencia del valor modal: ", j)



if __name__ == "__main__":
    principal()
