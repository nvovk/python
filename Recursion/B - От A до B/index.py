""" Даны два целых числа A и В. Выведите все числа от A до B включительно,
в порядке возрастания, если A < B, или в порядке убывания в противном случае. """


def printA(a, b):
    if a == b :
        return b
    elif a > b :
        print(a)
        return printA(a - 1, b)
    else:
        print(a)
        return printA(a + 1, b)

print(printA(10,5))
