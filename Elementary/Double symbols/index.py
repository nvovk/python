print ("Enter your list (like '1 2 3'):")
num = [int(x) for x in input().split()]
print (num)


def CheckDouble(l,a,m):
    i = 0;
    for x in l:
        if x == a:
            i = i+1
    if i > 1:
        return True
    else:
        m.append(a)
            
lm = []

for x in num:
    CheckDouble(num,x,lm)
   
print(lm)