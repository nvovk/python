def pairs(l):
    p = 0
    for i in l:
        for j in l:
            if int(i) + int(j) == 0 and abs(int(i)) == abs(int(j)):
                p += 1
    if p > 0:
        return True
    else:
        return False


def opp(l):
    if pairs(l) is True:
        for i in l:
            for j in l:
                if int(i) + int(j) == 0 and abs(int(i)) == abs(int(j)):
                    print(i,' , ',j)
                    l.remove(i)
                    l.remove(j)
                    opp(l)
    else:
        print('tst ', l)
        return l

l = [1, 2, 2, 3, 4, 4]
l1 = [1, 2, 3, 3, -2, -1, 5]

print(opp(l))
print(opp(l1))
