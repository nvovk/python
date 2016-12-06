from simplenum import SimpleNum

sn = SimpleNum(600851475143)
max = sn[0]
n = 600851475143

for i in sn:
    if (n % i == 0) and (i > max):
        max = i

print(max)