# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


# print 内部 有一个将对象转换为 字符串 的方法，在上面我们定义了__str__就是如此
print(Student('Michael'))

s = Student('Jack')
print(s)
