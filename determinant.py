#!/usr/bin/env python
# -*- coding:utf8 -*-


def minor(x, i, j):
    y = x[:]
    del (y[i - 1])
    y = list(zip(*y))
    del (y[j - 1])
    return list(zip(*y))


def checkio(data):
    if len(data) == 1:
        return data[0][0]
    return sum([(-1) ** i * data[i][0] * checkio(minor(data, i + 1, 1))
                for i in range(len(data))])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[4, 3], [6, 3]]) == -6, 'First example'

    assert checkio([[1, 3, 2],
                    [1, 1, 4],
                    [2, 2, 1]]) == 14, 'Second example'
