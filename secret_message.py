# https://www.checkio.org/mission/secret-message/
__author__ = 'Vitalii K'


def find_message(text):
    return ''.join([l for l in text if l.isupper()])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
