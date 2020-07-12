# zgadywanie cyfry
# autor Pawel

liczba = 500

while True:
    gracz = int(input("Zgadnij liczbe "))
    if gracz > liczba:
        print("Liczba zbyt wysoka")
    elif gracz < liczba:
        print("Liczba zbyt niska")
    else:
        print("trafiles")
        break
