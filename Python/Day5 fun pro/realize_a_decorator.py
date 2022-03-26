#假设我们现在想统计一个方法的执行时间
import time

def hello():
    start = time.time() # 开始时间
    time.sleep(1)       # 模拟执行耗时
    print ('hello')
    end = time.time()   # 结束时间
    print ('duration time: %ds' % int(end - start) )# 计算耗时

hello()

#first edition
import time

def timeit(func):   # 计算方法耗时的通用方法
    start = time.time()
    func()          # 执行方法
    end = time.time()
    print (('duration time: %ds') % int(end - start))

def hello():
    time.sleep(1)
    print ('hello')

timeit(hello)   # 调用执行

#second edition 这也是装饰器的内部实现
import time
from functools import wraps

def timeit(func):
    @wraps(func)  # 使用 wraps 装饰内部方法inner，这样第55输出的就是hello 而不是inner
    def inner():
        start = time.time()
        func()
        end = time.time()
        print( ('duration time: %ds') % int(end - start))
    return inner

def hello():
    time.sleep(1)
    print ('hello')

hello = timeit(hello)   # 重新定义hello
hello()       # 像调用原始方法一样使用

#语法糖
@timeit   # 相当于 hello = timeit(hello)
def hello():
    time.sleep(1)
    print ('hello')

hello()
print(hello.__name__)