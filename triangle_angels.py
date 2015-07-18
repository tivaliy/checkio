# http://www.checkio.org/mission/triangle-angles/solve/
__author__ = 'Vitalii K'


from math import acos, degrees


def checkio(a, b, c):
    # Check degenerated triangle
    if a+b <= c or b+c <= a or a+c <= b:
        return [0, 0, 0]
    # Law of cosines
    alpha = round(degrees(acos((b**2 + c**2 - a**2) / (2*b*c))))
    betta = round(degrees(acos((a**2 + c**2 - b**2) / (2*a*c))))
    gamma = round(degrees(acos((a**2 + b**2 - c**2) / (2*a*b))))
    return sorted([alpha, betta, gamma])

print(checkio(10, 20, 30))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
