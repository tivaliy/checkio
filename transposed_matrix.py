# http://www.checkio.org/mission/matrix-transpose
__author__ = 'Vitalii K'


def checkio(data):
    # Nested list comprehension example
    # [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    return list(map(lambda *row: list(row), *data))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert isinstance(checkio([[0]]).pop(), list) is True, "Match types"
    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"