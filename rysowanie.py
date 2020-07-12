# rysowanie kwadratu
# autor Pawel

bok = int(input("Podaj dlugosc boku "))

for i in range(bok):
    print("*" * (bok - i))

for i in range(bok - 1):
    print("*" * (i+2))
