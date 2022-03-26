'''
Author: your name
Date: 2022-03-25 12:57:06
LastEditTime: 2022-03-25 13:02:28
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_practice\练习\猜数.py
'''

from random import randint


def GussNumber():
    number = randint(0,100)
    i = 1
    while(i< 8):
        n = eval(input())
        if n<number:
            print("猜小了")
        if n>number:
            print("猜大了")
        if n == number:
            print("你猜对了")
            return 
        i = i+1
    print("你的智商不足")

GussNumber()
