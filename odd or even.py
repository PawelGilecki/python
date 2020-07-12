number1 = int(input("Podaj numer1 "))
number2 = int(input("Podaj numer2 "))
rest = number1%2
rest_four = number1%4
even_div = number1%number2

if even_div == 0:
    print("podzielone bez reszty")
else:
    print("roznica to ", even_div)


if rest_four == 0 and rest == 0:
    print("nr 1 to wielokrotonosc 4 i przysty")
elif rest == 0:
    print("Numer1 jest przysty")
else:
    print("numer1 jest nieparzysty")

