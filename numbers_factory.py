#!/usr/bin/env python
# -*- coding:utf8 -*-


def checkio(data):
    result = []
    while data > 9:
        is_found = False
        for i in range(9, 1, -1):
            if data % i == 0:
                is_found = True
                result.append(i)
                data = data // i
                break
        if not is_found:
            return 0
    result.append(data)
    return int(''.join([str(i) for i in sorted(result)]))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
