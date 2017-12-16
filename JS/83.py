"""
83
Napisz skrypt python z zaproponowaną przez siebie funkcją
pobierającą liczbę od użytkownika i sprawdzającą jej
typ (całkowita, rzeczywista)
"""


def getNumericalInput():
    print("Podaj liczbę:")
    while True:
        v = input()
        try:
            v = int(v)
            print("Wczytano liczbę całkowitą")
            return v
        except ValueError:
            pass
        try:
            v = float(v)
            print("Wczytano maszynową liczbę rzeczywistą")
            return v
        except ValueError:
            print("Błąd, spróbuj ponownie")


getNumericalInput()