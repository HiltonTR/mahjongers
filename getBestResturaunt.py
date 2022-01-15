import json
import requests
from bs4 import BeautifulSoup

# Code found from https://stackoverflow.com/questions/52910297/pydictionary-word-has-no-synonyms-in-the-api
def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] # 'css-1gyuw4i eh475bn0' for less relevant synonyms

# Grabs an array of synonyms for given word
# TODO CHANGE THE WORD TO THE INPUT FROM GULLEY
word = "hi".lower()
array1 = synonyms(word).copy()
print(array1)

# JSON file for yelp reviews for each restaurant
#file = open(yelpRating.json)
#data = json.load(file)

# Dictionary for holding Restaurants and their final rating
restaurantOrder = {}

for i in range (1, 11):
    # There will be 10 JSON files for each restaurant which contains the ratings
    f = open('data' + str(i) + '.json')

    data1 = json.load(f)

    restaurant_name = (data1["name"])
    google_rating = int(data1["rating"])
    num_reviews = int(data1["numReviews"])
#    yelp_rating = int(data[restaurant_name])
    reviews = (data1["reviews"]).lower()
    amount = 0
    result = reviews.split()

    for x in array1:
        amount += result.count(x[:-1])
    amount += result.count(word)
    print(amount)

    calculation = (amount / num_reviews) * ((google_rating + yelp_rating)/2)
    restaurantOrder[restaurant_name] = calculation

    f.close()

#file.close()
