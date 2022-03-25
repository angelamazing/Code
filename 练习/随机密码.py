import random

strList1 = [chr(i) for i in range(97, 123)]
strList2 = [chr(i) for i in range(65, 91)]
numberList = [str(i) for i in range(0, 10)]
L = strList1 + strList2 + numberList
print(len(L))


def printPassword():
    seed = int(input(''))
    number = int(input(''))
    nInt = int(input(''))
    random.seed(seed)
    for i in range(0, number):
        tem = []
        result = []
        for j in range(0, nInt):
            tem.append(random.randint(0, 61))
        print(tem)
        for k in range(0, nInt):
            key = tem[k]
            result.append(L[key])
        result = ''.join(result)
        print(result)


printPassword()
