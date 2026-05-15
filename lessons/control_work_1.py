class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print("Животное издает звук")


class Dog(Animal):
    def make_sound(self):
        print("Гав-гав")


class Cat(Animal):
    def make_sound(self):
        print("Мяу-мяу")



dog = Dog("Rex", 3)
kitty = Cat("Murka", 1)


dog.make_sound()
kitty.make_sound()
kitty.set_age(2)
print(kitty.get_age())