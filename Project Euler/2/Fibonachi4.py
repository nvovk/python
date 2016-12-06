def Fibonachi(n):
    l = [0,1]
    a = 1
    l.append(a)
    i = 2
    while a < n:
        a = l[i] + l[i - 1]
        l.append(a)
        i += 1
    return l