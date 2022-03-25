import math


# 空函数
def nop():
    pass


age = 20

if age >= 18:
    pass


# 定义完善的函数，包括抛出错误
def my_abs(x):
    if not isinstance(x, (int, float)):  # x 既不是 int 也不是 float
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值，实际上是转化为tuple


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    tmp = b * b - 4 * a * c
    if tmp < 0:
        return '无解'
    tmp = math.sqrt(tmp)
    return (-b + tmp) / (2 * a), (-b - tmp) / (2 * a)


print(quadratic(1, 2, 8))
