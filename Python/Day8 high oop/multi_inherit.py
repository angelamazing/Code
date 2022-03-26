# 为了解决庞大的层次继承链

class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 对于需要Runnable功能的动物，就多继承一个Runnable
class Dog(Mammal, Runnable):
    pass
