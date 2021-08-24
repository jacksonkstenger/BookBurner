from flask import Flask, request, redirect
import sys

from utils import done, away, error, requested_remind, get_person, text_all, _send_reminders, get_praise
from logic import logic

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    """Default Endpoint"""
    return "Default Endpoint"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to texts with a custom text response"""

    try:
        # Parse relevant values from the request
        from_number = request.values.get('From', None)
        text = request.values.get('Body', None)

        # Logic
        logic(text, from_number)

    except TwilioRestException as e:
        print(e)
        sys.stdout.flush()

    return str(resp)

@app.route("/send_reminders", methods=['GET', 'POST'])
def send_reminders():
    try:
        _send_reminders()
        return {}
    except Exception as e:
        print(e)
        return {}

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
