import re


def map_point(value):
    return sum((lambda x: [int(j) for j in str(x*2)])(value))


def checkio(data):
    data = re.sub(r'[^A-Z0-9]+', '', data)
    data = list(map(lambda x: ord(x) - 48, reversed(data)))
    r = sum([data[i] if i % 2 != 0 else map_point(data[i])
             for i in range(len(data))])
    return [str(-r % 10), r]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")
