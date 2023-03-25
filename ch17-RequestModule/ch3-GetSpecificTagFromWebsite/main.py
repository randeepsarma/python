import requests

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)
from bs4 import BeautifulSoup

soup = BeautifulSoup()

soup = BeautifulSoup(r.text, "html.parser")

# print(soup.prettify())#for beautifying code

# to get text inside h2 tag that is static and not populated by api
for heading in soup.find_all("h2"):
    print(heading.text)
