def issame(l,a):
    p = 0
    for i in l:
        if i == a:
                p +=1
    if p > 1:
        return True
    else:
        return False

def delsame(l,a):
    if issame(l,a) is True:
        l.remove(a)
        return delsame(l,a)
    else:
        return l
