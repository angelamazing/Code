# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # 外部代码要获取name和score
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 外部代码要更改name和score
    # 这样可以检查参数 避免无效传入
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
