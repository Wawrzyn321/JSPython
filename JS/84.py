"""
84
Napisz  skrypt  python, który będzie losował liczbę z zadanego
przedziału oraz  element  listy wczytanej z pliku i obie wartości
zapisze do pliku wynikzadanie84.txt
"""

import random

print("Podaj przedział: ")
a = float(input())
b = float(input())
#ewentualne poprawienie przedziału
if a > b:
    a, b = b, a # fajne, nie?

delim = ' '
pIn = 'dane84.txt'
data = open(pIn).read().split(delim)

pOut = open('wynikzadanie84.txt','w')
pOut.write(str(random.uniform(a, b)))
pOut.write('\n')
pOut.write(data[random.randint(0, len(data)-1)]) # uwaga na indeksy bardzo
pOut.close()

# BTW operacja z linii 15 działa dla dowolnej liczby zmiennych