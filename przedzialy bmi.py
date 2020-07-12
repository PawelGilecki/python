# status BMI
# autor: Grzegorz Jakubowski, Paweł Gilecki

waga = float(input("Wpisz wage w kg: "))
print(waga)   
wzrost = float(input("Wpisz wzrost w metrach: "))
print(wzrost)
BMI = waga/(wzrost**2)
print(BMI)

if BMI <  16:
    print ("Jestes wygłodniały")
elif BMI < 18:
    print ( "Jestes wychudzony")
elif BMI < 20:
    print ( "Jestes normalny")
else:
    print ( "Jestes gruby")
