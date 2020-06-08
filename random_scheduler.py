from random import randrange
from random import shuffle
import random
from pprint import pprint
#b = 1014
b = 984
   
c = []
while b > 0 : 
    a = randrange(0,11)
    b = b - a
    c.append(a)
c.append(b)
print(c)

sum = 0
for i in c :
    sum += i
print(sum) 
print(len(c))




# a = [{'b' : 2},{'b' : 3}]
# print(a[0]['b'])


# c = list(item for item in a if item['b']==2)
# d = a.index(c[0])
# print(d)
aasd = []

if not aasd : print(1)