# How to send a request html page from web

import requests

URL = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"

page = requests.get(URL)
# print(page)

data = page.text
print(data)