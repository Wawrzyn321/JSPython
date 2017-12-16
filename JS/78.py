"""
78
Napisz skrypt python drukujący na ekran konsoli wszystkie samogłoski
jeśli znajdują się one w ciągu liter alfabetu, który podajemy z klawiatury.
"""

samogloski = [ 'a', 'e', 'y', 'i', 'o', 'ą', 'ę',  'u', 'ó']
teKtóreSą = []

s = input()

for znak in s:
    znak = znak.lower()
    # dodaj, jeśli występuje w liście samogłosek,
    # nie dublując elementów w liście tychKtóreSą
    if znak in samogloski and not znak in teKtóreSą:
        teKtóreSą.append(znak)

print(teKtóreSą)