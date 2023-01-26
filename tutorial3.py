# Finding elements by id
# in a html webpage every element has an id attribute assigned to it to uniquely identify it

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"

page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

# print(soup.prettify())

# res = soup.find(id='mw-content-text')
# print(res)

# to find the first anchor tag
# print(soup.a)

# to find all anchor tags
all_links = soup.find_all('a')
# print(all_links)

# to print links one after another
# for i in all_links:
#     print(i)

# to get only links
for i in all_links:
    print(i.get('href'))


