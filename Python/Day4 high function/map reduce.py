# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
from functools import reduce


def pf(x):
    return x * x


def add(x, y, f):
    return f(x) + f(y)


print(add(1, 2, pf))

# map  左边的函数作用于右边的列表
list(map(str, [1, 2, 3, 4, 5, 6, 7]))  # ['1', '2', '3', '4', '5', '6', '7']


# reduce


def myadd(a, b):
    return a + b


def fn(x, y):
    return x * 10 + y


def chartonum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


reduce(myadd, [1, 2, 3, 4, 5])  # 25

# 完成了string to number
result = reduce(fn, map(chartonum, '12646'))  # 12646

# 整理下
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


""" 
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s)) 
"""
