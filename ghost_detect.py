# http://www.checkio.org/mission/ghost-detect/
__author__ = 'Vitalii K'


def recognize(n):
    l = list(filter(None, "{0:b}".format(n).split('0')))
    return l[1:] == l[:-1]

