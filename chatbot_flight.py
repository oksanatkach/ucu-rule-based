from preprocessing import preproc
from NER import find_loc, loc_relation, isloc
from date_regex import find_date, later_date
from chatbot_config import respond, usr


def flight(usr_txt, _from, _to, _date, tries):

    def find_data(usr_txt):
        _from = None
        _to = None
        parsed = preproc(usr_txt)
        locs = [ find_loc([], usr_txt, parsed_sent) for parsed_sent in parsed ]
        if len(locs) > 0:
            for loc in locs:
                loc_rel = loc_relation(loc, parsed[0])
                if loc_rel == 'from':
                    _from = loc[1]
                elif loc_rel == 'to':
                    _to = loc[1]
        return _from, _to, find_date(usr_txt)

    if not _from and not _to and not _date:
        if tries > 3:
            return "Sorry, I couldn't understand."
        else:
            _from, _to, _date = find_data(usr_txt)

    if not _from:
        respond("Where are you flying from?")
        usr_txt = raw_input(usr)
        parsed = preproc(usr_txt)

        if len(parsed[0]) <= 3 and isloc(usr_txt, 0, parsed[0], parsed[0][0][0], parsed[0][0][1]):
            _from = usr_txt

        else:
            if not _date:
                _from, _to, _date = find_data(usr_txt)
            else:
                _from, _to, _ = find_data(usr_txt)

        return flight(usr_txt, _from, _to, _date, tries+1)

    elif not _to:
        respond("Where are you flying to?")
        usr_txt = raw_input(usr)
        parsed = preproc(usr_txt)

        if len(parsed) <= 3 and isloc(usr_txt, 0, parsed[0], parsed[0][0][0], parsed[0][0][1]):
            _to = usr_txt

        else:
            if not _date:
                _from, _to, _date = find_data(usr_txt)
            else:
                _from, _to, _ = find_data(usr_txt)

        return flight(usr_txt, _from, _to, _date, tries + 1)

    elif _from.lower() == _to.lower():
        respond("The departure and destination cities can't be the same.")
        usr_txt = raw_input(usr)

        if not _date:
            _from, _to, _date = find_data(usr_txt)
        else:
            _from, _to, _ = find_data(usr_txt)

        return flight(usr_txt, _from, _to, _date, tries+1)

    elif not _date:
        respond("When do you want to go?")
        usr_txt = raw_input(usr)
        _date = find_date(usr_txt)
        return flight(usr_txt, _from, _to, _date, tries+1)

    elif not later_date(_date):
        respond("Sorry, the date has to be in the future.")
        usr_txt = raw_input(usr)
        _date = find_date(usr_txt)
        return flight(usr_txt, _from, _to, _date, tries+1)

    return "OK, looking for a " + _from + '-' + _to + ' flight on ' + _date + '.'
