from getGoogleReviews import extract_google_reviews
from getYelpInfo import writeToJson
from getBestResturaunt import getRestaurantOrder

import os
import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

inputs = {
    "term": "Japonais",
    "location": "Edmonton",
    "radius": "40000",
    "available": "true",
    "limit": "10",
    "categories": ""
}

def main():
    # Creating the dictionary to later sort the restaurants by value
    restaurant_dict = {}

    # Thomas Code
    writeToJson(inputs, "yelpRating.json")

    restaurantList = getRestaurants()
    # Hilton Code
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(os.getcwd() + r"/chromedriver_win32/chromedriver.exe", options = chrome_options)
    for restaurants in restaurantList:
        reviewsSearched, numberOfReviews, Rating = extract_google_reviews(driver, restaurants)
        # Jakob's Code
        restaurant_dict.update(getRestaurantOrder(restaurants, Rating, reviewsSearched, "unique"))

    driver.quit()
    print(restaurant_dict)


def getRestaurants():
    restaurant_list = []

    # Opening JSON file
    f = open('yelpRating.json')
 
    # returns JSON object as
    # a dictionary
    data = json.load(f)
 
    # Iterating through the json
    # list
    for i in data['restaurants']:
        restaurant_list.append(i["name"])
 
    # Closing file
    f.close()
    
    #print(restaurant_list)
    return restaurant_list

main()