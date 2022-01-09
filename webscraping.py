import sys
import requests
import inspect
from bs4 import BeautifulSoup
import re

print("Lets try some webscraping with Py!")


class Response():
    def __init__(self, response):
        self.status = response.status_code
        self.headers = response.headers
        # self.content = BeautifulSoup(response.text, 'lxml')
        self.content = response.text

    def print(self):
        print(f'Status code: {self.status}')
        print(f'Headers: {self.headers}')
        print(f'Content: {self.content}')

    """
    def replace_tag(self):
        self.content = self.content.replace(
            'name="description"', 'property="og:description"')
    """


class RegexTreatment():
    def __init__(self):
        self.content = None
        self.matches = []

    def repl(self, m):                          # m is a match data object
        self.matches.append(m.group())         # Add a whole match value
        # Return the match and a newline appended to it
        return m.group().replace('.', '.</p><p>')

    def add_paragraph(self, content):
        self.content = content
        self.matches = []
        pattern = re.compile(r"\w\.[A-Z]")
        content = re.sub(pattern, self.repl, content)
        return content


champs = ['leona', 'diana', 'darius', 'kaisa']

base_url = "https://universe.leagueoflegends.com/pt_BR/story/champion/"

# r = Response(requests.get(
#     "https://universe.leagueoflegends.com/pt_BR/story/champion/diana/"))

# print(r.content.prettify())
# f = open("texto.txt", "w", encoding=" iso-8859-1")
# f.write(r.content.prettify())
# f.close()
# print(r.status)

# print(r.content.meta)
print()
# print(r.content.select('meta:nth-of-type(6)')[0].prettify())
# print(r.content.select('meta:nth-of-type(9)')[0].prettify())
# r.replace_tag()


for champ in champs:
    prettier = RegexTreatment()
    r = Response(requests.get(
        base_url + champ))
    soup = BeautifulSoup(r.content, 'lxml')
    root = soup.html.head
    f = open(champ + "_complete_file.txt", "w", encoding=" iso-8859-1")
    f.close()
    text1 = soup.find("meta", property="og:description")["content"]
    text1 = prettier.add_paragraph(text1)
    # print(text1)
    text1 = "<p>" + text1 + "</p>"
    f = open(champ + ".html", "w", encoding=" iso-8859-1")
    f.write(text1)
    f.close()

# root_childs = [e.name for e in root.children if e.name is not None]
# print(root_childs)


# metas = [meta.content for meta in root]
# print(metas)
# [print(meta.content) for meta in metas]


# text1 = soup.find("meta", property="og:description")["content"]
# print(text1)
# print(text2)
# print(text2["content"] if text2 else "No meta url given")

# print(text1)
# f = open("texto.txt", "w", encoding=" iso-8859-1")
# f.write(text1)
# f.close()
