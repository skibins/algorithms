import random


def insertion_sort(tablica):
    for i in range(1, len(tablica)):
        klucz = tablica[i]
        j = i - 1
        while j >= 0 and klucz < tablica[j]:
            tablica[j + 1] = tablica[j]
            j -= 1
        tablica[j + 1] = klucz


tablica_liczb = [random.randint(1, 100) for _ in range(10)]

'''
tablica_liczb = []
for i in range(10):
    liczba = int(input(f"Podaj liczbę {i + 1}: "))
    tablica_liczb.append(liczba)
'''

print("Tablica przed sortowaniem:", tablica_liczb)

insertion_sort(tablica_liczb)

print("Tablica po sortowaniu:", tablica_liczb)
