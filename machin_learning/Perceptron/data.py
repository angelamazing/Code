import numpy as np
import matplotlib.pyplot as plt

def getData():
    data = np.loadtxt('hw1_15_train.dat')
    x = data[:, :-1]
    y = data[:,-1]
    n = x.shape[0]
    tmp = np.ones(n).reshape((n,1))
    x = np.concatenate((tmp,x),axis=1)
    return x,y

def randData():
    x =  np.random.randn(800).reshape(400,2)
    y =  np.random.randint(-1,1,(400,1))
    y[y==0]=1
    n = x.shape[0]
    tmp = np.ones(n).reshape((n,1))
    x = np.concatenate((tmp,x),axis=1)
    return x,y

