"""
71
Spowoduj pojedynczym poleceniem python, by na ekranie
n-krotnie wyświetliła się wartość wyrażenia -0.7e+4.07
każdorazowo rozdzielona znakiem @.
"""

n = int(input())
co = -0.7 * pow(10, 4.07) # da się to lepiej zapisać?
znak = '@'

print((str(co)+znak) * (n-1) + str(co) if (n > 0) else "")
