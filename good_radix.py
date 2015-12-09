__author__ = 'Vitalii K'

K_MAX = 37


def checkio(number):
    for k in range(1, K_MAX):
        try:
            if int(number, k) % (k - 1) == 0:
                return k
        except ValueError:
            pass
    return 0

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    assert checkio("IDDQD") == 0, "k is not exist"
    print('Local tests done')
