import random
c = random.sample(range(1, 100), 15)
d = random.sample(range(1, 100), 12)
print(c)
print(d)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new = []

for element in c:
    if element in d:
        new.append(element)
print(new)