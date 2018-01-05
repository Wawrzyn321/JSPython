"""
75a
Napisz procedurę sprawdzającą, czy podany element występuje
gdziekolwiek w podanej liście.
"""

# sprawdzenie, czy element jest listą (ogólniej: czy można po nim iterować)
# nieużywane tutaj, ale podoba mi się
def isIterable(val):
    try:
        iter(val) # próba pobrania iteratora
        return True
    except TypeError:
        return False

# mozna ladniej
# https://docs.python.org/3/library/collections.abc.html
# - przyp. red.
from collections import abc

def is_iterable(val):
    return isinstance(val, abc.Iterable)

is_iterable([1])

# sprawdzenie, czy element jest listą
# UWAGA: funkcja zwraca False dla łańcuchów znaków
def isList(val):
    return type(val) is list

# szukanie elementu "gdziekolwiek"
def szukaj(n, lista):
    if n in lista: return True

    #wywołaj rekurencyjnie dla każdego elementu
    #będącego listą
    for i in range(len(lista)):
        if isList(lista[i]):
            if szukaj(n, lista[i]):
                return True

    return False


Lista = [
    [1, 2],
    ['a', ['b', 'c'], 'd'],
    [[[['!']]]],
    [
        ['A', 'B'],
        ['C', 'D']
    ],
    ["drewno"]
]


print(szukaj(   [1, 2]      , Lista))
print(szukaj(   [3, 5]      , Lista))
print(szukaj(   '!'         , Lista))
print(szukaj(   'd'         , Lista))
print(szukaj(   'C'         , Lista))
print(szukaj(   ['A', 'B']  , Lista))
print(szukaj(   ['w']       , Lista))
