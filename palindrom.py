# sprawdzenie czy jest palindromem z zamiana znakow na male litery
# autor: Pawel, Grzesiek

def palindrom(slowo):
    """
    Funkcja sprawdza czy slowo jest palindormem
    :param text: badane slowo
    :return: True jezeli slowo jest palindromem
    """
    slowo = slowo.replace(",","").\
                  replace("?","").\
                  replace(".","").\
                  replace(" ","").\
                  lower()
    print(slowo)
    nowe_slowo = slowo[::-1]
    if nowe_slowo == slowo:
        return True
    else:
        return False

print(palindrom("O, ty z Katowic, Iwo? Tak, Zyto."))