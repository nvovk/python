from Pythagorean import Pyth

i1 = 1
i = j = k = 0
m1 = m2 = m3 = 1
pol = 0

lsa = range(i1, 1000)
while m1 != 0:
    j1 = i1 + 1
    lsb = range(j1, 999)
    while m2 != 0:
        k1 = j1 + 1
        lsc = range(k1, 998)
        m3 = 1
        while m3 != 0:
            if Pyth(lsa[i],lsb[j],lsc[k]) == True:
                if lsa[i] + lsb[j] + lsc[k] == 1000:
                    print('a - ',lsa[i],'; b - ',lsb[j],'; c - ',lsc[k])
                    pol = 1
                    break
            k += 1
            if k == len(lsc)-1:
                m3 = 0
        j +=1
        if j == len(lsb)-1:
            m2 = 0
            break
    i += 1
    if pol != 1:
        m2 = 1