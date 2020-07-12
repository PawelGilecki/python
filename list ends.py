a = [5, 10, 15, 20, 25]

b = len(a)

def list_creation():
    for i in range (b):
        new_list = [a[0], a[b-1]]
    print(new_list)
list_creation()
