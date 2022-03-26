#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()

""" 
其中if name == 'main'：这句估计很多和我一样的初学者都是不求甚解。 这里作一下解释

1.name是一个变量。前后加了爽下划线是因为是因为这是系统定义的名字。普通变量不要使用此方式命名变量。 
2.Python有很多模块，而这些模块是可以独立运行的 这点不像C++和C的头文件。 
3.import的时候是要执行所import的模块的。 
4.name就是标识模块的名字的一个系统变量。这里分两种情况:假如当前模块是主模块（也就是调用其他模块的模块），
那么此模块名字就是main，通过if判断这样就可以执行“mian:”后面的主函数内容；
假如此模块是被import的，则此模块名字为文件名字（不加后面的.py），通过if判断这样就会跳过“mian:”后面的内容。
通过上面方式，python就可以分清楚哪些是主函数，进入主函数执行；并且可以调用其他模块的各个函数等等。
"""
