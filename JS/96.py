"""
96
Napisz skrypt python wyznaczający lata przestępne w podanym zakresie.
"""

import math

# zaokrąglenie do najbliżej wielokrotności 4
def ceilTo4(n):
    return 4 * math.ceil(n / 4)

a = int(input())
b = int(input())
#dzisiaj nie sprawdzamy poprawności przedziału

# normalnie jak w tym zarcie o calce oznaczonej wsiadajacej do pociagu, ktory wisi na wydziale...
# - przyp. zazenowanej redakcji

a = int(ceilTo4(a))

for i in range(a, b + 1, 4):
    if i % 100 == 0 and i % 400 != 0:
        continue
    print(i)
