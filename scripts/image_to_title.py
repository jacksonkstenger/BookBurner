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
    try:
        url_to_search = "https://www.google.com/searchbyimage?image_url={}&encoded_image=&image_content=&filename=&hl=en".format(image_url)
        resp = requests.get(url_to_search)
        redirect_url = resp.history[1].url

        # Using Chrome to access web
        DRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', None)
        #DRIVER_PATH = r"C:\Users\Jackson\Downloads\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        # Open the website
        driver.get(redirect_url)

        # Get the title from Google's search box
        search_box = driver.find_elements(By.XPATH, '//input')
        title = search_box[0].get_attribute("value")
        driver.close()

        return title
    except:
        driver.close()
        return None


if __name__ == "__main__":
    url = "https://api.twilio.com/2010-04-01/Accounts/AC15abe67bd635f83f4fa678d17ccf9e6d/Messages/MM5da7bbd6c8af667b494b94d1dfb8c215/Media/ME828bbe7ea2257e7dbb0b370a7eba1908"
    print(image_to_title(url))
