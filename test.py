import sys
import requests
import inspect
from bs4 import BeautifulSoup
import re


matches = []


def repl(m):                          # m is a match data object
    matches.append(m.group())         # Add a whole match value
    # Return the match and a newline appended to it
    return m.group().replace('.', '.</p><p>')


s = "Ela estava sozinha na escuridão.Foi apenas quando tudo parecia perdido que ela viu a luz.E a seguiu.Pelo caminho, ela encontrou suprimentos escassos."
pattern = re.compile(r"\w\.[A-Z]")
s = re.sub(pattern, repl, s)

print(s)
