from checkio import CheckDouble

print ("Enter your list (like '1 2 3'):")
num = [int(x) for x in input().split()]
print (num)

lm = []

for x in num:
    CheckDouble(num,x,lm)

print(lm)