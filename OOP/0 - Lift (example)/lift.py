class Elevator:
    """ Simple elevator class """
    # Переменная класса. Сколько людей было перевезено ВСЕМИ лифтами
    people_lifted = 0

    # Конструктор класса. Вызывается при создании экземпляра класса
    def __init__(self, name):
        self.name = name
        # переменная класса. Количество людей перевезенных КОНКРЕТНЫМ лифтом
        self.people_lifted = 0

    # Метод перевозки людей
    def lift(self):
        print("{} lifted someone".format(self.name))
        # Увеличиваем количество людей перевезенных ЭТИМ лифтом
        self.people_lifted += 1
        # Увеличиваем количество людей перевезенных ВСЕМИ лифтами
        Elevator.people_lifted += 1

    # Метод печатающий информацию о конкретном лифте
    def info(self):
        print(self.name, "lifted", self.people_lifted, "people out of", Elevator.people_lifted)