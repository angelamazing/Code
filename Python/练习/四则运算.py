a = float(input())
op = input()
b = float(input())
d = {'+':a+b, '-':a-b, '*':a*b, '/':a/b if b!=0 else "divided by zero"}
res = d[op]
if type(res)==float:
    print("%.2f"%res)
else:
    print(res)
