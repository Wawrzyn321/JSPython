"""
88
Napisz skrypt python obliczający silnię zadanej liczby.
"""

import math


def silniaRek(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n-1)

def silnia(n):
    w = 1
    for i in range(1, n+1):
        w *= i
    return w


v = int(input())

print(silniaRek(v))
print(silnia(v))
print(math.factorial(v))
