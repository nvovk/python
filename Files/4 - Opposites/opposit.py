def pairs(l):
    p = 0
    for i in l:
        for j in l:
            if int(i) + int(j) == 0 and abs(int(i)) == abs(int(j)):
                if int(i) != 0:
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
                    if int(i) != 0:
                        print(i, ', ', j)
                        l.remove(i)
                        l.remove(j)
                        return opp(l)
    else:
        return l
