"""
68a
Napisać skrypt python pobierający dwie liczby
i zapisujący ich sumę w postaci liczby całkowitej
na standardowym wyjściu konsoli.
"""

import math  #math.floor

print("Podaj dwie liczby: ")
a = float(input())
b = float(input())
suma = math.floor(a+b)
print("Ich suma w postaci liczby calkowitej to: "+str(suma))
