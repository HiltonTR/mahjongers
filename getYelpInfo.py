
from sre_parse import CATEGORIES
from unicodedata import category
import requests
import json
from spellchecker import SpellChecker
from dotenv import dotenv_values

# ------------------------ NECESSARY INFO TO USE YELP API ----------------------------------------
config = dotenv_values('.env')
api_key = config['YELP_API_KEY']
headers = {'Authorization': 'Bearer %s' % api_key}

url = 'https://api.yelp.com/v3/businesses/search'
#yelp params: https://www.yelp.ca/developers/documentation/v3/business_search
#categories can be Restaurants (restaurants, All), Food (food, All), Nightlife (nightlife, All)->Bars (bars, All)
#category list: https://www.yelp.ca/developers/documentation/v3/all_category_list
# ----------------------------------------------------------------------------------------------------

# --------PARAMS AREAS--------
inputs = {
    "term": "Japanese",
    "location": "Edmonton",
    "radius": "40000",
    "available": "true",
    "limit": "11",
    "categories": "restaurants, nightlife, food"
}
# -----------------------------

def inputSpellCheck(inputs):
    spell = SpellChecker();
    for key, value in inputs.items():
        correctedWord = ""
        # only correct non-empty string
        if value:
            for word in value.split():
                correctedWord += spell.correction(word) + " ";
            inputs[key] = correctedWord.strip();
    print(inputs)
    

def getRestaurants(inputs):
    params = {
        'term': inputs["term"], 
        'location': inputs["location"], 
        'radius': inputs["radius"], 
        'open_now': inputs["available"], 
        'limit': inputs["limit"], 
        'categories': inputs["categories"]
        } #if city is just searched take out radius term and add open_now = true 
    req = requests.get(url, params=params, headers=headers)
    parsedInfo = json.loads(req.text)
    restaurants = parsedInfo["businesses"]
    return restaurants

# create json file containing place name, rating and address
def writeToJson(inputs, filename):
    restaurants = getRestaurants(inputs)
    # print(restaurants)
    jsonObj = {}
    jsonObj['restaurants'] = []
    with open(filename, "w") as file:
        for restaurant in restaurants:
            # print(restaurant)
            restaurantName = restaurant["name"]
            restaurantRating = restaurant["rating"]
            restaurantAddress = restaurant["location"]["display_address"];
            jsonLine = {'name': restaurantName, 'rating': restaurantRating, 'address': restaurantAddress}
            jsonObj['restaurants'].append(jsonLine)

        json.dump(jsonObj, file, indent = 4)

# inputSpellCheck(inputs)
# writeToJson(inputs, "yelpRating.json")