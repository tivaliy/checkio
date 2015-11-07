import itertools
from math import pi, sqrt, acos
from operator import itemgetter

__author__ = 'Vitalii K'

OVERLAPPED_THR = 55  # in %
AREA_RATIO_THR = 20  # in %


def get_distance(c_pair):
    (x1, y1), (x2, y2) = (c_pair[0][0], c_pair[0][1]), (
        c_pair[1][0], c_pair[1][1])
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_min_distance_pair(circle_pairs):
    return min(circle_pairs, key=get_distance)


# return True if one of the two circles is dominated over AREA_RATIO_THR area
def is_dominated(a1, a2, area_ratio_thr=20):
    return (max(a1, a2) * 100) / min(a1, a2) - 100 >= area_ratio_thr


def merge_circles(c_pair):
    r1, r2 = c_pair[0][2], c_pair[1][2]
    # Areas of c1 and c2 circles
    a1 = pi * r1 * r1
    a2 = pi * r2 * r2
    d = get_distance(c_pair)
    new_radius = sqrt((r1 ** 2 + r2 ** 2))
    # No intersection or no dominant, where x1y1 == x2y2
    if d >= r1 + r2 or d == 0 and not is_dominated(a1, a2):
        return c_pair
    # x1y1 == x2y2 and dominant existing
    elif d <= abs(r1 - r2):
        # 'eat up' small circle
        dominant_c = list(max(c_pair, key=itemgetter(2)))
        dominant_c[2] = new_radius
        return tuple(dominant_c),
    s1 = r1 * r1 * acos((d * d + r1 * r1 - r2 * r2) / (2 * d * r1))
    s2 = r2 * r2 * acos((d * d + r2 * r2 - r1 * r1) / (2 * d * r2))
    a = 0.5 * sqrt((-d + r1 + r2)*(d + r1 - r2)*(d - r1 + r2)*(d + r1 + r2))
    # Total area intersection
    s = s1 + s2 - a
    # Portion
    p1 = round((s * 100) / a1)
    p2 = round((s * 100) / a2)
    if p1 < OVERLAPPED_THR and p2 < OVERLAPPED_THR:
        # No need to 'eat up', overlapped area of two circles < 55%
        return c_pair
    # Check dominated circle
    if not is_dominated(a1, a2):
        return c_pair
    # 'eat up' small circle
    dominant_c = list(max(c_pair, key=itemgetter(2)))
    dominant_c[2] = new_radius
    return tuple(dominant_c),


def checkio(data):
    c_pairs = [i for i in itertools.combinations(data, r=2)]
    while len(data) != 1 and len(c_pairs) != 0:
        min_pair = c_pairs.pop(c_pairs.index(min(c_pairs, key=get_distance)))
        result = merge_circles(min_pair)
        if len(result) == 1:
            data.remove(min(min_pair, key=itemgetter(2)))
            data[data.index(max(min_pair, key=itemgetter(2)))] = result[0]
            c_pairs = [i for i in itertools.combinations(data, r=2)]
    # Added to round up final result
    data = [(x, y, round(r, 2)) for x, y, r in data]
    return data


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
    assert checkio([(0, 0, 2), (-1, 0, 2)]) == [(0, 0, 2), (-1, 0, 2)]
    assert checkio([(4, 3, 2), (2.5, 3.5, 1.4)]) == [(4, 3, 2.44)]
    assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]
