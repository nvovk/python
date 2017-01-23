def pairs(l):
    p = 0
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if int(l[i]) + int(l[j]) == 0 and abs(int(l[i])) == abs(int(l[j])):
                p += 1
    if p > 0:
        return True
    else:
        return False


def opp(l):
    if pairs(l) is True:
        for i in range(0, len(l) - 1):
            for j in range(0, len(l) - 1):
                if int(l[i]) + int(l[j]) == 0 and abs(int(l[i])) == abs(int(l[j])):
                    l.remove(l[i])
                    l.remove(l[j])
                    opp(l)
    else:
        return l