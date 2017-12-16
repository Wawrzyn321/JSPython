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
import time


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

def qsort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        qsort(A, lo, p - 1)
        qsort(A, p + 1, hi)

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j := lo to hi - 1 do
        if A[j] < pivot then
            i := i + 1
            swap A[i] with A[j]
    if A[hi] < A[i + 1] then
        swap A[i + 1] with A[hi]
    return i + 1

def rzymianie(t):
    qsort(t, 0, len(t)-1)

dane = [random.randint(-10,10 + 1) for i in range(20)]
print(dane)

# a) bąbelkowe
dane2 = copy.copy(dane) # kopia, bo modyfikujemy tylko dane2

bańki(dane2)
print(dane2)

# b) wstawianie
dane2 = copy.copy(dane) # kopia, bo modyfikujemy tylko dane2

wklej(dane2)
print(dane2)


# c) qsort
dane2dane2 = copy.copy(dane) # kopia, bo modyfikujemy tylko dane2

rzymianie(dane2)
print(dane2)