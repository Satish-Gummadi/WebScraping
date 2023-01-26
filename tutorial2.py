# using beautifulsoup to parse the html data

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"

page = requests.get(URL)
# print(page)

soup = BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())

# to only get the title
data = soup.title
print(data)

# to get title only in string without html tags
data1 = soup.title.string
print(data1)