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

def image_to_title(url):
    resp = requests.get("https://www.google.com/searchbyimage?image_url=https%3A%2F%2Fapi.twilio.com%2F2010-04-01%2FAccounts%2FAC15abe67bd635f83f4fa678d17ccf9e6d%2FMessages%2FMM2731b3d74b95937e4caea55f86530858%2FMedia%2FME0b75de784bb7dd2b33d4e97ddc156ccd&encoded_image=&image_content=&filename=&hl=en")
    # print(resp)
    # print(resp.text)
    # print(resp.history)
    # print(resp.history[0])
    redirect_url = resp.history[1].url

    redirect_resp = requests.get(redirect_url)
    print(redirect_url)
    # print(redirect_resp)
    # print(redirect_resp.text)
    # print(redirect_resp.content)

    # final_resp = requests.get(redirect_url)
    # soup = BeautifulSoup(redirect_resp.text, 'html.parser')
    # print(soup)

    # search_box = soup.find_all('input')
    # print(search_box)
    # print(search_box.get_attribute("value"))

    # Using Chrome to access web
    DRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', None)
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    # Open the website
    driver.get(redirect_url)

    search_box = driver.find_elements(By.XPATH, '//input')
    # for x in search_box:
    #     print(x.get_attribute("value")
    title = search_box[0].get_attribute("value")
    return title
    # print(search_box[1].get_attribute("value"))
    # print(search_box[2].get_attribute("value"))
    # print(search_box)
    # print(search_box.get_attribute("value"))


def image_to_title_old(url):
    # Using Chrome to access web
    # DRIVER_PATH = r'/Users/gstenger/Downloads/chromedriver 2'
    DRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', None)
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    try:
        # Open the website
        driver.get('https://images.google.com/')

        # Find cam button
        cam_button = driver.find_elements_by_xpath("//div[@aria-label=\"Search by image\" and @role=\"button\"]")[0]
        cam_button.click()

        # Find upload tab
        upload_tab = driver.find_elements_by_xpath("//*[contains(text(), 'Upload an image')]")[0]
        upload_tab.click()

        # # Click upload from URL
        # upload_tab = driver.find_elements_by_xpath('//*[@id="gsr"]')[0]
        # upload_tab.click()

        # Find image input
        upload_btn = driver.find_element_by_name('encoded_image')
        upload_btn.send_keys(url)

        element = driver.find_element_by_xpath('//*[@id="sbtc"]/div[2]/div[2]/input')
        my_result = element.get_attribute("value")

        return my_result

    except Exception as e:
        print(e)

    driver.quit()

    return my_result

if __name__ == "__main__":
    url = "https://api.twilio.com/2010-04-01/Accounts/AC15abe67bd635f83f4fa678d17ccf9e6d/Messages/MM2731b3d74b95937e4caea55f86530858/Media/ME0b75de784bb7dd2b33d4e97ddc156ccd"
    image_to_title(url)


    # import requests
    # import webbrowser
    #
    # filePath = 'data/image.jpeg'
    # searchUrl = 'http://www.google.hr/searchbyimage/upload'
    # multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
    # response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    # fetchUrl = response.headers['Location']
    # print(fetchUrl)
    # # webbrowser.open(fetchUrl)
    #
    # /html/body/div[4]/div[2]/div[1]/form/div[1]/div[1]/div[2]/div[2]/div[2]/input
