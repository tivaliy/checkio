__author__ = 'machin'


def checkio(game_result):
    game_grid = [[i for i in range(len(game_result))] for i in range(len(game_result))]
    for i, line in enumerate(game_result):
        for j, char in enumerate(line):
            game_grid[i][j] = char
    print(game_grid)
    array = []
    for j in range(len(game_grid)):
        m = ''
        k = ''
        for i in range(len(game_grid)):
            m += game_grid[i][j]
            k += game_grid[j][i]
        array.append(m)
        array.append(k)
    # Add main diagonals
    l = len(game_grid[0])
    array.append(''.join([str(game_grid[i][i]) for i in range(l)]))
    array.append(''.join([str(game_grid[l-1-i][i]) for i in range(l-1, -1, -1)]))
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
