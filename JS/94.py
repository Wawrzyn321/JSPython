"""
94
Napisz skrypt python wypisujący iterację wraz z sumowaniem
pobranej podstawy w danej iteracji do zadanego pliku według
schematu: (goto 94 short.png)

Co prawda nie formatuje do końca jak trzeba, ale trudno ej.
"""


do = 10
podstawa = int(input("Podaj podstawę: "))

plik = open("wyjsciezadanie94.txt", "w")

plik.write("licznik  suma\n")
plik.write("0".center(5,"*"))
plik.write(" ")
plik.write("0".center(5,"*"))
plik.write("\n-----  -----\n")

# ilość miejsca przy maksymalnym wyrazie
gwiazdek = len(str((do + 1) * podstawa)) + 2

for i in range(1, do + 1):
    plik.write(str(i).center(gwiazdek, "*"))
    plik.write(" | ")
    plik.write(str(podstawa * i).center(gwiazdek, "*"))
    plik.write("\n")

plik.close()
