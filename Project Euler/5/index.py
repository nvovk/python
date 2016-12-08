from checkdiv import CheckDiv

num = 200

pol = CheckPol(num)

while pol == False:
    num = num + 20
    pol = CheckPol(num)

print(num)