"""
81
Napisz  skrypt  python obliczający sumę,
wartość średnią i medianę liczb całkowitych
pobranych z zadanego pliku.
"""


import statistics

# separator - u nas dane są zapisane w osobnych liniach
# jeśli były by oddzielone spacjami, to delim = ' ' i tak dalej
delim = '\n'

# wczytanie z pliku
plik = "dane81.txt"
nums = open(plik).read().split(delim)
#usunięcie elementów pustych ('')
nums = filter(None, nums)
# zamiana str na int
nums = [int(i) for i in nums]

print(sum(nums))
print(statistics.mean(nums))
print(statistics.median(nums))
