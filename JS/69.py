"""
69
Wiedząc, że pierwiastek n-tego stopnia z x równa się x do potęgi 1/n
i wykorzystując  wiedzę  o  użyciu  liczb  zespolonych  w python,
wylicz wartość pierwiastka drugiego stopnia z liczby -23.
"""

import math


def sqrt(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return complex(0, pow(abs(x), 0.5))


print(sqrt(-23))
