from SqS import SumSq, SqSum

num = range(1,101)

s1 = SumSq(num)
s2 = SqSum(num)

dif = s2 - s1

print(dif)