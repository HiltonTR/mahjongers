
from sre_parse import CATEGORIES
from unicodedata import category
import requests
import json
import enum
# ------------------------ NECESSARY INFO TO USE YELP API ----------------------------------------
api_key = '9BqKWX1mOXXiQqomscePk5OUJ4YhoI2BS-cNLAkQq63KTLoONoPxyvJ9YCDlCHRoskLeUSn70s4gCIrwrL6T3TgBiSo4o-bwqBFBcMmzUS3-tarHNs6Bhw8mWHziYXYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url = 'https://api.yelp.com/v3/businesses/search'
#yelp params: https://www.yelp.ca/developers/documentation/v3/business_search
#categories can be Restaurants (restaurants, All), Food (food, All), Nightlife (nightlife, All)->Bars (bars, All)
#category list: https://www.yelp.ca/developers/documentation/v3/all_category_list
# ----------------------------------------------------------------------------------------------------

# --------PARAMS AREAS--------
term = 'Cozy Bar';
location = 'Edmonton';
radius = '40000';
available = 'true';
limit = '10';
categories = '';
# -----------------------------

def getRestaurants():
    params = {'term': term,'location': location, 'radius': radius, 'open_now': available, 'limit': limit} #if city is just searched take out radius term and add open_now = true 
    req = requests.get(url, params=params, headers=headers)
    parsedInfo = json.loads(req.text)
    restaurants = parsedInfo["businesses"]
    return restaurants


# create json file containing place name, rating and address
def writeToJson(filename = "yelpRating.json"):
    restaurants = getRestaurants()
    print(restaurants)
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

writeToJson();