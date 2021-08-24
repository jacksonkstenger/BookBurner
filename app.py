from flask import Flask, request, redirect
import sys

from utils import send_text
from logic import logic

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    """Default Endpoint"""
    return "Default Endpoint"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)


# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     """Respond to texts with a custom text response"""
#
#     try:
#         # Parse relevant values from the request
#         from_number = request.values.get('From', None)
#         text = request.values.get('Body', None)
#
#         # Logic
#         # resp = logic(text, from_number)
#
#         return str(resp)
#
#     except TwilioRestException as e:
#         print(e)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
