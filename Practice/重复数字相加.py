a = input('请输入关键数字: ')
n = input('请输入个数： ')
n = int(n)
a = int(a)

result = 0

for i in range(1, n + 1):
    result += i * a * (10 ** (n-i))
    print(result)

