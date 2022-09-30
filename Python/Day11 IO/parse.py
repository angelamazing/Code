# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
d = dict(name='Bob', age=20, score=88)

import pickle

data = pickle.dumps(d)
print(data)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。

# 用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
# f = open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()

f = open('dump.txt', 'rb')
data = pickle.load(f)
f.close()
print(data)  # 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
