"""
ASCII Unicode UTF-8
Python 3版本中，字符串是以Unicode编码的
"""

ord("a")  # ord()函数获取字符的整数表示
chr(65)  # chr()函数把编码转换为对应的字符

print('\u4e2d\u6587')  # 打印中文

len('abc')  # 3
len('中文')  # 2

len(b'ABC')  # 计算字节数 3
len('中文'.encode('utf-8'))  # 6 中文通常经过UTF-8 编码后通常会占用3个字节

"""
#!/usr/bin/env python3  告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*- 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
"""
