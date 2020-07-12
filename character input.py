import datetime

current_year = datetime.datetime.now().year
name = input("Podaj swoje imie ")
age = int(input("Podaj swoj wiek "))
yob = current_year - age
hundred = yob + 100
no_of_pages = int(input("Podaj dowolna liczbe "))

for i in range(no_of_pages):
    print(name, "ukonczysz 100 lat w", hundred)