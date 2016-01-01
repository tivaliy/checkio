import fractions


def divide_pie(groups):
    group_size = sum(abs(i) for i in groups)
    result = fractions.Fraction(1, 1)
    for dron in groups:
        if dron > 0:
            result -= fractions.Fraction(dron, group_size)
        else:
            result *= 1 - fractions.Fraction(abs(dron), group_size)
    return (0, 1) if result == 0 else (result.numerator, result.denominator)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
