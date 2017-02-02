"""
def sorting(l):
    for i in range(0, len(l)-1):
        if l[i] < l[i+1]:
            a = l[i]
            l[i] = l[i+1]
            l[i+1] = a
            return sorting(l)
    return l

l = ['aaa', 'ddd', 'c', 'xa', 'bo', 'b']
print(sorting(l))


def sorting(l):
    for i in range(0, len(l)-1):
        # Сортування по зарплаті
        if l[i] < l[i+1].salary:
            a = l[i]
            l[i] = l[i+1]
            l[i+1] = a
            return sorting(l)
        # Сортування по прізвищу
        elif l[i].salary == l[i+1].salary:   # Сортування по імені
            if l[i].salary < l[i + 1].salary:
                a = l[i]
                l[i] = l[i + 1]
                l[i + 1] = a
                return sorting(l)

    return l
"""

l = [1, 2]

for i in range(len(l) - 3,len(l)):
    try:
        print(l[i])
    except IndexError:
        print('There are less than 3 workers in the list')
        break



