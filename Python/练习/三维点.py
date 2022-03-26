import math


def readPoint():
    coord = input().split(',')
    for i in range(3):
        try:
            coord[i] = int(coord[i])
        except:
            coord[i] = 0
    coord = tuple(coord)
    return coord


def distance(point):
    x = pow(point[0], 2) + pow(point[2], 2)
    y = pow(point[1], 2)
    s = math.sqrt(x + y)
    return s
