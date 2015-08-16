# https://www.checkio.org/mission/digits-multiplication/
__author__ = 'Vitalii K'

from functools import reduce


def checkio(n):
    return reduce(lambda x, y: x*y, [int(i.replace('0', '1')) for i in str(n)])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1