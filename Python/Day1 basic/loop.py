# 第一种循环
names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(name)

sum = 0
for x in range(0, 5, 2):
    sum += x

print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
