def CheckPol(l):
    n = len(l)

    i = 0
    j = n - 1

    if l[j] == 0:
        return False
    else:
        if l[i] == l[j]:
            dec = True
            if n % 2 == 0:
                while dec == True:
                    i = i + 1
                    j = j - 1
                    if l[i] == l[j]:
                        dec = True
                        if (i + 1 == j) and (l[i] == l[j]):
                            return True
                        else:
                            continue
                    else:
                        return False
                        break
            else:
                while dec == True:
                    i = i + 1
                    j = j - 1
                    if l[i] == l[j]:
                        dec = True
                        if i + 1 == j - 1:
                            return True
                        else:
                            continue
                    else:
                        return False
                    break
        else:
            return False