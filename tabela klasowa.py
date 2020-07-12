class Person ():
    def __init__(self, name, email, size):
        self.name = name
        self.email = email
        self.size = size

lista_osob = [Person("Jan Kowalski", "email@2p.pl", "44"),
              Person("Maciek Szwedzki", "abc@2p.pl", "44")]

for osoba in lista_osob:
    print(osoba.name.center(20) + osoba.email.center(20) + osoba.size.center(5))
