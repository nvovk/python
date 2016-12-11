from SqS import SumSq, SqSum
from math import pow

lst = range(1,101)

pol = CheckPol(num)

while pol == False:
    num = num + 20
    pol = CheckPol(num)

print(num)