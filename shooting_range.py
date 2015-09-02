# http://www.checkio.org/mission/shoot-range/solve/
from math import sqrt

__author__ = 'Vitalii K'


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def shot(wall1, wall2, shot_point, later_point):
    x1, y1, x2, y2, x3, y3, x4, y4 = wall1 + wall2 + shot_point + later_point
    x_diff = (x1 - x2, x3 - x4)
    y_diff = (y1 - y2, y3 - y4)
    # Center of the wall
    c1, c2 = (x1 + x2) / 2, (y1 + y2) / 2
    # Shot vector + Target vector
    s1, s2, t1, t2 = x4 - x3, y4 - y3, c2 - x3, c1 - y3
    # Check if shot is on target
    if s1 * t1 + s2 * t2 <= 0:
        return -1
    div = det(x_diff, y_diff)
    if div == 0:
        return -1
    d = (det(wall1, wall2), det(shot_point, later_point))
    x = det(d, x_diff) / div
    y = det(d, y_diff) / div
    wall_length = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / 2
    shot_distance = sqrt((x - c1) ** 2 + (y - c2) ** 2)
    result = round(((wall_length - shot_distance) * 100) / wall_length)
    return result if result >= 0 else -1

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
