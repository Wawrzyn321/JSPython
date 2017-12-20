"""
90
Używając funkcji python, dla zadanych wartości
zmiennych wykonaj następujące obliczenia:
(goto '90 shortcut')
"""

import math


def p_a():
    alfa = float(input("Podaj alfę: "))
    beta = float(input("Podaj betę: "))
    lewa = math.sin(alfa) + math.sin(beta)
    prawa = 2 * math.sin((alfa + beta) / 2) * math.cos((alfa - beta) / 2)
    print("dla dodawania: ")
    print("L: " + str(lewa))
    print("P: " + str(prawa))
    lewa = math.sin(alfa) - math.sin(beta)
    prawa = 2 * math.sin((alfa - beta) / 2) * math.cos((alfa + beta) / 2)
    print("dla odejmowania: ")
    print("L: " + str(lewa))
    print("P: " + str(prawa))


def p_b():
    x = float(input("Podaj x: "))
    n = int(input("Podaj n: "))
    it = int(input("Podaj it: "))
    lewa = 1 + x**n
    prawa = 1
    for i in range(1, it + 1):
        prawa += (n * (n - i) * x) / math.factorial(i)
    print("L: " + str(lewa))
    print("P: " + str(prawa))


def p_c():
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    print("x1: " + str(x1))
    print("x2: " + str(x2))


def p_d():
    x = float(input("Podaj x: "))
    ile = int(input("Podaj ile: "))
    lewa = math.e**x
    prawa = 1
    for i in range(1, ile):
        prawa += x**i / math.factorial(i)
    print("L: " + str(lewa))
    print("P: " + str(prawa))


v = input("Który podpunkt? ")

# słownik par łańuch - funkcja
dostepnePodpunkty = {"a": p_a, "b": p_b, "c": p_c, "d": p_d}

if v not in dostepnePodpunkty:
    print("nie to nie.")
    exit(666)
else:
    dostepnePodpunkty[v]()
