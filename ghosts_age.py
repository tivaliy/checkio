# http://www.checkio.org/mission/ghosts-age/
__author__ = 'Vitalii K'

from math import sqrt


def checkio(opacity):
    temp_opacity = 10000
    for age in range(1, 5000):
        if opacity == temp_opacity:
            break
        elif is_fibonacci(age):
            temp_opacity -= age
        else:
            temp_opacity += 1
    return age - 1

# Recognizing Fibonacci numbers - "perfect square"
def is_fibonacci(n):
    phi = 0.5 + 0.5 * sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"




