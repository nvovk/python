""" Дано натуральное число n. Выведите все числа от 1 до n. """

def printA(n):
    if n == 1:
        return 1
    print(n)
    return printA(n - 1)

print(printA(5))