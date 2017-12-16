"""
83, ale z tuplami
"""


def getNumericalInput():
    print("Podaj liczbę:")
    while True:
        v = input()
        try:
            v = int(v)
            return v, "int"
        except ValueError:
            pass
        try:
            v = float(v)
            return v, "float"
        except ValueError:
            print("Błąd, spróbuj ponownie")


val = getNumericalInput()
print("wczytano " + str(val[0]) + ', czyli ' + val[1])
