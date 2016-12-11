def SumSq(ls):
    sq = 0

    for i in ls:
        sq = sq + i*i
    return sq

def SqSum(ls):
    sum = 0

    for i in ls:
        sum = sum + i

    sq = sum * sum

    return sq
