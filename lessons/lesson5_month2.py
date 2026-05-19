class Animal:
    def move(self):
        print("животное двигается")


class Swimming(Animal):
    def move(self):
        print("плавает")

#pep8      command


class Flying(Animal):
    def move(self):
        print("летает")

class Duck(Swimming,Flying):
    def move(self):
        super().move()
        print("утка плавает и летает")

duck = Duck()
duck.move()
print(Duck.__mro__)  #metod resolition order

bird = Flying()
bird.move()
print(Flying.__mro__)