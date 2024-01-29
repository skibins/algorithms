import random

def znajdz_najmniejszy(tablica):
    if not tablica:
        return None

    najmniejszy = tablica[0]

    for element in tablica:
        if element < najmniejszy:
            najmniejszy = element

    return najmniejszy


dlugosc_tablicy = 10
tablica = [random.randint(1, 100) for i in range(dlugosc_tablicy)]


print("Wygenerowana tablica:", tablica)

najmniejszy_element = znajdz_najmniejszy(tablica)

print(f"Najmniejszy element w tablicy to: {najmniejszy_element}")
