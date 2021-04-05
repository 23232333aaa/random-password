import random
ls=['0','1','2','3','4','5','6','7','8','9',',','.','/',';','\'']
ls2='abcdefghijklmnopqrstuvwxyz'
ls3='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a=random.sample(ls,5)
b=random.sample(ls2,5)
c=random.sample(ls3,5)
for Pass in a+b+c:
    print(Pass,end='')
