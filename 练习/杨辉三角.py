def jiecheng(j, i):  # 计算组合数   i为上面的数 j下面
    m = 1
    n = 1  # 下面的大家都知道   不知道问初中老师 排列组合
    for t in range(j, 0, -1):
        m *= t
    for k in range(i - j + 1, i + 1):
        n *= k
    return n / m


def printYanghui(n):
    for i in range(n, 0, -1):  # 控制行数
        for j in range(i - 1, 0, -1):  # 进行空格的打印
            print(" ", end='')
        for k in range(0, n - i + 1):  # 进行元素的计算
            if k == 0:  # 第一个数直接打印1 （1后面有个空格）
                print("1 ", end='')
                continue
            if k == n - i:  # 最后一个数直接打印1 （注意空格）
                print("1 ", end='')
                continue
            else:
                print("%d" % (jiecheng(k, n - i)), end=' ')  # 其他数进行 组合数计算  定义一个“jiecheng()”函数
        print()
