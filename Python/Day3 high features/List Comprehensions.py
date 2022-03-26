list(range(0,100))

[x*x for x in range(1,11) if x % 2 == 0]    #[4, 16, 36, 64, 100]

#全排列
[m + n for m in 'ABC' for n in 'XYZ']   #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#同时迭代key，value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
"""
y = B
x = A
z = C
"""

#使用2个变量生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.items()] #['y=B', 'x=A', 'z=C']

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

#if else
[x if x % 2 == 0 else -x for x in range(1, 11)] #[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]