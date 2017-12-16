"""
91a
Napisz skrypt python, który będzie przeliczał i wypisywał na ekran
konsoli liczbę wystąpień liter w tekście wczytanym z pliku
wejściowego danezadanie91.txt.
"""

str = open('danezadanie91.txt').read()
slowa = {}

for c in str:
    slowa.setdefault(c, 0)
    slowa[c] += 1

for pair in slowa.items():
    print(pair)