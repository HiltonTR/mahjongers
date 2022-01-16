import os

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def extract_google_reviews(driver, resturauntName):
    driver.get('https://www.google.com/?hl=en')
    driver.find_element_by_name('q').send_keys(resturauntName)
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()
    except:
        driver.find_element_by_name('q').send_keys(Keys.ENTER)

    Header = driver.find_element_by_css_selector('div.kp-header')
    Rating = Header.find_element_by_class_name("Aq14fc").get_attribute('innerHTML')
    Link = Header.find_element_by_partial_link_text('Google reviews')
    numberOfReviews = int((Link.text.split()[0]).replace(',', ''))
    resturauntImage = Header.find_element_by_xpath('div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]').get_attribute('href')
    Link.click()

    allReviews = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.gws-localreviews__google-review')))
    if(numberOfReviews > 20):
        totalReviews = 20
    else:
        totalReviews = numberOfReviews

    while len(allReviews) < totalReviews:
        driver.execute_script('arguments[0].scrollIntoView(true);', allReviews[-1])
        WebDriverWait(driver, 10, 0.1).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class$="activityIndicator"]')))
        allReviews = driver.find_elements_by_css_selector('div.gws-localreviews__google-review')

    reviewsSearched = 0
    text = open("review.txt", "w+", encoding='utf-8')
    for review in allReviews:
        try:
            element = review.find_element_by_css_selector('span.review-full-text')
            reviewsSearched += 1
        except NoSuchElementException:
            element = review.find_element_by_xpath('div[1]/div[3]/div[2]/span[1]')
            reviewsSearched += 1
            
        review = element.get_attribute('textContent')
        text.write(review)
        text.write("\n")
        
    text.close()
    return reviewsSearched, numberOfReviews, Rating, resturauntImage

def test():
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(os.getcwd() + r"/chromedriver_win32/chromedriver.exe")
    reviewsSearched, numberOfReviews, Rating, resturauntImage = extract_google_reviews(driver, 'Izakaya O-Tori')
    print(resturauntImage)
    driver.quit()
    #print(reviewsSearched, " " , numberOfReviews, " ", Rating)

test()