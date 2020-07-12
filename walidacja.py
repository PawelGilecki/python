#walidacja pol
#

def waliduj_pola(imie, wiek, pin, zip, email):
    """
    sprawdzanie walidacji pol
    :param imie: imie i nazwisko
    :param wiek: wiek
    :param pin: kod pin
    :param zip: kod pocztowy
    :param email: adres email
    :return:
    """
    waliduj_imie(imie)
    waliduj_wiek(wiek)
    waliduj_pin(pin)
    waliduj_zip(zip)
    waliduj_email(email)


def waliduj_email(email):
    if "@" in email:
        print("to jest email")
    else:
        print("to nie jest email")


def waliduj_zip(zip):
    if len(zip) == 6 and "-" == zip[2]:
        print("to jest poprawny kod pocztowy")
    else:
        print("to nie jest poprawny kod pocztowy")


def waliduj_pin(pin):
    if pin.isdecimal() and len(pin) == 4:
        str(pin)
        print("to jest pin")
    else:
        print("to nie jest pin")


def waliduj_wiek(wiek):
    if wiek.isdecimal():
        if int(wiek) < 150 and int(wiek) > 0:
            print("to jest wiek")
        else:
            print("wiek jest niepoprawny")
    else:
        print("to nie jest wiek")


def waliduj_imie(imie):
    if imie.istitle() and " " in imie:
        print("to jest imie")
    else:
        print("to nie jest imie")


waliduj_pola("Jan Kowalski", "188", "78915", "12-123", "abc@abc.com")