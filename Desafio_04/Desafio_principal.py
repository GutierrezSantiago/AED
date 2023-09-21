import pickle
import os.path
import math

class Point:
    def __init__(self, cx, cy, desc='p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc


def to_string(point):
    r = str(point.descripcion) + '(' + str(point.x) + ', ' + str(point.y) + ')'
    return r


def distance_between(p1, p2):
    # calcular "delta y" y "delta x"
    dy = p2.y - p1.y
    dx = p2.x - p1.x

    # Distancia entre ellos... Pitágoras...
    return math.sqrt(pow(dx, 2) + pow(dy, 2))


def deserializacion(FD):
    m = open(FD, "rb")
    tsize = os.path.getsize(FD)
    v = []
    while m.tell() < tsize:
        point = pickle.load(m)

        v.append(point)

    return v


def distancia_minmax(FD):
    v = deserializacion(FD)
    dmax = 0
    dmin = distance_between(v[0], v[1])
    n = len(v)

    for i in range(0, n-1):
        for j in range(i+1, n):
            d = distance_between(v[i],v[j])
            if d < dmin:
                dmin = d
            if d > dmax:
                dmax = d

    return dmin, dmax


def test():
    dmin, dmax = distancia_minmax("puntos.df4")
    print(dmin)
    print(int(dmin))
    print(dmax)
    print(int(dmax))


if __name__ == "__main__":
    test()
