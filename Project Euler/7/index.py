from simplenum import SimpleNum

n = 10000
ls = SimpleNum(n)

while len(ls) < 10001:
    ls = SimpleNum(n)
    n = n + 1000

print(ls[10000])