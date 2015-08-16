# http://www.checkio.org/mission/three-words/
__author__ = 'Vitalii K'


def checkio(words):
    words_list = ''.join(['1' if w.isalpha() else '0' for w in words.split()])
    return True if '111' in words_list else False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"