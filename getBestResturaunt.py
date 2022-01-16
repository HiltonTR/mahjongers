import json
import requests
from bs4 import BeautifulSoup
import re

# Code found from https://stackoverflow.com/questions/52910297/pydictionary-word-has-no-synonyms-in-the-api
# Finds the thesaurus words for a given word to search
def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] # 'css-1gyuw4i eh475bn0' for less relevant synonyms

# Returns a dictionary of restaurants in order of value
def getRestaurantOrder(name, google_rating, num_reviews, environment):
    # Grabs an array of synonyms for given word
    # TODO CHANGE THE WORD TO THE INPUT FROM GULLEY
    word = environment.lower()
    array1 = synonyms(word).copy()
    print(array1)

    # JSON file for yelp reviews for each restaurant
    file = open("yelpRating.json")
    data = json.load(file)

    # Open text file
    text_file = open("review.txt", "r" , encoding='utf-8')
 
    # Read whole file to a string and then convert to a list
    dataReview = text_file.read()
    dataReview = re.sub('[^A-Za-z0-9\s]+', '', dataReview)
    result = dataReview.split()
 
    # Dictionary for holding Restaurants and their final rating
    restaurantOrder = {}

    # Grabbing data from JSON files
    google_rating = google_rating

    yelp_rating = 0
    for j in data["restaurants"]:
        if name == j["name"]:
            yelp_rating = float(j["rating"])

    # Counting the amount of times the synonyms appear in the reviews
    amount = 0
    for x in array1:
        amount += result.count(x[:-1])
    amount += result.count(word)
    print(amount)

    # Doing the calculation
    calculation = (amount / float(num_reviews)) + ((float(google_rating) + yelp_rating)/2) 
    restaurantOrder[name] = calculation

    # Close files and return dictionary
    file.close()
    text_file.close()

    print(restaurantOrder)
    
    return restaurantOrder

def main():
    # Test function
    getRestaurantOrder("Japonais", 5, 100)

if __name__ == "__main__":
    main()