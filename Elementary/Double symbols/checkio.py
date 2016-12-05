def CheckDouble(l,a,m):
    i = 0
    for x in l:
        if x == a:
            i = i+1
    if i > 1:
        return True
    else:
        m.append(a)