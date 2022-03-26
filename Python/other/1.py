def myfun():
    print('++')


def prinfwrapper(fun):
    def improvefun():
        print('a')
        fun()
        print('b')

    return improvefun


fun1 = prinfwrapper(myfun)
fun1()
