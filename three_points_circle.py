__author__ = 'Vitalii K'

from math import sqrt


def checkio(data):
    val = [int(i) for i in data if i.isdigit()]
    x1, y1, x2, y2, x3, y3 = val
    # mid sides
    x4 = (x1 + x2) / 2
    y4 = (y1 + y2) / 2
    x5 = (x1 + x3) / 2
    y5 = (y1 + y3) / 2
    # Coefficients of two lines perpendicular to the sides passing through their middle
    a1 = x2 - x1
    b1 = y2 - y1
    c1 = x4 * (x2 - x1) + y4 * (y2 - y1)
    a2 = x3 - x1
    b2 = y3 - y1
    c2 = x5 * (x3 - x1) + y5 * (y3 - y1)
    # Coordinates of the center == point of the intersection of the lines
    x0 = round((c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1), 3)
    y0 = round((a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1), 3)
    r = str(round(sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2), 2))
    r = r.strip('.0') if r[-2:] == '.0' else r
    x0 = str(round(x0, 2)).strip('.0')
    y0 = str(round(y0, 2)).strip('.0')
    return '(x-' + x0 + ')^2+(y-' + y0 + ')^2=' + r + '^2'


print(checkio("(7,3),(9,6),(3,6)"))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
