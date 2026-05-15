class Person:
    def __init__(self, name, birth_date, profession):
        self.name = name
        self.birth_date = birth_date
        self.profession = profession

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родилась {self.birth.date}, работаю {self.profession}")
        
class Classmate(Person):
    def __init__(self, name, birth_date, profession, group_name):
        super().__init__(name, birth_date, profession)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник из группы {self.group_name}, родилься {self.birth_date}, работаю {self.profession}")

class Friend(Person):
    def __init__(self, name, birth_date, profession, hobby):
        super().__init__(name, birth_date, profession)
        self.hobby = hobby
    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, я твой друг,  родилься {self.birth_date}, работаю {self.profession}. Мой хобби {self.hobby}")

classmate1 = Classmate("Бектур", "05.12.2000", "программистом", "PY-24-1")
classmate2 = Classmate("Айдана", "15.08.2001", "Дизайнером", "Ux-24-2")
friend1 = Friend("Алмаз", "05.12.1999", "программистом", "играть в футбол")
friend2 = Friend("Сафия", "10.03.2003", "поварам", "ходить в горы")

print("===Одноклассники")
classmate1.introduce()
classmate2.introduce()

print("\n===Друзья===")
friend1.introduce()
friend2.introduce()


