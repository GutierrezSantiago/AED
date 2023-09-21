# def Hades(n1, n2, n3):
#     u = n1**1
#     d = n2**2
#     t = n3**3
#     return (u, d, t)
#
#
#
# x = int(input("N1: "))
# y = int(input("N2: "))
# z = int(input("N3: "))
# (a, b, c) = Hades(x, y, z)
# print(a)
# print(b)
# print(c)
import random

for i in range(5):
    a = random.randint(1,5)
    b = random.choices(("Hades", "Zeus", "Hestia", "Demeter", "Ares"))
    c = random.random()*100
    t = (a, b, c)
    if i == 0:
        x = t,
    else:
        x += t,

l = len(x)
s = x[0-l]
m = x[1-l]
n = x[2-l]
print(x)
print(s)
print(m)
print(n)
a, b, c = s
d, e, f = m
g, h, i = n
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

