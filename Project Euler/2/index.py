from Fibonachi4 import Fibonachi

f = Fibonachi(4000000)
sum = 0

for i in f:
    if i % 2 == 0:
        sum = sum + i

print('Sum of the even-valued terms: ',sum)