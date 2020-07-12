class Animal():
    def breathe(self):
        print("I am breathing")
    def move(self):
        print("I am moveing")
    def eat(self):
        print("I am eating")


class Mammals(Animal):
    def feed(self):
        print("Feed young with milk")

torbacz = Mammals()
torbacz.feed()

class Giraffe(Mammals):
    def eat_leaves(self):
        print("I am eating leaves from tree")

zyrafa = Giraffe()
zyrafa.eat_leaves()

class Cat(Mammals):
    def __init__(self, kolor = "rozowy", zeby = "40"):
        self.kolor_siersci = kolor
        self.ilosc_zyc = 9
        self.ilosc_nog = 4
        self.ilosc_zebow = zeby
    def give_sound(self):
        print("Moew!")

mruczek = Cat("zielony")
fredek = Cat()
mruczek.ilosc_zyc -= 1
print(mruczek.ilosc_zyc, mruczek.ilosc_zebow)
print(mruczek.kolor_siersci)
print(fredek.kolor_siersci)