# Import Dependencies
from twilio.twiml.messaging_response import MessagingResponse
from twilio.base.exceptions import TwilioRestException

def logic():
    # Start our TwiML response
    resp = MessagingResponse()
    if 'done' in text.lower().strip():
        praise = get_praise()
        resp.message(praise)
        done(text, from_number)
    elif 'error' in lower_text:
        resp.message("Cool, I hear you have an error. If you formatted the complaint as follows, you're good to go.")
        resp.message("ERROR: This is my complaint blah blah nat's booty 2 tasty")
        error(text, from_number)
    elif 'away' in lower_text or 'sub' in lower_text:
        resp.message("I hear you awayyyy, have fun on your trip queen")
        away(text, from_number)
    elif 'remind' in lower_text:
        requested_remind(from_number)
    elif any(word in lower_text for word in ['commands', '?', 'halp']):
        text_all("You can type DONE to complete a task, AWAY/SUB to have a friend sub in, ERROR to report an error, REMIND to remind yourself of your current task, and COMMANDS to see this text again.")
    else:
        resp.message("This is an invalid method. Try texting COMMANDS for a list of commands.")
