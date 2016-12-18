n = 2
p = 1000
s = 0

sq = list(str(n ** p))

for i in range(len(sq)):
    s += int(sq[i])

print(s)