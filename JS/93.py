"""
93
Napisz skrypt python, który będzie zamieniał w tekście wczytanym z pliku
danezadanie93.txt  wszystkie  wczytane  litery  na  wersaliki  i  wynik
zapisze do pliku wyjsciezadanie93.txt.
"""

pIn = open('danezadanie93.txt', encoding="utf-8")
str = pIn.read()
pIn.close()

pOut = open('wyjsciezadanie93.txt', 'w', encoding="utf-8")
pOut.write(str.upper())
pOut.close()