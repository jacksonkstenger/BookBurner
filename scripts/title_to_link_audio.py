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

def title_to_link_audio(url):
    try:
        url += ' audiobook'
        formatted_url = url.replace(' ','+')
        url_to_search = rf"https://www.youtube.com/results?search_query={formatted_url}"
        #with requests.Session() as s:
        #    resp = s.get(url_to_search)
        #    redirect_url = resp.history[1].url
        #    print(redirect_url)

        # Using Chrome to access web
        DRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', None)

        DRIVER_PATH = r"C:\Users\Jackson\Downloads\chromedriver_win32\chromedriver.exe"

        driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        # Open the website
        driver.get(url_to_search)

        # Get the title from Google's search box
        video_link1 = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
        #print(video_link1)
        video_link2 = video_link1[0].get_attribute("href")
        #print(video_link2)
        final_video_link = rf"www.youtube.com/{video_link2}"
        driver.close()

        return final_video_link
    except:
        driver.close()
        return None


if __name__ == "__main__":
    # url = "https://api.twilio.com/2010-04-01/Accounts/AC15abe67bd635f83f4fa678d17ccf9e6d/Messages/MM2731b3d74b95937e4caea55f86530858/Media/ME0b75de784bb7dd2b33d4e97ddc156ccd"
    url = "https://api.twilio.com/2010-04-01/Accounts/AC15abe67bd635f83f4fa678d17ccf9e6d/Messages/MM5da7bbd6c8af667b494b94d1dfb8c215/Media/ME828bbe7ea2257e7dbb0b370a7eba1908"
    print(title_to_link_audio(url))
