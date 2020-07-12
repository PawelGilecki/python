import random

ran_num = random.randint(1, 9)
user = 0
while user != "q":
    user = input("Podaj cyfre od 1 do 9 ")
    if user == "q":
        break
    user = int(user)
    if ran_num == user:
        print("Wygrales")
    elif ran_num < user:
        print("podaj mniejsza cyfre")
    else:
        print("Podaj wieksza cyfre")