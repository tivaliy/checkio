# http://www.checkio.org/mission/weekend-counter/solve/
__author__ = 'Vitalii K'

import datetime
from datetime import date


def checkio(from_date, to_date):
    weekdays_count = 0
    # Get total number of days between "start" and "stop" dates in int
    for i in range(abs((to_date - from_date).days) + 1):
        weekdays_count += 1 if from_date.isoweekday() == 6 or from_date.isoweekday() == 7 else 0
        # Increment day
        from_date += datetime.timedelta(days=1)
    return weekdays_count


print(checkio(date(2013, 2, 2), date(2013, 2, 3)))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
