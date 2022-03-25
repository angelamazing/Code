1. eval(input)

   eval()能够以Python[表达式](https://so.csdn.net/so/search?q=表达式&spm=1001.2101.3001.7020)的方式解析并执行字符串，并将返回结果输出。eval()函数将去掉字符串的两个引号，将其解释为一个变量。

   eval()会去掉字符串最外层的引号，然后当做Python语句执行

   a. 处理数字

   单引号，双引号，eval()函数都将其解释为int类型；三引号则解释为str类型。

   eval('2')	# 2

   eval('"2"')	# '2'

