import random
from opposit import opp, pairs

n = int(input('Enter N - '))
l = []
for i in range(0,n):
    l.append(random.randint(-10, 10))

f = open('F.txt', 'w')
for i in l:
    f.write(str(i) + '\n')

f = open('F.txt', 'r')
l1 = [line.strip() for line in f]

f.close()

len1 = len(l1)
print(l1)

len2 = len(opp(l1))
print(l1)

c = (len1 - len2) / 2
print('Amount of opposites: ', int(c))



g = open('G.txt', 'w')
for i in l:
    g.write(str(i) + '\n')

g = open('G.txt', 'r')
lg = [line.strip() for line in g]
g.close()
