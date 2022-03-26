class Animal(object):  # 编写Animal类
    def run(self):
        print("Animal is running...")


class Dog(Animal):  # Dog类继承Amimal类，没有run方法
    pass


class Cat(Animal):  # Cat类继承Animal类，有自己的run方法
    def run(self):
        print('Cat is running...')

    pass


class Car(object):  # Car类不继承，有自己的run方法
    def run(self):
        print('Car is running...')


class Stone(object):  # Stone类不继承，也没有run方法
    pass


"""
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法
对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
"""


def run_twice(animal):
    animal.run()  # 只要保证animal 有run 方法 不需要保证run_twice是animal家族
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Car())
""" run_twice(Stone()) 这个就会出错，没有run方法"""

# 判断一个变量是否是某一个类型
c = Dog()
isinstance(c, Dog)  # True
isinstance(c, Animal)  # True
