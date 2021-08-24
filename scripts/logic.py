# Import Dependencies
from twilio.twiml.messaging_response import MessagingResponse
from twilio.base.exceptions import TwilioRestException

def logic(text, from_number):

    # Start our TwiML response
    resp = MessagingResponse()

    # Respond to the texter
    resp.message("Message received! You said {}".format(text))

    return resp
