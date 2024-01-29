def fibonnaci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n + 5:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[n:n + 5]


indeks_poczatkowy = int(input("Podaj indeks początkowy ciągu Fibonacciego: "))


nastepne_liczby = fibonnaci(indeks_poczatkowy)


print(f"5 następnych liczb ciągu Fibonacciego po indeksie {indeks_poczatkowy}: {nastepne_liczby}")
