from worker import *


def sorting(l):
    for i in range(0, len(l)-1):
        # Сортування по зарплаті
        if l[i].salary() < l[i + 1].salary():
            a = l[i]
            l[i] = l[i + 1]
            l[i + 1] = a
            return sorting(l)
        # Сортування по прізвищу
        elif l[i].salary() == l[i+1].salary():
            if l[i].surname > l[i + 1].surname:
                a = l[i]
                l[i] = l[i + 1]
                l[i + 1] = a
                return sorting(l)
            elif l[i].surname == l[i + 1].surname:
                # Сортування по імені
                if l[i].name > l[i + 1].name:
                    a = l[i]
                    l[i] = l[i + 1]
                    l[i + 1] = a
                    return sorting(l)
    return l


def firstfive(l):
    # Перші 5 працівників зі списку
    for i in range(0,5):
        try:
            l[i].out()
        except IndexError:
            print('No more workers in the list')
            break


def lastthree(l):
    # Останні 3  працівники зі списку
    if len(l) < 3:
        print('There are less than 3 workers in the list')
    else:
        for i in range(len(l) - 3,len(l)):
            l[i].out()

