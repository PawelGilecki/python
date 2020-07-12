x = int(input("podaj liczbe "))
y = range(1, x+1)
lista = []

for element in y:
    div = x % element
    if div == 0:
        lista.append(element)
print(lista)


