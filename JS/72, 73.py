"""
72, 73
Utwórz nową listę złożona w python, a następnie
rozszerz ja o kolejne elementy różnych typów,
72) na koniec wydrukuj całość na ekran konsoli python.
73) wykonaj wydruk poszczególnych elementów
    tej listy na   ekran konsoli python .
"""

lista = [
    ['a', 'b', 'c', 'zlew'],
    [1, 2, 3, 4],
    [[1,2], [3,4]],
    ['a', None, True]
]

print("Oryginał: " + str(lista), end = "\n\n")

lista[0] = ['-a'] + lista[0]
lista[1].append(5)
lista[2].insert(1, [2,3])
lista[3] = lista[3] * 2
lista = [["tak", "nie"]] + lista # podwójne nawiasy, ponieważ dodajemy
    # tutaj {listę, której elementem jest jedna lista}, a nie po prostu {listę}


# 72: całość
print(lista, end = '\n\n')

# 73: poszczególne elementy

for i in range(len(lista)):
    print("lista["+str(i)+"]:")
    for j in range(len(lista[i])):
        print(lista[i][j], end = " ")
    print()
