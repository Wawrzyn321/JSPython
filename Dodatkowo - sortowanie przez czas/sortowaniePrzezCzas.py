"""
Sortowanie przez czas - mam do posortowania n zmiennych liczbowych.
Dla każdej z nich tworzę wątek, który zwróci po n[i] interwałach
wartość n[i] do wspólnej kolekcji.

Więcej o wątkach: https://www.tutorialspoint.com/python/python_multithreading.htm
"""

import random
import _thread
import time

posortowane = []


def sub(timeToSleep):
    time.sleep(timeToSleep * 0.1)
    posortowane.append(timeToSleep)


rand = []
for i in range(10):
    rand.append(random.randint(1, 30))
print(rand)


for r in rand:
    try:
        _thread.start_new_thread(sub, (r, ))
    except:
        print("Error: unable to start thread!")

print("SORTUJĘ")

while len(rand) != len(posortowane):
    pass

print(posortowane)
