import datetime


class Person:
    def __init__(self, name, birth_date, occupation, higher_edication):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_edication = higher_edication

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_edication(self):
        return self.__higher_edication

    def introduce(self):
        edication = "есть высшее образование" if self.higher_edication else "нет высшее образование"

        print(f"Привет, меня зовут {self.name}."
              f"Моя профессия {self.__occupation}."
              f"У меня {edication}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, university):
        super().__init__(name, birth_date, occupation, higher_education)
        self.university = university

    def introduce(self):
        education = "есть высшее образование" if self.higher_edication else "нет высшее образование"
        print(f"Привет, меня зовут {self.name}."
              f"Моя профессия {self.occupation}."
              f"У меня {education}."
              f"Я учился {self.university}")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_edication, hobby):
        super().__init__(name, birth_date, occupation, higher_edication)
        self.hobby = hobby

    def introduce(self):
        education = "есть высшее образование" if self.higher_edication else "нет высшее образование"
        print(f"Привет, меня зовут {self.name}."
              f"Моя профессия {self.occupation}."
              f"У меня {education}." 
              f"Мое хобби {self.hobby}")

cl1 = Classmate ("Алмаз", "20.02.2000", "студент", True,  "АУЦА")
cl1.introduce()

fr1 = Friend("Айбек", "23.06.1999", "студент", True,  "футбол")
fr1.introduce()

