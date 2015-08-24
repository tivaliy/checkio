# http://www.checkio.org/mission/calls-home/
__author__ = 'Vitalii K'

import math


def total_cost(calls):
    total = 0
    # Collect all day long calls
    dates_cost_dict = {}
    for call in calls:
        # Round + Up seconds to minutes
        duration_time = math.ceil(float(call.rsplit(' ', 1)[1]) / 60)
        # Check if this call is on the same day
        if call.split(' ', 2)[0] not in dates_cost_dict:
            dates_cost_dict[call.split(' ', 2)[0]] = duration_time
        else:
            dates_cost_dict[call.split(' ', 2)[0]] = dates_cost_dict.get(
                call.split(' ', 2)[0]) + duration_time
    # Make calculation
    for v in dates_cost_dict.values():
        if v > 100:
            total += 100 + abs(100 - v) * 2
        else:
            total += v
    return total


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"
