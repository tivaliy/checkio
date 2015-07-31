# http://www.checkio.org/mission/ghost-detect/
__author__ = 'Vitalii K'


def recognize(n):
    # l = filter(None, "{0:b}".format(n).split('0'))
    l = list(filter(None, bin(n)[2:].split('0')))
    return l[1:] == l[:-1]
