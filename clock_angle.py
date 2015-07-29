# http://www.checkio.org/mission/clock-angle/
__author__ = 'Vitalii K'


from datetime import datetime


def clock_angle(time):
    # Convert 24:00 to 12:00 time format
    d = datetime.strptime(time, '%H:%M').strftime('%I:%M')
    hours, minutes = [int(x) for x in d.split(':')]
    # 1 min = 6 grad, 1 hour = 5 min * 6 grad
    h_grad = hours * 30 + ((minutes / 12) * 6)
    m_grad = minutes * 6
    # Get absolute value + return min angel
    return min(abs(m_grad - h_grad), 360 - abs(m_grad - h_grad))


if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

