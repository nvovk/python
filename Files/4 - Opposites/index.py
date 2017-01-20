import random

n = int(input('Enter N - '))

l = []
for i in range(n):
    l.append(random.randint(-10,10))


f = open('F.txt', 'w')
for i in l:
    f.write(str(i) + '\n')


f = open('F.txt', 'r')
l1 = [line.strip() for line in f]
l2 = l1

print(l1)

d = 0

for i in range(0, len(l1)-1):
    for j in range(0, len(l2)-1):
        if (l1[i] + l2[j] == 0) and (abs(l1[i]) == abs(l2[j])):
            print(l1[i])
            l1.remove(l1[i])
            l2.remove(l2[j])
            d += 1

print(l1)
print(l2)
print(d)