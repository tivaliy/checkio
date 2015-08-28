# https://www.checkio.org/mission/most-wanted-letter/
__author__ = 'Vitalii K'

from string import ascii_lowercase
from operator import itemgetter
import itertools


def checkio(text):
    # Create a list of tuples (ascii_lowercase_index, n)
    val = [(ascii_lowercase[i], v) for i, v in
           enumerate(map(lambda x: text.lower().count(x), ascii_lowercase))]
    # Remove tuples with zero n-value
    k = (filter(lambda x: x[1], sorted(val, key=itemgetter(1))))
    return ["".join(char for char, num in tuples) for num, tuples
            in itertools.groupby(k, key=lambda a: a[1])][-1][0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
