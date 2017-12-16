"""
77
Napisz skrypt python drukujący na ekran konsoli w kolejnych wierszach
poszczególne elementy listy pobieranej z klawiatury.
"""

print("wpisuj kolejne elementy listy lub 'q', aby wyjść: ")
print("jeśli chcesz wpisać zwykłe 'q' do listy, wpisz je jako '\q'")

list = []

while True:
    v = input()
    if v == 'q':
        break
    elif v == '\q':
        v = 'q'

    list.append(v)

print("Oto lista:")
for l in list:
    print(l, end=" ")

