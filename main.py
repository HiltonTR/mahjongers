import platform
from getGoogleReviews import extract_google_reviews
from getYelpInfo import writeToJson
from getBestResturaunt import getRestaurantOrder
from collections import OrderedDict


import os
import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main(content):
    mood = content[1]
    if (len(content) == 5):
        inputs = {
            "term": content[2],
            "location": content[4],
            "radius": content[0] + "000",
            "available": "false",
            "limit": "5",
            "categories": "restaurants, nightlife, food"
        }
    else:
        inputs = {
            "term": content[2],
            "location": content[3],
            "radius": content[0] + "000",
            "available": "false",
            "limit": "5",
            "categories": "restaurants, nightlife, food"
        }
    

    # Creating the dictionary to later sort the restaurants by value
    restaurant_dict = {}

    # Thomas Code
    writeToJson(inputs, "yelpRating.json")

    restaurantList, address_list = getInfo()
    # Hilton Code
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    print(platform.system())
    if (platform.system() == "Darwin"):
        driver = webdriver.Chrome(os.getcwd() + r"/chromedriver_mac64_m1/chromedriver", options = chrome_options)
    else:
        driver = webdriver.Chrome(os.getcwd() + r"/chromedriver_win32/chromedriver.exe", options = chrome_options)
    for i in range(0, len(restaurantList)):
        try:
            reviewsSearched, numberOfReviews, Rating = extract_google_reviews(driver, restaurantList[i] + " " + inputs['location'])
            # Jakob's Code
            restaurant_dict.update(getRestaurantOrder(restaurantList[i], Rating, reviewsSearched, mood))
        except:
            pass

    sort_order = sorted(restaurant_dict.items(), key=lambda x: x[1], reverse=True)
    driver.quit()
    ordered_restaurants = {}
    for i in sort_order:
        ordered_restaurants[i[0]] = i[1]

    print(ordered_restaurants)
    return(ordered_restaurants)


def getInfo():
    restaurant_list = []
    address_list = []

    # Opening JSON file
    f = open('yelpRating.json')
 
    # returns JSON object as
    # a dictionary
    data = json.load(f)
 
    # Iterating through the json
    # list
    for i in data['restaurants']:
        restaurant_list.append(i["name"])
        address_list.append((((i["address"])[-2]).split())[0])
 
    # Closing file
    f.close()
    #print(restaurant_list)
    return restaurant_list, address_list
