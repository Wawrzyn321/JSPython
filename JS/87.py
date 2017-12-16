"""
87
Napisz skrypt python generujący siatkę danych testowych w postaci
macierzy o liczbie kolumn i wierszy podanej przez użytkownika, której
elementy będą losowane z zadanego przedziału liczbowego.
"""

import random

print("Podaj liczbę kolumn: ", end="")
k = int(input())
print("Podaj liczbę wierszy: ", end="")
w = int(input())
print("Podaj liczbę początek przedziału: ", end="")
a = float(input())
print("Podaj liczbę koniec przedziału: ", end="")
b = float(input())

if a > b:
    a, b = b, a

for i in range(w):
    for j in range(k):
        print(random.uniform(a,b), end = " ")
    print()

