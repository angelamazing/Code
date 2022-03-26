# 阶乘计算函数
def factorial(num=3):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


# 可变参数


def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 最大公约数
def gcd(a, b):
    tmp = a % b
    while (tmp != 0):
        a = b
        b = tmp
        tmp = a % b
    return b


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


# 判断素数
def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
        return True if num != 1 else False


print(is_prime(34))
