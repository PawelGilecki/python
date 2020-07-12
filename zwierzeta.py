class Cat():
    def give_sound(self):
        print("Moew!")

class Dog():
    def give_sound(self):
        print("Bark!")

class Python():
    def give_sound(self):
        print("SSSS!")

arka_noego = [Cat(),Dog(),Python()]

for zwierze in arka_noego:
    zwierze.give_sound()