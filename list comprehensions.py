a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = []

"""for element in a:
    if element%2 == 0:
        even.append(element)"""
even = [element for element in a if element%2 == 0]
print(even)