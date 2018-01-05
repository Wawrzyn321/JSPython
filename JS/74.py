"""
Porównaj elementy obu utworzonych już list.
"""

list1 = [["tak", "nie"], ["moze", "domysl sie"], 1, 5]
list2 = [1, ["matematyka"], ["jest", "piekna"], ["tak, nie"]]

print("Czy obie listy sa rowne?")
print(str(bool(tuple(list1) == tuple(list2))))
# mozna w pythonie porownywac tylko hashowalne niemutowalne obiekty, tj. z kolekcji tylko tuple - przyp. red.
