# http://www.checkio.org/mission/counting-tiles/
__author__ = 'Vitalii K'


from math import floor, sqrt, ceil


def checkio(radius):
    solid, partial = 0, 0
    up_border, down_border = radius, radius
    # We will use well-known Gauss's Circle Problem
    for i in range(1, floor(radius) + 1):
        down_border = sqrt(radius**2-i**2)
        solid += floor(down_border)
        partial += floor(ceil(up_border))-floor(down_border)
        up_border = down_border
    # Up round if radius is float
    if floor(radius) != radius:
        partial += floor(ceil(down_border))
    return [4*solid, 4*partial]

print(checkio(2.5))

# These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio(2) == [4, 12], "N=2"
#     assert checkio(3) == [16, 20], "N=3"
#     assert checkio(2.1) == [4, 20], "N=2.1"
#     assert checkio(2.5) == [12, 20], "N=2.5"
