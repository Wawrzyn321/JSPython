"""
89
Napisz  skrypt  python, który zamieni pobraną z pliku
danezadanie89.txt liczbę na system szesnastkowy i ósemkowy,
a następnie wszystkie trzy  zapisze do pliku
wyjsciezadanie89.txt.
"""

plik = "danezadanie89.txt"
data = open(plik).read().split("\n")
data = filter(None, data )
data = [int(i) for i in data ]

pOut = open("wyjsciezadanie89.txt", "w")

for d in data:
    pOut.write('{} {} {}\n'.format(
        d,
        hex(d), 
        oct(d))
    )

pOut.close()