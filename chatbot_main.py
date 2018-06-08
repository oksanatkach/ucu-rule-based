import random
import re
from preprocessing import preproc
from chatbot_flight import flight

bot = "BOT: "
usr = "YOU: "

EXIT = ('goodbye', 'exit', 'bye', 'stop', 'stahp')


def respond(txt):
    print bot + str(txt)

def match_kwds(lemmas, kwds):
    return len(lemmas.intersection(kwds)) > 0

# Here, you indicate regex or keywords that trigger the corresponding topic (function).
def matches(usr_txt):
    parsed, lemmas = preproc(usr_txt)

    # Goodbye when exiting chat.
    if match_kwds(lemmas, EXIT):
        return "Thanks for talking to me."

    else:
        if match_kwds(lemmas, ('hi', 'hello', 'greetings')):
            return hello()
        elif match_kwds(lemmas, ('flight', 'plane', 'fly', 'ticket')):
            return flight(usr_txt, None, None, None, 0)
        else:
            # Default answer when no matches found.
            return "Human, please employ logic. I don't understand."


def hello():
    # TASK: Write a function to return a response to the user's greeting randomly picked from a list of different response
    return ''


if __name__ == '__main__':
    respond("Hello, human.")
    usr_txt = ''
    while usr_txt.lower() not in EXIT:
        usr_txt = raw_input(usr)
        respond(matches(usr_txt))
