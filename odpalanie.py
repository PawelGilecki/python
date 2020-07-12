import sys

print(type(sys.argv))
print(sys.argv)
suma = 0

for i in sys.argv[1:]:
    suma += int(i)
print(suma)