import math
from itertools import product
#1A
lis = ['Henning', 'Hans', 'Carlos', 'Larsen', 'Karlerne']
l = 'H'
out = [i for i in lis if i[0].lower() == l.lower()]
print(str(out))

#1B
numb = [i ** 3 for i in range(1, 101)]
print(numb)

#1C
result = []
for l in lis:
    result.append((len(l), l))
print(result)

#1D
result = ""
string = "H3ll0 wh0 4r3 y0u?"
for i in string:
    if i.isdigit():
        result = result +i
print(result)

#1E
dice = set((d1,d2) for d1 in range(1,7) for d2 in range(1,7))
print(dice)

#2A
naDict = {obj:len(obj) for obj in lis}
print(naDict)

#2B
nuLis= [29,35,42,86,108,200]
nuDict= {obj:math.sqrt(obj) for obj in nuLis}
print(nuDict)  

#3
dice = 2
choices = list(product(range(1, 7), repeat=dice))
dsum ={obj:0 for obj in range(2,13)}
for i in choices:
    dsum[sum(i)]+=1
for obj in dsum:
    dsum[obj] = dsum[obj]/36*100
print(dsum)