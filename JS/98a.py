"""
98a
Napisz skrypt python sprawdzający unikalność linków
do stron zewnętrznych jakie znajdują się w podanej
jako argument wywołania stronie www.

Tym razem autorem całości jest Bartek.
# to ja - przyp. red.
"""

import urllib.request
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    found_links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, val in attrs:
                if name == "href":
                    self.found_links.append(val)


parser = MyHTMLParser()
parser.feed(str(urllib.request.urlopen('http://python.org/').read()))

print("Oto unikalne linki:")
print(set(parser.found_links))
print("\nOto nieunikalne linki:")
print(set([x for x in parser.found_links if parser.found_links.count(x) > 1])) #genialne
