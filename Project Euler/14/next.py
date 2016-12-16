def Even(n):
    a = n / 2
    return a

def Odd(n):
    a = 3 * n + 1
    return a

def EvOdd(n):
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = Even(n)
            l.append(n)
        else:
            n = Odd(n)
            l.append(n)
    return l