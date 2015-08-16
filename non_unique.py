# http://www.checkio.org/mission/non-unique-elements/
__author__ = 'Vitalii K'

import itertools


def checkio(data):
    res = [(a, b) for (a, b) in itertools.combinations(data, r=2)
           if str(a).lower() == str(b).lower()]
    res_set = set([i[j] for i in res for j in range(len(i))])
    return [x for x in data if x in res_set]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"

assert checkio(['P', 7, 'j', 'A', 'P', 'N', 'Z', 'i',
                'A', 'X', 'j', 'L', 'y', 's', 'K', 'g',
                'p', 'r', 7, 'b']) == ['P', 7, 'j', 'A', 'P', 'A', 'j', 'p',
                                       7], "Letters"
