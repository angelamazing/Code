"""
可以直接作用于for循环的数据类型有以下几种:
1.可以直接作用于for循环的数据类型有以下几种
2.一类是generator，包括生成器和带yield的generator function
    可以直接作用于for循环的对象 Iterable(要与Iterator区分开)
"""

from collections.abc import Iterable

L = [1, 2, 3]
isinstance(L, Iterable)  # True

# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
from collections.abc import Iterator

isinstance((x for x in range(10)), Iterator)  # True
isinstance([], Iterator)  # False
isinstance(iter([]), Iterator)  # True

# 那么for的实现？
for x in [1, 2, 3, 4, 5]:
    pass

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
    except  StopIteration:
        break
