"""
76a
Napisz skrypt python pobierający liczbę z klawiatury i drukujący w oknie
konsoli napis zależnie od wartości pobranej liczby „więcej niż zero” lub
„mniej niż zero lub zero”.
"""

w = "więcej niż zero"
m = "mniej niż zero lub zero"
v = float(input())

# można tak
if v > 0:
    print(w)
else:
    print(m)

# albo tak
print(w if (v > 0) else m)

# w podobny sposób można zrobić oryginalne zadanie:
print("więcej niż zero" if (v > 0) else "mniej niż zero" if (v<0) else "")