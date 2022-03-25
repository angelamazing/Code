type(123)  # <class 'int'>


# 如果一个变量指向函数或者类，也可以用type()判断：
def abs(x):
    if x <= 0:
        return -x
    else:
        return x


my = abs
type(my)  # <class 'function'>

# 判断一个对象是否是函数
import types


def fn():
    pass


type(fn) == types.FunctionType  # True

#
