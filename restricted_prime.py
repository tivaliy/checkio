# http://www.checkio.org/mission/restricted-prime/
__author__ = 'Vitalii K'


def checkio(number):
    i = ord(' ') ^ ord('"')
    while i < number:
        curr_number = number
        while curr_number >= (ord('a')) ^ (ord('a')):
            i_neg = ~i + (ord(' ') ^ ord('!'))
            curr_number += i_neg
            if curr_number == (ord('a')) ^ (ord('a')):
                return False
        i += ord(' ') ^ ord('!')
    return True



