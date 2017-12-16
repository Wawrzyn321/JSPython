"""
95
Napisz skrypt python rozwiązujący równanie kwadratowe w ciele liczb
zespolonych, gdzie współczynniki a, b, c będą pobierane z jednego pliku
danezadanie95.txt a wynik będzie wypisywany na konsoli.
"""

import math

plik = open("danezadanie95.txt")
strw = plik.read()
plik.close()

dane = strw.split(' ')
a = float(dane[0])
b = float(dane[1])
c = float(dane[2])

if a == 0:
    print('to nie jest rownanie kwadratowe', end="")
    if b == 0:
        if c == 0:
            print(', ale i tak jako równanie to ma nieskończenie wiele rozwiązań')
        else:
            print(' i w ogóle nie ma rozwiązań')
    else:
        print("ale jako równanie liniowe ma rozwiązanie x = "+str(-c/b))
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("rozwiązanie spełnia zarówno liczba " + str(x1) + ", jak i " + str(x2))
    elif delta == 0:
        print("rozwiązaniem jest liczba " +str(-b/(2*a)))
    else:
        dsqrti = math.sqrt(-delta)
        x1 = complex(-b / (2 * a), dsqrti / (2 * a))
        x2 = complex(-b / (2 * a), -dsqrti / (2 * a))
        print("rozwiązania są " + str(x1) + " oraz " + str(x2))

