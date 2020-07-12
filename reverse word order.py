sentence = input("Podaj zdanie: ")

def reverse():
    splitted = sentence.split()[::-1]
    result = " ".join(splitted)
    return (result)
print(reverse())