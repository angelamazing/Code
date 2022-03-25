def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
f()  # 这里才调用


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
f1()  # 9
f2()  # 9
f3()  # 9
""" 
这里为什么都是9呢？
第一，返回的函数引用了变量i
第二，它并非立即执行
第三，等三个函数都返回时，所引用的变量i已经变成了3
"""


def count():
    def f(j):
        def g():  # 创建的这个函数绑定了每次循环j的值，并且已经执行，返回了g
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


[f1, f2, f3] = count()
f1()  # 1
f2()  # 4
f3()  # 9
