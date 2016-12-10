from checkpol import CheckPol

pol = False
lpol = []

for i in range(100,1000):
    for j in range(100,1000):
        dob = i * j
        pol = CheckPol(list(str(dob)))
        if pol == True:
            lpol.append(dob)

print(max(lpol))