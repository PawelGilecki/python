prime = int(input("Podaj prosze liczbe "))
divisors = []
for number in range(2, prime):
    if prime%number == 0:
        divisors.append(number)
print(divisors)

def prime_check(x):
    if prime > 1:
        if divisors == []:
            print("pierwsza")
        else:
            print("nie")
    else:
        print("nie")
prime_check(prime)