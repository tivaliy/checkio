# http://www.checkio.org/mission/word-pattern/
__author__ = 'Vitalii K'


def base_n(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return (((num == 0) and '0') or
            (base_n(num // b, b).lstrip("0") + numerals[num % b]))


def check_structure(pattern, structure, pattern_level=2):
    base_n_str = base_n(pattern, pattern_level)
    bin_str = '0' * (len(structure) - len(base_n_str)) + base_n_str
    if pattern_level == 2:
        bin_command = ''.join(['1' if x.isalpha() else '0' for x in structure])
    elif pattern_level == 3:
        bin_command = ''.join(
            ['1' if x.islower() else '2' if x.isupper() else
             '0' for x in structure])
    else:
        bin_command = ''.join(['1' if x.islower() else '2' if x.isupper() else
                               '3' if x.isspace() else '0' for x in structure])
    return bin_str == bin_command


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert check_structure(42, "12a0b3e4"), "42 is the answer"
    assert not check_structure(101, "ab23b4zz"), "one hundred plus one"
    assert check_structure(0, "478103487120470129"), "Any number"
    assert check_structure(127, "Checkio"), "Uppercase"
    assert not check_structure(7, "Hello"), "Only full match"
    assert not check_structure(8, "a"), "Too short command"
    assert check_structure(5, "H2O"), "Water"
    assert not check_structure(42, "C2H5OH"), "Yep, this is not the Answer"

    # Rank 2
    assert check_structure(1823, 'CheckiO', 3), "up and down"
    assert not check_structure(1826, 'CheckiO', 3), "wrong up and down"
    assert check_structure(66431, '9z1b2c4d6a7Z', 3), "Various"

    # Rank 3
    assert not check_structure(39294315, 'Kill Them ALL', 4), "Don't kill"
    assert not check_structure(29, 'aXz', 4), "A Z"
    assert check_structure(39294442, 'Feed Them ALL', 4), "Feed them"
    assert check_structure(2385166685525, 'C3PO and 300 spartans', 4), "C3PO"
