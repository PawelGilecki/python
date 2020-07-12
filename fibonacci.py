value = int(input("podaj ile liczb z ciagu pokazac: "))

x = 0
y = 1
def fibonacci_list(n):
    if value == 0:
        fibonacci = [0]
    if value == 1:
        fibonacci = [0, 1]
    if value > 1:
        fibonacci = [0, 1]
        for i in range(2, value):
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
            i += 1
        return(fibonacci)

print(fibonacci_list(value))