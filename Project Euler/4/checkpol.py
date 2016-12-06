def CheckPol(l):
    n = len(l)

    i = 0
    j = n-1

    while l[i] == l[j]:
            i = i+1
            j = j-1
            if n % 2 == 0:
                if i+1 == j:
                    return True
                else:
                    continue
            else:
                if i+1 == j-1 :
                    return True
                else:
                    continue