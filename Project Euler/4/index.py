from checkpol import CheckPol

num = 999 * 999

while True:
    pol = CheckPol(list(str(num)))
    if pol == None:
        num = num - 1
        False
    else:
        True

print(num)




