lambda x: x * x
""" 
相当于：
def f(x):
    return x*x
"""

def build(x, y):
    return lambda: x * x + y * y

my = build(1,2)
my()    #5