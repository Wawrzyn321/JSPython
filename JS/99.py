"""
99
Napisz skrypty python wykonujące sortowanie danych z pliku
i zapisujące posortowane elementy do innego pliku:
a. Sortowanie bąbelkowe
b. Sortowanie przez wstawianie
c. Quick sort
"""

#czytanie i pisanie do plików jest mało ciekawe, bo i tak robiliśmy to wiele razy wcześniej

import random  # randint
import copy  # copy

# bąbelkowe
def bańki(t):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(t) - 1):
            # elementy nie spełniające porzadku
            if t[i] > t[i + 1]:
                # zamiana
                t[i], t[i+1] = t[i+1], t[i]
                # od nowa
                sorted = False
                break

# wstawianie
def wklej(t):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(t) - 1):
            # elementy nie spełniające porzadku
            if t[i] > t[i + 1]:
                # wycięcie i-tego elementu
                v = t[i]
                del t[i]

                # szukanie dla niego miejsca
                nojuzwkleilem = False
                for i in range(len(t) - 1):
                    if t[i] > v:
                        t.insert(i, v)
                        nojuzwkleilem = True
                        break
                # jeśli miejsca nie znaleziono, zamontować z tyłu
                if not nojuzwkleilem:
                    t.append(v)
                # i od nowa
                sorted = False
                break

# qsort
def zwyciężaj(t, s, e):
    if s < e:
        split = dziel( t, s, e)
        zwyciężaj(t, s, split - 1)
        zwyciężaj(t, split + 1, e)
    return t

# pomocnicza do qsortu - znajdowanie miejsca podziału
# u nas to po pierwszy element
def dziel(t, s, e):
    pivot = t[s]
    i = s + 1
    for j in range( s + 1, e + 1 ):
        if t[j] < pivot:
            t[i], t[j] = t[j], t[i]
            i += 1
    t[s], t[i - 1] = t[i - 1], t[s]
    return i-1

# wywołanie qsortu
def rzymianie(t):
    zwyciężaj(t, 0, len(t)-1)

# skopiuj dane, posortuj je wybranym algorytmem i wypisz
def sortowania(dane, funkcja):
    dane2 = copy.copy(dane) # kopia, bo modyfikujemy tylko dane2

    funkcja(dane2)
    print(dane2)

dane = [random.randint(-10,10 + 1) for i in range(20)]
print(dane)


# a) bąbelkowe
sortowania(dane, bańki)

# b) wstawianie
sortowania(dane, wklej)

# c) qsort
sortowania(dane, rzymianie)

