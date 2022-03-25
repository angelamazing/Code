# 随机梯度下降算法（SGD，根据时间复杂度）
# 批量梯度下降算法（BGD，根据数据量的大小）
# 小批量梯度下降算法（MBGD，算法准确性）

# y=x**2+2x+1

def gradient(x):
    return 2 * x + 2


def main():
    x_old = 1
    x_new = 5
    error = 0.0000001
    distance = 0.01
    while abs(x_new - x_old) > error:
        x_old = x_new
        x_new = x_old - distance * gradient(x_old)
    return x_new


print(main())
