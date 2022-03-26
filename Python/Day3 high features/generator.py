# 1.把一个列表生成式的[]改成()
g = (x * x for x in range(10))
next(g)  # 0
next(g)  # 1
next(g)  # 4

for n in g:
    pass
    # print(n)    #9  16  25  36  49  64  81


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b  # t = (b,a+b)   a = t[0]  b = t[1]
        n = n + 1
    return 'done'


g = fib(5)  # 如果直接调用，相当于创建一个g，每次调用都会生成一个新的g

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
