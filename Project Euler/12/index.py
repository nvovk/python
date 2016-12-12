from triangle import TriangleNum, DivNum

divs = 0
i = 3000
while divs < 500:
    i += 1
    num = TriangleNum(i)
    divs = DivNum(num)

print(i,divs,num)