import re
from bs4 import BeautifulSoup
import serpscrap
''


def clean_me(html):
    soup = BeautifulSoup(html, "lxml")
    for s in soup(['script', 'style']):
        s.decompose()
    return ' '.join(soup.stripped_strings)

with open("ace.html") as f:
    content = f.readlines()


clean_str = clean_me(str(content))
with open("clean_ace.txt", "w", encoding="utf-8") as k:
    k.write(clean_str)