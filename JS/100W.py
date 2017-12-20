# wstawianie

import random
import sys


# wstawianie
def wklej(t):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(t) - 1):
            # elementy nie spełniające porzadku
            if t[i] > t[i + 1]:
                # wycięcie i-tego elementu
                v = t[i]
                del t[i]

                # szukanie dla niego miejsca
                nojuzwkleilem = False
                for i in range(len(t) - 1):
                    if t[i] > v:
                        t.insert(i, v)
                        nojuzwkleilem = True
                        break
                # jeśli miejsca nie znaleziono, zamontować z tyłu
                if not nojuzwkleilem:
                    t.append(v)
                # i od nowa
                sorted = False
                break


if len(sys.argv) < 3:
    print("Za mało parametrów!")
    exit(-1)

random.seed(int(sys.argv[1]))
randomy = []
for i in range(int(sys.argv[2])):
    randomy.append(random.randint(-100, 100))

wklej(randomy)

