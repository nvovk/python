from checkpol import CheckPol

num = 999*999
pol = CheckPol(list(str(num)))

while pol == False:
    num = num - 1
    pol = CheckPol(list(str(num)))

print(num)