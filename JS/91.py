"""
91
Napisz skrypt python, który będzie przeliczał i wypisywał na ekran
konsoli liczbę wystąpień zadanych liter w tekście wczytanym z pliku
wejściowego danezadanie91.txt.
"""

print(open('danezadanie91.txt', encoding="utf-8").read().count(input()))