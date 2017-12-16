"""
92
Napisz skrypt python, który będzie wykonywał i wypisywał na ekran
konsoli statystykę wyrazów w tekście wczytanym z pliku wejściowego
danezadanie92.txt.
"""

str = open('danezadanie91.txt').read()
slowa = {}

for w in str.split(' '):
    slowa.setdefault(w, 0)
    slowa[w] += 1

for pair in slowa.items():
    print(pair)