# Import Dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib.parse
import time
import os

def title_to_link(title):

    timeout = 6

    try:
        # Using Chrome to access web
        # DRIVER_PATH = r'/Users/gstenger/Downloads/chromedriver 2'
        DRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', None)
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        # Open the website
        driver.get('https://libgen.is/')

        # Click the search box
        element = EC.presence_of_element_located((By.XPATH, '//*[@id="searchform"]'))
        WebDriverWait(driver, timeout).until(element)
        driver.find_element_by_xpath('//*[@id="searchform"]').click()

        # Type title into the box
        driver.find_element_by_xpath('//*[@id="searchform"]').send_keys(title)
        # WebDriverWait(driver, timeout).until(element)

        # Click the search button
        element = EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody[2]/tr/td[2]/form/input[2]'))
        # element = driver.find_element_by_xpath('/html/body/table/tbody[2]/tr/td[2]/form/input[2]')
        WebDriverWait(driver, timeout).until(element)
        driver.find_element_by_xpath('/html/body/table/tbody[2]/tr/td[2]/form/input[2]').click()

        # Click the link of the first pdf
        found = False
        i = 0
        while i < 10 and found == False:
            pdf_element = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[{}]/td[9]'.format(2+i))
            if pdf_element.text == "pdf":
                try:
                    element = EC.presence_of_element_located((By.XPATH, '/html/body/table[3]/tbody/tr[2]/td[3]/a[2]'))
                    WebDriverWait(driver, timeout).until(element)
                    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[2]/td[3]/a[2]').click()
                except:
                    element = EC.presence_of_element_located((By.XPATH, '/html/body/table[3]/tbody/tr[2]/td[3]/a'))
                    WebDriverWait(driver, timeout).until(element)
                    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[2]/td[3]/a').click()
                found = True
            else:
                i += 1

        # Click the link to get to pdfs
        element = EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td[3]/b/a'))
        WebDriverWait(driver, timeout).until(element)
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/b/a').click()

        # Click the final link woohoo!
        element = EC.presence_of_element_located((By.XPATH, '//*[@id="download"]/h2/a'))
        WebDriverWait(driver, timeout).until(element)
        final_element = driver.find_element_by_xpath('//*[@id="download"]/h2/a')
        final_url = final_element.get_attribute("href")

        return final_url

    except Exception as e:
        print(e)


if __name__ == "__main__":
    title = 'nonlinear dynamics and chaos strogatz'
    print(title_to_link(title))
