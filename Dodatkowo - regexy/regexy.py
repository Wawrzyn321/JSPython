import re
import slowaSource


# szukanie pierwszego wyrazu dwuliterowego
"""
r'
\w{2} wyrazy dwuliterowe
  spacja (której nie widać)
'
"""
r = r'\w{2} .*';
l = re.search(r, slowaSource.lorem, re.M|re.I)
print(l.group())


l = re.sub(r"[A-Z]", r"[a-z]", slowaSource.wiki)
print(l)
print(l.group())

# raise RuntimeError, "tekst"
# bigger = lambda a, b : a > b
