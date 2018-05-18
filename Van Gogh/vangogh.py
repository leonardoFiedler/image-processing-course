#Aprendizado do algoritmo de Van Gogh
import math as math

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

def CCW(p1, p2, p3):
    value = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

    if (value < 0.000001):
        return True
    else:
        return False


def area(p1, p2, p3):
    return math.fabs((p1.x * p2.y - p1.y * p2.x + p1.y * p3.x - p1.x * p3.y + p2.x * p3.y - p2.y * p3.x) / 2)

#Inicio do Programa
p1 = Point(0, 0)
p1.x = 1
p1.y = 1

p2 = Point(0, 0)
p2.x = 1
p2.y = 3

p3 = Point(0, 0)
p3.x = 3
p3.y = 1

# Quadrado
print("Quadrado")
print (CCW(p1, p2, p3))
print (area(p1, p2, p3))

# https://en.wikipedia.org/wiki/Graham_scan
# Hexagono
print("Hexagono")
arr = [Point(0, 6), Point(4, 9), Point(6,7), Point(7,4), Point(5, 1), Point(1, 1)]

a = 0
i = 0

for x in arr[:]:
    if (i == 0):
        i += 1
        continue

    if (i + 1 == len(arr)):
        break

    a += area(arr[0], x, arr[i + 1])
    i += 1

print(a)
#Fim do programa