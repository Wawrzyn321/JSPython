"""
85, 86 TODO o co chodzi
Napisz  skrypt  python
85) wypisujący na  ekran  konsoli
86) zapisujący do pliku zewnętrznego
liczby o  wymiarze  5 kolumn i 7 wierszy na podstawie
pobranej wartości liczbowej.
"""

val = input()

out = ""

for i in range(5):
    for j in range(7):
        out += str(val) + " "
    out += "\n"

# 85: konsola
print(out)

# 86: plik
plik = open("wyjsciezadanie86.txt", 'w')
plik.write(out)
plik.close()
