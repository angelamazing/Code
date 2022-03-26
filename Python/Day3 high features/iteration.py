d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

# 如何判断是否可以迭代？
from collections.abc import Iterable
from typing import Iterator

isinstance('abc', Iterator)  # 可迭代，返回True
isinstance(123, Iterable)  # False

# 下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1,), (2, 2), (3, 3)]:
    print(x, y)
