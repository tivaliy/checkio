__author__ = 'Vitalii K'


def checkio(result):
    array = []
    # Add rows
    array.extend(result)
    # Add columns
    for j in range(len(result)):
        m = ''
        for i in range(len(result)):
            m += result[i][j]
        array.append(m)
    # Add main diagonals
    array.append(''.join([str(result[i][i]) for i in range(len(result[0]))]))
    array.append(''.join([str(result[len(result[0])-1-i][i])
                          for i in range(len(result[0])-1, -1, -1)]))
    if 'XXX' in array:
        return 'X'
    if 'OOO' in array:
        return 'O'
    return 'D'

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
