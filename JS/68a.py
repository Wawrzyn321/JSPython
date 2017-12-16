"""
68
Napisać skrypt python pobierający
a) liczbę danych
b) dane będące liczbami rzeczywistymi
i zapisujący ich sumę w postaci liczby całkowitej
na standardowym wyjściu konsoli.
Dodaj kontrolę błędów wejścia.
"""


import math  #math.floor


# parsowanie liczb całkowitych
def safeInputInt():
    while True:
        try:
            return int(input())
        except ValueError:
            print('Błąd wejścia, podaj liczbę całkowitą: ', end="")


# parsowanie liczb rzeczywistych
def safeInputFloat():
    while True:
        try:
            return float(input())
        except ValueError:
            print('Błąd wejścia, podaj liczbę rzeczywistą: ', end="")


suma = 0

print("Podaj liczbę (nie ilość!) sumowanych liczb: ", end="")
ile = safeInputInt()

for i in range(ile):
    print("Podaj liczbę #"+str(i+1)+": ", end="")
    suma += safeInputFloat()

suma = math.floor(suma)
print("Ich suma w postaci liczby calkowitej to: "+str(suma))
