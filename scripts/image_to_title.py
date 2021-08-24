from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import os
import sys
sys.path.append('../data/')

def image_to_title(image_url):

    url_to_search = "https://www.google.com/searchbyimage?image_url={}&encoded_image=&image_content=&filename=&hl=en".format(image_url)
    resp = requests.get(url_to_search)
    redirect_url = resp.history[1].url
    print(redirect_url)

    # Using Chrome to access web
    DRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', None)
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    # Open the website
    driver.get(redirect_url)

    # Get the title from Google's search box
    search_box = driver.find_elements(By.XPATH, '//input')
    title = search_box[0].get_attribute("value")

    return title
    

if __name__ == "__main__":
    url = "https://api.twilio.com/2010-04-01/Accounts/AC15abe67bd635f83f4fa678d17ccf9e6d/Messages/MM2731b3d74b95937e4caea55f86530858/Media/ME0b75de784bb7dd2b33d4e97ddc156ccd"
    print(image_to_title(url))
