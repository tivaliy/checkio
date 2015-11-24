from math import pi, atanh, sqrt, atan


def checkio(height, width):
    a, b = height / 2, width / 2
    if a > b:
        e = (1 - b ** 2 / a ** 2) ** 0.5
        s = 2 * pi * (b ** 2 + a * b * atan(e / sqrt(1 - e ** 2)) / e)
    elif a < b:
        e2 = 1 - a ** 2 / b ** 2
        e = e2 ** 0.5
        s = 2 * pi * b ** 2 * (1 + (1 - e2) / e * atanh(e))
    else:
        s = 4 * pi * a * a
    return [round(4 / 3 * pi * a * b * b, 2), round(s, 2)]

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
