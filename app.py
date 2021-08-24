from twilio.twiml.messaging_response import MessagingResponse
from twilio.base.exceptions import TwilioRestException
from flask import Flask, request, redirect
import sys
import os

from utils import send_text
from logic import logic
from title_to_link import title_to_link

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

        # url = title_to_link(text)
        resp.message("Your URL SIR")
        # resp.message(url)

        return str(resp)

    except TwilioRestException as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
