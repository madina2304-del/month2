#Родительский класс, супер класс
class Car:  # Car названия файла
    # ...  #три точи заменяет pass-пусто
    # конструктор/инициализатор __init__
    # self - переводиться сам обьект (указательный обьект)
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print(f"Машина модели:  {self.model} едет в {destination}")

    def change_color(self, new_color):
        self.color = new_color

#(Car)- это дечерний класс, наследник подкласс
class Bus(Car):
    def __init__(self, model, color, number):
        super().__init__(color, model) #super- это обрашение к родительский класс
        self.number = number

    def drive_to(self, destination):
        print(f"Автобус едет в рейс  в: {destination}")
        super().drive_to(destination)    # это обращение к методу из родительский класс

class Truck(Car):
    def change_color(self, new_color):
        self.color = new_color
        print(f"цвет грузовика изменился на {new_color}")


car2 = Car("черный", "BMW")
car2.change_color("серый")
bus_42 = Bus("зеленный", "Mercedes", "42")
print(bus_42.color , bus_42.model)
bus_42.drive_to("Сокулук")
truck1 = Truck("Белый", "Man")
truck1.change_color("синий")
truck1.drive_to("Каракол")
car2.drive_to("Бишкек")

print(type(truck1))
print(isinstance(truck1, Truck))
print(isinstance(truck1, Car))

vehicles = [car2, truck1, bus_42]
for v in vehicles:
    v.drive_to(destination="Каракол")



