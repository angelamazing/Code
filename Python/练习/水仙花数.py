'''
Author: your name
Date: 2022-03-25 13:03:30
LastEditTime: 2022-03-25 13:12:47
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \python_practice\练习\水仙花数.py
'''

def isShui(inputNumber):
    if type(inputNumber) != int:
        pass
    if inputNumber >1000 or inputNumber <100:
        pass
    number = inputNumber
    m = number // 100
    number -= m*100
    n = number // 10
    number -= n*10
    p = number
    
    if m**3 + n**3 + p**3 == inputNumber:
        print("是水仙花数")
    else:
        print("不是")

while(1):
    n = eval(input())
    isShui(n)