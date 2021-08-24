from twilio.twiml.messaging_response import MessagingResponse
from twilio.base.exceptions import TwilioRestException
from flask import Flask, request, redirect
import sys
import os

from utils import send_text
from logic import logic
from title_to_link import title_to_link

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

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    """Default Endpoint"""
    return "Default Endpoint"


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to texts with a custom text response"""

    try:
        # Start our TwiML response
        resp = MessagingResponse()

        # Parse relevant values from the request
        from_number = request.values.get('From', None)
        text = request.values.get('Body', None)

        print("Received from: {}".format(from_number))
        print("Text: {}".format(text))

        # Add a message
        resp.message("Time to burn some books! I heard you say {}.".format(text))

        # Logic
        # resp = logic(text, from_number)


        timeout = 10

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

            # Click the link of the first book
            # element = EC.presence_of_element_located((By.XPATH, '//*[@id="4542"]'))
            element = EC.presence_of_element_located((By.XPATH, '/html/body/table[3]/tbody/tr[2]/td[3]/a[2]'))
            WebDriverWait(driver, timeout).until(element)
            driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[2]/td[3]/a[2]').click()

            # Click the link to get to pdfs
            element = EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td[3]/b/a'))
            WebDriverWait(driver, timeout).until(element)
            driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/b/a').click()

            # Click the final link woohoo!
            element = EC.presence_of_element_located((By.XPATH, '//*[@id="download"]/h2/a'))
            WebDriverWait(driver, timeout).until(element)
            final_element = driver.find_element_by_xpath('//*[@id="download"]/h2/a')
            final_url = final_element.get_attribute("href")

        except Exception as e:
            print(e)
            final_url = "No URL Found"





        # url = title_to_link(text)
        resp.message("Your URL SIR")
        resp.message(final_url)

        return str(resp)

    except TwilioRestException as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
