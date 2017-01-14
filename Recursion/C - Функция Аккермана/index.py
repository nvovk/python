def printA(m, n):
    if m == 0 :
        return n + 1
    elif n == 0 :
        return printA(m - 1, 1)
    else:
        return printA(m - 1, printA(m, n - 1))

print(printA(0,4))
