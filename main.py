from getGoogleReviews import extract_google_reviews
from getYelpInfo import writeToJson
from getBestResturaunt import getRestaurantOrder

import os
import time

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


main()