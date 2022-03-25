# list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)  # ['Michael', 'Bob', 'Tracy']
len(classmates)  # 3

classmates[0]  # 索引访问
classmates[-1]  # 直接访问最后一个元素

classmates.append('Adam')
classmates.pop(2)

L = ['Apple', 123, True]  # 类型可以不同
s = ['python', 'java', ['asp', 'php'], 'scheme']  # list嵌套
L = []

# tuple：所谓的“不变”是说，tuple的每个元素，指向永远不变
t = ('a', 'b', ['A', 'B'])
t[2][1] = 'C'
# t[0]='b' wrong
