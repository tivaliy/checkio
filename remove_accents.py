# http://www.checkio.org/mission/remove-accents/
__author__ = 'Vitalii K'


import unicodedata


def checkio(in_string):
    return ''.join(c for c in unicodedata.normalize('NFD', in_string)
                   if unicodedata.category(c) != 'Mn')

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"