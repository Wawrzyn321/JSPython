"""
75
Wykonaj polecenie sprawdzające, czy zadany element należy do jednej z
utworzonych list.
"""

lista = [['a', 'b', 'c', 'zlew'], [1, 2, 3, 4], [[1,2], [3,4]], ['a', None, False]]

print([1,2,3,4] in lista)
print(3 in lista)
print(None in lista[0])
print(None in lista[3])