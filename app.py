# Import Dependencies
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.base.exceptions import TwilioRestException
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import urllib.parse
# import time
import sys
# import os
sys.path.append('scripts/')

from utils import send_text
from title_to_link import title_to_link#title_to_link_old#title_to_link
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
            text = image_to_title(media_url)
            if text == None:
                text = image_to_title_og(media_url)
        
        # Add a message
        ##resp.message("Time to burn some books! Here's a free version of {}.".format(text))
        send_text("Time to burn some books! Here's a free version of {}.".format(text), from_number)

        # Get a link to the pdf of this book
        url = title_to_link(text)#title_to_link_old(text)#title_to_link(text)
        print(rf"FINAL URL: {url}")
        audio_url = title_to_link_audio(text)
        print(rf"AUDIO URL: {audio_url}", )
        if url is None:
            url == ""
        if audio_url is None:
            audio_url == ""
        #if (url == "") and (audio_url == ""):
        if (not url) and (not audio_url):
            #resp.message("I can't find a pdf of this title. Try including more details.")
            send_text("I can't find a pdf of this title. Try including more details.", from_number)
        elif (not not url) and (not audio_url):
            #resp.message("{}".format(url))
            send_text("{}".format(url), from_number)
        elif (not url) and (not not audio_url):
            #resp.message(rf"I can't find a pdf of this title. I did find this link, it may be an audio book: {audio_url}")
            send_text(rf"I can't find a pdf of this title. I did find this link, it may be an audio book: {audio_url}", from_number)
        else:
            #resp.message(rf"{url} (possible audio version: {audio_url})")
            send_text(rf"{url} (possible audio version: {audio_url})", from_number)
        return str(resp)

    except TwilioRestException as e:
        print(e)
        #resp.message("I can't find a pdf of this title.")
        send_text("I can't find a pdf of this title.", from_number)
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
