# napisanie wlasnej funkcji
# autor Pawel

def przywitaj(imie, plec="k"):
    """
    Witaj z uzytkownikiem
    :param imie: imie osoby
    :param plec: string okreslajacy plec
    :return: none
    """
    if plec == "m":
        print("witaj drogi "+ imie + "! milo cie widziec")
    elif plec == "k":
        print("witaj droga " + imie + "! milo cie widziec")
    else:
        print("witaj drogo " + imie + "! milo cie widziec")

przywitaj("Pawle", "g")
przywitaj("Macku", "m")
przywitaj("Zosiu")
przywitaj("Henryk")
