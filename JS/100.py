"""
100
Napisz skrypt python, który wywoła napisane przez Ciebie
wcześniej skrypty python wykonujące sortowanie i zmierzy
ich czasy sortowania. Następnie wykona raport ze zgromadzonych
wyników zapisany w pliku raport_[aktualna data].txt
następującej postaci (goto 100 short.png)
"""

# chcemy, by zestaw liczb przy wywołaniu kazdego
# podskryptu był taki sam, więc ustawiamy seed
# w drugim argumencie
# w trzecim jest liczebność zestawu danych


import time
import datetime
import os
import random


def odch_standard(list):
    avg = sum(list) / len(list)
    v = 0
    for i in list:
        v += (i - avg)**2
    v /= len(list)
    return v


skrypty = ["100B.py", "100W.py", "100Q.py"]
nazwy = ["bąbelkowe", "wstawianie", "quick sort"]

sample = 300
testów = 20

czasy = [[], [], []]
odchylenia = []
srednie = []

for j in range(testów):
    print('test #' + str(j), end="")
    # seed jest jednakowy dla każdej trójki testów
    seed = random.randint(0, 10000)
    for i in range(len(skrypty)):
        print('.', end="")
        start = time.time()
        os.system("{} {} {}".format(skrypty[i], str(seed), str(sample)))
        t = time.time() - start
        czasy[i].append(t)
    print()

for t in czasy:
    odchylenia.append(odch_standard(t))
    srednie.append(sum(t) / len(t))


data = datetime.datetime.now().strftime('%Y-%m-%d')
pOut = open('raport_' + data + 'txt', 'w')

pOut.write("RAPORT ALGORYTMÓW SORTOWANIA\n")
pOut.write("NAZWA -- LICZBA SORTOWANYCH DANYCH -- ŚREDNI CZAS -- ODCHYLENIE STANDARDOWE\n")

for i in range(len(czasy)):
    pOut.write("{}. {} -- {} -- {} -- {}\n".format(
        str(i+1),
        nazwy[i],
        str(sample),
        srednie[i],
        odchylenia[i]
    ))

pOut.close()
