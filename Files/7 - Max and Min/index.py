import random

n = int(input('Enter N - '))

l = []
for i in range(0,n):
    l.append(random.uniform(0,100))

f = open('F.txt', 'w')

for i in l:
    f.write(str(i) + '\n')

f = open('F.txt', 'r')
lf = [line.strip() for line in f]

m1 = round(float(max(lf)),2)
m2 = round(float(min(lf)),2)

sum = round(m1 + m2,2)

print(m1, ' - maximum')
print(m2, ' - minimum')
print(sum, ' - sum')

