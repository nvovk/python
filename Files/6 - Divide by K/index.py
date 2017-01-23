import random

k = int(input('Enter K - '))
n = int(input('Enter N - '))

l = []
for i in range(0,n):
    l.append(random.randint(0, 100))

f = open('F.txt', 'w')
g = open('G.txt', 'w')

for i in l:
    f.write(str(i) + '\n')

f = open('F.txt', 'r')
lf = [line.strip() for line in f]

for i in lf:
    if int(i) % k == 0:
        g.write(str(i) + '\n')

g = open('G.txt', 'r')
lg = [line.strip() for line in g]

f.close()
g.close()

print(lg)