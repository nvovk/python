import random
from same import issame, delsame

n = int(input('Enter N - '))
l = []
for i in range(0,n):
    l.append(random.randint(0, 10))

f = open('F.txt', 'w')
for i in l:
    f.write(str(i) + '\n')

f = open('F.txt', 'r')
l = [line.strip() for line in f]
f.close()

print(l)

for i in l:
    delsame(l,i)

g = open('G.txt', 'w')
for i in l:
    g.write(str(i) + '\n')

g = open('G.txt', 'r')
lg = [line.strip() for line in g]
g.close()

print(lg)