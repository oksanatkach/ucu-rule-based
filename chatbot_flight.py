from preprocessing import preproc
from NER import find_loc, loc_relation, isloc
from date_regex import find_date, later_date
from chatbot_config import respond, usr


def flight(usr_txt, _from, _to, _date, tries):

    if not _from and not _to and not _date:
        return "Sorry, I couldn't understand."

    # What if there's no departure city?

    # What if there's no destination city?

    # What if departure and destination are the same?

    # What if there's no date?

    # What if the date is in the future?

    return "OK, looking for a " + _from + '-' + _to + ' flight on ' + _date + '.'
