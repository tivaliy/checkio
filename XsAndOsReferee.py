__author__ = 'Vitalii K'


def checkio(result):
    # Create matrix of characters
    grid = [[i for i in range(len(result))] for i in range(len(result))]
    for i, line in enumerate(result):
        for j, char in enumerate(line):
            grid[i][j] = char
    array = []
    # Get all columns and rows from grid_matrix
    for j in range(len(grid)):
        m = ''
        k = ''
        for i in range(len(grid)):
            m += grid[i][j]
            k += grid[j][i]
        array.append(m)
        array.append(k)
    # Add main diagonals
    l = len(grid[0])
    array.append(''.join([str(grid[i][i]) for i in range(l)]))
    array.append(''.join([str(grid[l-1-i][i]) for i in range(l-1, -1, -1)]))
    for index in array:
        if index == 'XXX':
            return 'X'
        elif index == 'OOO':
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
