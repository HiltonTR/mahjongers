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
    writeToJson(inputs, "yelpRating.json")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(os.getcwd() + r"/chromedriver_win32/chromedriver.exe", options = chrome_options)
    reviewsSearched, numberOfReviews, Rating = extract_google_reviews(driver, 'skyview the keg')
    driver.quit()    
    
    
    print(reviewsSearched)
    print(numberOfReviews)
    print(Rating)
    getRestaurantOrder("Japonais", Rating, reviewsSearched)


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