from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import requests
# import time
import os
import sys
sys.path.append('../data/')

def title_to_link_audio(url):
    try:
        url += ' audiobook'
        formatted_url = url.replace(' ','+')
        url_to_search = rf"https://www.youtube.com/results?search_query={formatted_url}&sp=EgIYAg%253D%253D"

        # Using Chrome to access web
        DRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', None)
        #DRIVER_PATH = r"C:\Users\Jackson\Downloads\chromedriver_win32\chromedriver.exe"
        print(DRIVER_PATH)

        driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        # Open the website
        driver.get(url_to_search)

        # Get the title from Google's search box
        #video_link1 = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
        video_link1 = driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
        video_link2 = video_link1[0].get_attribute("href")
        final_video_link = rf"{video_link2}"
        driver.close()
        print("final video link")
        print(final_video_link)
        return final_video_link

    except:
        driver.close()
        return None


if __name__ == "__main__":
    url = "Theory of Games and Economic Behavior"
    print(title_to_link_audio(url))
