from abc import ABCMeta, abstractmethod


class Worker:
    # Загальна інформація про кожного працівника
    def __init__(self, id, n, s, a):
        self.id = id
        self.name = n
        self.surname = s
        self.sal = a

    __metaclass__ = ABCMeta

    @abstractmethod
    def salary(self):
        pass

    def out(self):
        print(self.id,' ',self.surname,' ',self.name,' ',self.salary(),'$')



class PerHour(Worker):
    # Підклас працівників з погодинною оплатою
    def salary(Worker):
        S = round(20.8 * 8 * Worker.sal)
        return S


class Fixed(Worker):
    # Підклас працівників з фіксованою оплатою
    def salary(Worker):
        S = Worker.sal
        return S


#a = Fixed(1,'Name','Surn',150)
#a.out()