import re
import datetime


def find_date(text):

    dates = r'' # TASK: Write your regex here

    res = re.search(dates, text.lower())
    if res:
        return res.group()
    else:
        return None


def later_date(date):
    now = datetime.datetime.now()
    cur = now.strftime('%B %d, %Y')
    return now.strptime(cur, '%B %d, %Y') < now.strptime(date, '%B %d, %Y')

if __name__ == '__main__':
    # Test your stuff.
    print find_date('The date is June 5th, 2016.')
    print find_date('There is no date in this sentence.')
    print find_date('I would like to book a flight on 05/11/2018, please.')
    print find_date('23rd of Jan 94')
