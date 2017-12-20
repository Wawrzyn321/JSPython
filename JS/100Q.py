# qsort

import random
import sys


def zwyciężaj(t, s, e):
    if s < e:
        split = dziel( t, s, e)
        zwyciężaj(t, s, split - 1)
        zwyciężaj(t, split + 1, e)
    return t

# pomocnicza do qsortu - znajdowanie miejsca podziału
# u nas to po pierwszy element
def dziel(t, s, e):
    pivot = t[s]
    i = s + 1
    for j in range( s + 1, e + 1 ):
        if t[j] < pivot:
            t[i], t[j] = t[j], t[i]
            i += 1
    t[s], t[i - 1] = t[i - 1], t[s]
    return i-1

# wywołanie qsortu
def rzymianie(t):
    zwyciężaj(t, 0, len(t)-1)


if len(sys.argv) < 3:
    print("Za mało parametrów!")
    exit(-1)

random.seed(int(sys.argv[1]))
randomy = []
for i in range(int(sys.argv[2])):
    randomy.append(random.randint(-100, 100))

rzymianie(randomy)
