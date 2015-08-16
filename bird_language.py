# http://www.checkio.org/mission/bird-language/
__author__ = 'Vitalii K'


VOWELS = "aeiouy"


def translate(phrase):
    string = ''
    for word in phrase.split():
        index = 0
        while index != len(word):
            string += word[index]
            if word[index] not in VOWELS:
                index += 2
            else:
                index += 3
        string += ' '
    return string.strip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
