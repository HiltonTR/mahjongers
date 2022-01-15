import json
import requests
from bs4 import BeautifulSoup

def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] # 'css-1gyuw4i eh475bn0' for less relevant synonyms

word = "cozy"
print(synonyms(word))

for i in range (10):

    f = open('data.json')

    data = json.load(f)

    for j in data['restaurants']:
        print(j)

    f.close()