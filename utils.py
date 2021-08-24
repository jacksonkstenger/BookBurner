from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

ACCOUNT_SID = os.environ.get('ACCOUNT_SID', None)
AUTH_TOKEN = os.environ.get('AUTH_TOKEN', None)
BOOKBURNER_NUMBER = os.environ.get('BOOKBURNER_NUMBER', None)

def send_text(message, phone_number):

    # Set up the Twilio Sid and Auth Token
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Create the message
    try:
        message = client.messages.create(
            body = message,
            from_ = BOOKBURNER_NUMBER,
            media_url = [],
            to = phone_number
        )
    except TwilioRestException as e:
        print(e)

if __name__ == "__main__":
    send_text('Testing jackssoooon', '+19252863862')
