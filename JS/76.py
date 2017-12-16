"""
76
Napisz skrypt python pobierający liczbę z klawiatury i drukujący w oknie
konsoli napis zależnie od wartości pobranej liczby „więcej niż zero” lub
„mniej niż zero”.
"""

v = input()
if v > 0:
    print("więcej niż zero")
elif v < 0:
    print("mniej niż zero, o")
