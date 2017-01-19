import random

n = int(input('Enter N - '))

l = []
for i in range(n):
    l.append(random.uniform(0,100))

f = open('F.txt', 'w')
for i in l:
    f.write(str(i) + '\n')

f = open('F.txt', 'r')
lf = [line.strip() for line in f]

d = 1
for i in lf:
    d *= float(i)

print(d)