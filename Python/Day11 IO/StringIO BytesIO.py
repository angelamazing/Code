# StringIO顾名思义就是在内存中读写str。
from io import StringIO

f = StringIO()
f.write('hello')

f.write(' ')

f.write('world!')

print(f.getvalue())  # getvalue()方法用于获得写入后的str。

f = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
