a = [1, 3, 5, 30, 42, 43, 500]
user = int(input("podaj numer: "))

middle = len(a)//2
print(middle)
new_list = []

for element in [middle]:
    print(a[element])
    if a[element] > user:
        new_list = a[:element:]
    print(new_list)

"""def element_search(x):
    if user not in a:
        return True
    else:
        return False

if __name__=="__main__":
    print(element_search(user))"""
