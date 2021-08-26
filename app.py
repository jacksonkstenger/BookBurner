# Import Dependencies
from twilio.twiml.messaging_response import MessagingResponse
from twilio.base.exceptions import TwilioRestException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from flask import Flask, request, redirect
import urllib.parse
import time
import sys
import os
sys.path.append('scripts/')

from utils import send_text
from title_to_link import title_to_link
from image_to_title import image_to_title as image_to_title_og
from image_to_title_barcode import image_to_title
from title_to_link_audio import title_to_link_audio
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    """Default Endpoint"""
    return "Default Endpoint"


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to texts with a custom response"""

    try:

        # Start our TwiML response
        resp = MessagingResponse()

        # Parse relevant values from the request
        from_number = request.values.get('From', None)
        text = request.values.get('Body', None)
        media_url = request.values.get('MediaUrl0', None)

        print("Received from: {}".format(from_number))
        print("Text: {}".format(text))
        print("Media URL: {}".format(media_url))

        # If an image was attached, get the title of the book from the image
        if media_url is not None:
            print("Here in the media url None condition")
            text = image_to_title(media_url)
            if text == None:
                text = image_to_title_og(media_url)
            if text == None:
                resp.message("I can't find a pdf of this title. Try including more details.")
                return str(resp)
                

        # Add a message
        resp.message("Time to burn some books! Here's a free version of {}.".format(text))

        # Get a link to the pdf of this book
        url = title_to_link(text)
        print("FINAL URL: {}", url)
        audio_url = title_to_link_audio(text)
        print("AUDIO URL: {}", url)
        
        if (url == "") and (audio_url == ""):
            resp.message("I can't find a pdf of this title. Try including more details.")
        elif (url != "") and (audio_url == ""):
            resp.message("{}".format(url))
        elif (url == "") and (audio_url != ""):
            resp.message(rf"I can't find a pdf of this title. I did find this audio book: {audio_url}")
        else:
            resp.message(rf"{url} (audio version: {audio_url})"
            
        return str(resp)

    except TwilioRestException as e:
        print(e)
        resp.message("I can't find a pdf of this title. Try including more details.")
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
