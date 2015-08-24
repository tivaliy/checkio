# http://www.checkio.org/mission/pawn-brotherhood/
__author__ = 'Vitalii K'


def safe_pawns(pawns):
    safe_pawns_cnt = 0
    for coord in pawns:
        first_check = (chr(ord(coord[0]) - 1) + str((int(coord[1]) - 1)))
        second_check = (chr(ord(coord[0]) + 1) + str((int(coord[1]) - 1)))
        if first_check in pawns or second_check in pawns:
            safe_pawns_cnt += 1
    return safe_pawns_cnt


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
