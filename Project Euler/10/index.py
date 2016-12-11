from Pythagorean import Pyth

lsc = lsb = lsa = range(1,500)

for ia in lsa:
    for ib in lsb:
        if ib > ia:
            for ic in lsc:
                if ic > ib:
                    k = Pyth(ia,ib,ic)
                    if (k == True) and (ia + ib + ic == 1000):
                        r1 = ia
                        r2 = ib
                        r3 = ic
                        break
prod = r1 * r2 * r3
print(prod)