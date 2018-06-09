import re
import datetime

days = r'([0-3]?[0-9])'
months_num = r'(0[1-9]|1[0-2])'
years = r'([1-2][0-9][0-9][0-9]|[0-9][0-9])'
months = {'1': 'january',
          '2': 'february',
          '3': 'march',
          '4': 'april',
          '5': 'may',
          '6': 'june',
          '7': 'july',
          '8': 'august',
          '9': 'september',
          '10': 'october',
          '11': 'november',
          '12': 'december'}
short_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
re_months = '(' + '|'.join(months.values()) + '|' + '|'.join(short_months) + ')' + '(,)? '
ends = r'((st|nd|th)( of |, | )?)'

date1 = days + '/' + months_num + '/' + years
date2 = days + ends + re_months + years
date3 = re_months + days + ends + '?,? ' + years

def find_date(text):

    if re.search(date1, text.lower()):
        res = re.search(date1, text.lower())
        return ' '.join([months[res.group(2)].title(), res.group(1) + ',', res.group(3)])

    elif re.search(date2, text.lower()):
        res = re.search(date2, text.lower())
        return ' '.join([res.group(5).title(), res.group(1) + ',', res.group(7)])

    elif re.search(date3, text.lower()):
        res = re.search(date3, text.lower())
        return ' '.join([res.group(1).title(), res.group(3) + ',', res.group(7)])


def later_date(date):
    now = datetime.datetime.now()
    cur = now.strftime('%B %d, %Y')
    return now.strptime(cur, '%B %d, %Y') < now.strptime(date, '%B %d, %Y')


if __name__ == '__main__':
    # Test your stuff.
    print find_date('June 15, 2018')
    # print find_date('There is no date in this sentence.')
    # print find_date('I would like to book a flight on 05/11/2018, please.')
