n = 20

l = [[0 for x in range(n)] for y in range(n)]

count = 1

for i in range(0,n):
    for j in range(0,n):
        l[i][j] = 1
        if i > 0 and j > 0:
            l[i][j] = l[i][j-1] + l[i-1][j]

for i in range(n):
    for j in range(n):
        count += l[i][j]

print(count)