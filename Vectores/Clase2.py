def validate(inf):
    n = inf
    while n <= inf:
        n = int(input("Ingrese un número(mayor a " + str(inf) + "): "))
        if n <= inf:
            print("Error! Se pidió mayor a " + str(inf) + ".")
    return n


def read(v):
    n = len(v)
    for i in range(n):
        v[i] = int(input("Ingrese un número: "))


def compare_arrays(v, w):
    n = len(v)
    m = len(w)
    y = []
    for i in range(n):
        for j in range(m):
            if v[i] == v[j]:
                if not(v[j] in y):
                    y.append(v[i])
    return y

def test():
    n = validate(0)
    m = validate(0)
    v = n * [0]
    w = m * [0]
    read(v)
    read(w)
    y = compare_arrays(v, w)
    print(v)
    print(w)
    print(y)


if __name__ == "__main__":
    test()
