def euklides(a, b):
    while b:
        a, b = b, a % b
    return a


liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))

nwd = euklides(liczba1, liczba2)

print(f"Największy wspólny dzielnik ({liczba1}, {liczba2}) = {nwd}")

