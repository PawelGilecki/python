# listy
#Pawel, Grzegorz

osoba1 = ["Pawel Gilecki", "abc@abc.com", 45]
osoba2 = ["Grzegorz Jakubowski", "xyz@xyz.com", 46]
osoba3 = ["Michal Pacak", "qwe@qwe.com", 47]

for i in osoba1:
    print(i, "\t", end="")
print("")
for i in osoba2:
    print(i, "\t", end="")
print("")
for i in osoba3:
    print(i, "\t", end="")
print("")

osoby = [["Pawel Gilecki", "abc@abc.com", 45],
         ["Grzegorz Jakubowski", "xyz@xyz.com", 46],
         ["Michal Pacak", "qwe@qwe.com", 47]]
for osoba in osoby:
        for i in osoba:
        print(i, "\t", end="")
    print("")