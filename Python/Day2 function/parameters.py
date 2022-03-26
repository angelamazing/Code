# 1位置参数
# 2默认参数   默认参数必须指向不变对象
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 3可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3, 4, 5))
print(calc(*[1, 2, 3, 4, 5]))  # 这样 list和tuple 转换为可变参数传进来


# 4关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('bob', 23, city='beijing')
