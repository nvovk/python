from checkdiv import CheckDiv

num = 200

pol = CheckDiv(num)

while pol == False:
    num = num + 20
    pol = CheckDiv(num)

print(num)