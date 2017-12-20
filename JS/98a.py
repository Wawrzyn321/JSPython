"""
98a
Napisz skrypt python sprawdzający unikalność linków
do stron zewnętrznych jakie znajdują się w podanej
jako argument wywołania stronie www.

Tym razem autorem całości jest Bartek.
"""

import urllib.request
from html.parser import HTMLParser

list = []

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if(tag == "a"):
            for name, attrs in attrs:
                if name == "href":
                    list.append(attrs)

parser = MyHTMLParser()
parser.feed(str(urllib.request.urlopen('http://python.org/').read()))

print("Oto unikalne linki:")
print(set(list))
print("Oto nieunikalne linki:")
print(set([x for x in list if list.count(x) > 1])) #genialne
