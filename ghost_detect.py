# http://www.checkio.org/mission/ghost-detect/
__author__ = 'Vitalii K'


def recognize(n):
    # l = filter(None, "{0:b}".format(n).split('0'))
    l = list(filter(None, bin(n)[2:].split('0')))
    return l[1:] == l[:-1]


print(recognize(21))

print(recognize(1587))

print(recognize(3687))

print(recognize(1057222687))
