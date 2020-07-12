a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = int(input("podaj numer "))

lista = []
for element in a:
    if element < b:
        lista.append(element)
print(lista)
