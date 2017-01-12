from lift import Elevator

elevator_1 = Elevator("OTIS")
elevator_2 = Elevator("PHILLIPS")

# Везем человека в лифте под именем OTIS
elevator_1.lift()
# Везем двоих человек в лифте под именем PHILLIPS
elevator_2.lift()
elevator_2.lift()
# Получаем информацию по лифту под именем OTIS
elevator_1.info()
# Получаем информацию по лифту под именем PHILLIPS
elevator_2.info()