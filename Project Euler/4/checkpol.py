def CheckPol(l):
    n = len(l)

    i = 0
    j = n - 1

    if l[j] == 0:
        return False
    else:
        if l[i] == l[j]:
            dec = True
        else:
            return False

        while dec == True:
            if n % 2 == 0:
                if (i + 1 == j) and (l[i] == l[j]):
                    return True
                else:
                    i = i + 1
                    j = j - 1
                    continue
            else:
                if i + 1 == j - 1:
                    return True
                else:
                    i = i + 1
                    j = j - 1
                    continue
