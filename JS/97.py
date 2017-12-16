"""
97
Napisz skrypt python wyznaczający wszystkie możliwe rozmiary ubrań
kobiecych i męskich (Kobieta, Mężczyzna) w zadanych kolorach (biały,
czarny, zielony, czerwony, niebieski) i rozmiarach (XL, L, M,  S).
Wyznaczone  metki zostaną zapisane każda oddzielnie do pliku
wyjsciezadanie97_metkai.txt, gdzie i oznacza kolejną iterację utworzenia
nowej metki.
"""

plcie = ["K", "M"]
kolory = ["biały", "czarny", "zielony", "czerwony", "niebieski"]
rozmiary = ["XL", "L", "M", "S"]

l = 0
for p in plcie:
    for k in kolory:
        for r in rozmiary:
            l += 1
            pOut = open("97/wyjsciezadania97_metka"+str(l)+".txt", "w")
            pOut.write(p+"_"+k+"_"+r)
            pOut.close()
