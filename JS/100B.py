# bąbelki

import random
import sys


def bańki(t):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(t) - 1):
            # elementy nie spełniające porzadku
            if t[i] > t[i + 1]:
                # zamiana
                t[i], t[i+1] = t[i+1], t[i]
                # od nowa
                sorted = False
                break


if len(sys.argv) < 3:
    print("Za mało parametrów!")
    exit(-1)

random.seed(int(sys.argv[1]))
randomy = []
for i in range(int(sys.argv[2])):
    randomy.append(random.randint(-100, 100))

bańki(randomy)

