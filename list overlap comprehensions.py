import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = random.sample(range(100),5)
print(c)

set_a = set(a)
set_b = set(b)
print(list(set_a&set_b))

overlap = [number for number in a if number in b]
overlap = list(dict.fromkeys(overlap))
print(overlap)