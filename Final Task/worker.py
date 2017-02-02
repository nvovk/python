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


class PerHour(Worker):
    # Підклас працівників з погодинною оплатою
    def salary(Worker):
        S = 20.8 * 8 * Worker.sal
        return S


class Fixed(Worker):
    # Підклас працівників з фіксованою оплатою
    def salary(Worker):
        S = Worker.sal
        return S

a = Fixed('n1', 's1', 500)
b = PerHour('n2', 's2', 5)

a.salary()
b.salary()











#lift(self):
  #      print("{} lifted someone".format(self.name))
  #      # Увеличиваем количество людей перевезенных ЭТИМ лифтом
  #      self.people_lifted += 1
  #      # Увеличиваем количество людей перевезенных ВСЕМИ лифтами
  #      Elevator.people_lifted += 1

    # Метод печатающий информацию о конкретном лифте
   # def info(self):
   #     print(self.name, "lifted", self.people_lifted, "people out of", Elevator.people_lifted)

a) Упорядочить всю последовательность работников по убыванию среднемесячного заработка.
При совпадении зарплаты – упорядочивать данные по алфавиту по имени.
Вывести идентификатор работника, имя и среднемесячный заработок для всех элементов списка.
b) Вывести первые 5 имен работников из полученного в пункте а) списка.
c) Вывести последние 3 идентификатора работников из полученного в пункте а) списка.
d) Организовать запись и чтение коллекции в/из файл.
e) Организовать обработку некорректного формата входного файла.