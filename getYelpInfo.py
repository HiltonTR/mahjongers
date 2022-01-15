import requests
import json

api_key = '9BqKWX1mOXXiQqomscePk5OUJ4YhoI2BS-cNLAkQq63KTLoONoPxyvJ9YCDlCHRoskLeUSn70s4gCIrwrL6T3TgBiSo4o-bwqBFBcMmzUS3-tarHNs6Bhw8mWHziYXYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url = 'https://api.yelp.com/v3/businesses/search'

params = {'term':'Cozy Bar','location':'Edmonton', 'radius':'40000', 'open_now':'true', 'limit':'50', } #if city is just searched take out radius term and add open_now = true 

req = requests.get(url, params=params, headers=headers)

yelpInfo = json.loads(req.text)
# print(yelpInfo)

restaurants = yelpInfo["businesses"]
jsonDict= {};
for restaurant in restaurants:
    restaurantName = restaurant["name"];
    restaurantRating = restaurant["rating"];
    jsonDict [restaurantName] = restaurantRating;
    # print("Name:", business["name"])
    # print("Rating:", business["rating"])

#print place name and rating to json
def writeToJson(data, filename = "yelpRating.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent = 4)

writeToJson(jsonDict);