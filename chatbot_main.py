import random
import re
from chatbot_flight import flight
from chatbot_config import respond, usr


# Here, you indicate regex or keywords that trigger the corresponding topic (function).
def matches(usr_txt):

    # Goodbye when exiting chat.
    if re.match(r'exit|bye|stop|stahp', usr_txt):
        return "Thanks for talking to me."

    else:
        if re.match(r'.*(hi|hello|greetings).*', usr_txt):
            return hello()
        elif re.match(r'.*(flight|plane|fly|ticket).*', usr_txt):
            return flight(usr_txt, None, None, None, 0)
        else:
            # Default answer when no matches found.
            return "Human, please employ logic. I don't understand."


def hello():
    greetings = ["How can I help you?", "What can I do for you?"]
    return random.choice(greetings)


if __name__ == '__main__':
    respond("Hello, human.")
    usr_txt = ''
    while not re.match(r'hi|hello|greetings', usr_txt):
        usr_txt = raw_input(usr)
        respond(matches(usr_txt))
