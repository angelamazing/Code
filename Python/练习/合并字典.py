dic1=eval(input())
dic2=eval(input())
for i in dic1:
    if i in dic2:
        dic1[i]+=dic2[i]
dic2.update(dic1)
li1=[]
li2=[]
for i in list(dic2):
    if isinstance(i,str):
        li2.append(i)
    else:
        li1.append(i)
li=sorted(li1)+sorted(li2)
for i in range(len(li)):
    if i==0:
        print('{',end='')
    if isinstance(li[i],str):
        print(f'"{li[i]}":{dic2[li[i]]}',end='')
    else:
        print(f'{li[i]}:{dic2[li[i]]}',end='')
    if i!=len(li)-1:
        print(',',end='')
    else:
        print('}',end='')