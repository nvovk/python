import random
from item import item

n = int(input('Enter N - '))
l = []
for i in range(0,n):
    l.append(random.randint(0, 10))

f = open('F.txt', 'w')
for i in l:
    f.write(str(i) + '\n')

f = open('F.txt', 'r')
l1 = [line.strip() for line in f]

f.close()

l2 = []

for i in range(1, len(l)+1):
    l2.append(item(l1,i))

print('List - ', l1)

g = open('G.txt', 'w')
for i in l2:
    g.write(str(i) + '\n')

g = open('G.txt', 'r')
lg = [line.strip() for line in g]
g.close()

print('Multiple list - ', lg)