import math


def HasSq(n):
    x = math.ceil((math.sqrt(n)))
    if x * x == n:
        return True
    else:
        return False

def DivNum(m):
    x = 3
    n = 2
    while n <= m:
        n = 2
        num = sum([c for c in range(1, x + 1)])
        for i in range(2, math.ceil(math.sqrt(num))):
            if num % i == 0:
                n += 2
        if HasSq(num):
            n -= 1
        x += 1
    return num
