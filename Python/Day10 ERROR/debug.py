# print

# 断言（assert）
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'  # 如果 n=0,则会抛出后面的错误
    return 10 / n


def main():
    foo('0')


# logging
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
