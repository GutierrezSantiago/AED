def linear_search(v, x):
    for i in range(len(v)):
        if x == v[i]:
            return i

    return -1


def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1

    return -1


def shell_sort(v):
    n = len(v)
    h = 1

    while h <= n // 9:
        h = 3*h + 1

    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y.importe < v[k].importe:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3
