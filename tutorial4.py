# find elements by HTML class

import requests
from bs4 import BeautifulSoup

URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

results = soup.find(id="ResultsContainer")
# print(results.prettify())

# find all returns all the content in itterable format
job_elements =results.find_all('div',class_ ='card-content')
# print(job_elements)

for i in job_elements:
    title_element = i.find('h2',class_ ='title')
    subtitle_element = i.find('h3',class_ = 'subtitle')
    location_element= i.find('p',class_ = 'location')
    print('Title: ', title_element.string.strip())
    print('Subtitle: ',subtitle_element.string.strip())
    print('Location: ',location_element.string.strip())
    print()

