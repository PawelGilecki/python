import random

rn_number = str(random.randrange(1000, 9999, 4))

for pos1, char1 in enumerate(rn_number):
    position_number = [pos1, char1]
    print(position_number)

user = input("Podaj 4 cyfrowa liczbe: ")

for pos2, char2 in enumerate(user):
    user_position = [pos2, char2]
    print(user_position)