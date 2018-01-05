"""
98
Napisz skrypt python sprawdzający unikalność linków
do stron zewnętrznych jakie znajdują się w podanej
jako argument wywołania stronie www.

HTML crawling napisany przez redakcje
"""

import urllib.request
import sys
from html.parser import HTMLParser

linki = []


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, attrs in attrs:
                if name == "href":
                    linki.append(attrs)


# adres = 'https://platforma.polsl.pl/'
if len(sys.argv) < 2:
    print("brak argumentu wywołania!")
    exit(-1)
adres = sys.argv[1] # pierwszym argumentem jest jak widzę nazwa pliku
# tak - przyp. red.
parser = MyHTMLParser()

print("Zaczynam szukanie...")
parser.feed(str(urllib.request.urlopen(adres).read()))

print('No jest, mam ' + str(len(linki)))
print(linki)

unikalne = set(linki)
print('Ale unikalnych jest ' + str(len(unikalne))) # set odfiltruje wartości zduplikowane
print(unikalne)

