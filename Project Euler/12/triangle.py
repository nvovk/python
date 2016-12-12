def TriangleNum(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


def DivNumx(n):
    s = 1
    for i in range(1, (n // 2 + 1)):
        if n % i == 0:
            s += 1
    return s


def DivNum(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += 1
    return s
