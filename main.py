from getGoogleReviews import extract_google_reviews

import os

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException



def main():
    driver = webdriver.Chrome(os.getcwd() + r"/chromedriver_win32/chromedriver.exe")
    a, b, c = extract_google_reviews(driver, 'japonais')
    driver.quit()
    print(a)
    print(b)
    print(c)