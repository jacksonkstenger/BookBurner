from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


def image_to_title():
    # Using Chrome to access web
    DRIVER_PATH = r'/Users/gstenger/Downloads/chromedriver 2'
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

        # Find image input
        upload_btn = driver.find_element_by_name('encoded_image')
        upload_btn.send_keys(os.getcwd()+"/image.jpeg")

        element = driver.find_element_by_xpath('//*[@id="sbtc"]/div[2]/div[2]/input')
        my_result = element.get_attribute("value")

        return my_result

    except Exception as e:
        print(e)

    driver.quit()

    return my_result

if __name__ == "__main__":
    print(image_to_title())
