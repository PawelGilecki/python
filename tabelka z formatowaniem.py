# listy
#Pawel, Grzegorz

osoby = [["Pawel Gilecki", "abc@abc.com", 45],
         ["Grzegorz Jakubowski", "xyz@xyz.com", 46],
         ["Michal Pacak", "qwe@qwe.com", 47]]
for osoba in osoby:
    for i in osoba:
        print(str(i).center(20), "\t", end="")
    print("")