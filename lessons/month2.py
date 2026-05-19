from hw5 import designations


class Car:   #Car названия файла
 # ...  #три точи заменяет pass-пусто
 #конструктор/инициализатор __init__
 #self - переводиться сам обьект (указательный обьект)
    def __init__(self, color, model):
        self.color = color
        self.model = model


    def drive_to(self, destination):
        print(f"Машина модели:  {self.model} едет в {destination}")

#инициализация обьектов
car1 = Car("белый", "марк2")
car2 = Car("черный", "BMW")
print(car1)
print(car2)
print(type("25164361"))
print(type(car1))
print(car1.color, car1.model)
car1.drive_to("Каракол")