from types import MethodType


class Student(object):
    pass


s = Student()


# 给一个实例绑定方法
def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
s.age  # 测试结果

t = Student()


# 给所有实例绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score  # 这样所有实例都可以使用


# 限制实例的属性 这样 Student 类的实例只能绑定 name，age 属性，但这不影响子类
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
