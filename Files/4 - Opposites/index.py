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

print(l1)

l2 = opp(l1)

print(l)
print(l1)
print(l2)
print(c)

c = (len(l) - len(l1)) / 2

print(l1)
print(l2)
print(c)
