from data import getData,randData
import numpy as np
import matplotlib.pyplot as plt


x,y = getData() #这里可以收敛，因为样本数据是线性可分的
# x,y =randData() 这里并不会收敛，因为生成的随机数据大概率是线性不可分的
w = np.zeros(x.shape[1]).reshape(1,x.shape[1])


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def PLA(w,x,y, step=0):
    currentNum = 0
    index = 0
    isFinished = 0
    n = x.shape[0]
    while isFinished == 0:
        temp = np.dot(x[index], w.T)
        tmp = sign(temp)
        if tmp == y[index]:
            currentNum += 1
        else:
            w = w + y[index] * x[index]
            step = step + 1
            currentNum = 0
            print("step: ", step, " ", "index= ", index, " is wrong")
        if index == n - 1:
            index = 0
        else:
            index += 1
        if currentNum == n:
            isFinished = 1
    print("total step: ", step)
    return w



w = PLA(w,x,y)
print(w)





if __name__ == '__main__':
    pass


