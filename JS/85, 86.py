# """
# 85, 86 TODO
# Napisz  skrypt  python
# 85) wypisujący na  ekran  konsoli
# 86) zapisujący do pliku zewnętrznego
# liczby o  wymiarze  5 kolumn i 7 wierszy na podstawie
# pobranej wartości liczbowej.
# """

zero = [" 000 ","0   0","0   0","0   0","0   0","0   0"," 000 "]
jeden = ["  11 ", " 1 1 ", "1  1 ", "   1 ", "   1 ", "   1 ", "   1 "]
dwa = [" 222 ", "2   2", "   2 ", "  2  ", " 2   ", "2    ", "22222"]
trzy = [" 3333","3   3","    3"," 333 ","    3","3   3","3333 "]
cztery = ["4    ","4    ","4  4 ","44444","   4 ","   4 ","   4 "]
piec = ["55555","5    ","5    ","5555 ","    5","    5","5555 "]
szesc =[" 666 ","6   6","6    ","6666 ","6   6","6   6"," 666 "]
siedem =["77777","7   7","   7 ","  7  "," 7   ","7    ","7    "]
osiem =[" 888 ","8   8","8   8"," 888 ","8   8","8   8"," 888 "]
dziewiec =[" 999 ","9   9","9   9"," 9999","    9","9   9"," 999 "]

cyfry = [zero, jeden, dwa, trzy, cztery, piec, szesc, siedem, osiem, dziewiec]

val = input()

plik = open("wyjsciezadanie86.txt", 'w')
for i in range(0,7):
    for j in val:
        print (cyfry[int(j)][i], end="  ")
        plik.write(cyfry[int(j)][i])
    print("")
    plik.write("")
plik.close()
