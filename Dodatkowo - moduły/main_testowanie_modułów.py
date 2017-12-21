
# import własnego modułu
import modul

val = modul.sinus(3.14/2)
print(val)
print("PI: " + str(modul.pi))



# można importować tylko niektóre wartości
from modulWybiórczy import f1, f2

f1()
f2()
# f4() # tutaj będzie błąd




# import z innego katalogu - Python szuka modułów tylko w katalogu bierzącym
# ale można zrobić tak
import sys
sys.path.insert(0, './innyKatalog')

import choinki # u mnie pokazuje błąd, że nie można odnaleźć modułu... ale działa

choinki.choinka()
choinki.choinkaSmutna()
