# http://www.checkio.org/mission/morse-clock/
__author__ = 'Vitalii K'


TRUNC = [4, 2, 0, 3, 2, 0, 3, 2]


def checkio(time_string):
    # Create common format, e.g. 1:2:3 -> 01:02:03  01:2:03 -> 01:02:03
    t_str = ':'.join('{0:02}'.format(int(i)) for i in time_string.split(':'))
    # Convert to binary string format, eg 01 0000 : 011 0111 : 100 1001
    t_str = ' '.join(format(ord(x), 'b')[TRUNC[n]:]
                        if x != ':' else ':' for n, x in enumerate(t_str))
    return ''.join(c.replace('1', '-').replace('0', '.') for c in t_str)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"