from next import EvOdd

num = 999999
maxL = 0

while num > 100000:
    l = EvOdd(num)
    lenM = len(l)
    if lenM > maxL:
        ls = num
        maxL = lenM
    else:
        num -= 1

print(ls)
