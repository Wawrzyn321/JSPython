"""
89
Napisz  skrypt  python, który zamieni pobraną z pliku
danezadanie89.txt liczbę na system szesnastkowy i ósemkowy,
a następnie wszystkie trzy  zapisze do pliku
wyjsciezadanie89.txt.
"""

plik = "danezadanie89.txt"
# tutaj czytanie pliku jest nieco inaczej
data = open(plik).read()
data = data.strip()
data = data.splitlines(False)
data = [int(i) for i in data ]

pOut = open("wyjsciezadanie89.txt", "w")

for d in data:
    pOut.write('{} {} {}\n'.format(
        d,
        hex(d), 
        oct(d))
    )

pOut.close()
