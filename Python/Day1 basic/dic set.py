# dic
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85, }

d['Michael']

'Bob' in d  # True
d.get('Bob')  # 得到key的value值，如果没有默认返回None
d.pop('Bob')  # 删除Bob

# set    set和dict类似，也是一组key的集合，但不存储value 可以看成数学意义上的无序和无重复元素的集合
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2
