from getGoogleReviews import extract_google_reviews
from getYelpInfo import writeToJson
from getBestResturaunt import getRestaurantOrder

import os
import time
import json

from selenium import webdriver

inputs = {
    "term": "Japo",
    "location": "Edmonton",
    "radius": "40000",
    "available": "true",
    "limit": "10",
    "categories": ""
}

def main():
    writeToJson(inputs, "yelpRating.json")

    driver = webdriver.Chrome(os.getcwd() + r"/chromedriver_win32/chromedriver.exe")
    reviewsSearched, numberOfReviews, Rating = extract_google_reviews(driver, 'japonais')
    driver.quit()    
    
    
    print(reviewsSearched)
    print(numberOfReviews)
    print(Rating)

    getRestaurantOrder("Japonais", Rating, reviewsSearched)


#main()

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
getRestaurants()
