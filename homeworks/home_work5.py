class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"

class ClowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"{self.live()} + {self.superpower()}"

class ViralStreamer(TikToker, Mutant):
    def ultimate_content(self):
        return f"{self.live()} + {self.viral()} + {self.superpower()}"

class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
         return f"{self.live()} + {self.earn()} + {self.viral()}"

g1 = ClowStreamer()
v1 = ViralStreamer()
d1 = DonateMage()

print(g1.ultimate_content())
print(v1.ultimate_content())
print(d1.ultimate_content())

print(ClowStreamer.mro())
print(ViralStreamer.mro())
print(DonateMage.mro())