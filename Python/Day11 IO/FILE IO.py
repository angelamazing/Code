# 读文件
# read(size) readlines()
try:
    f = open('/path/to/file', 'r')  # 一次性读取文件全部，打印出文件的内容
    print(f.read())
finally:
    if f:
        f.close()

""" 
with open('/path/to/file', 'r') as f:
    print(f.read())
"""
# 二进制文件
f = open('/Users/michael/test.jpg', 'rb')

# 字符编码
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')  # 取非UTF-8编码的文本文件    例如，读取GBK编码的文件
f.read()

# 写文件 传入标识符'w'或者'wb'表示写文本文件或写二进制文件
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()
""" 
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!') 
"""
