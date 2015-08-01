# http://www.checkio.org/mission/mono-captcha
__author__ = 'Vitalii K'

import math

FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")
S_LEN = 3
S_NUM = 10
FONT_SHIFT = 41


def checkio(image):
    # Parse image to get font characters
    s_l = []
    step = 0
    k = 1
    for i in range(math.ceil(len(image[0]) / 4 - 1)):
        s = []
        for j in range(len(image)):
            s.append(''.join(map(str, image[j][k + step:S_LEN + k + step])))
        step += S_LEN
        k += 1
        s_l.append(''.join([i.replace('0', '-').replace('1', 'X') for i in s]))
    # Parse FONT to get decimal values for each character
    shift = 0
    f_l = []
    l_offset = 0
    for i in range(S_NUM):
        f = []
        for j in range(len(image)):
            f.append(FONT[1 + shift + l_offset: shift + S_LEN + 1 + l_offset])
            shift += FONT_SHIFT
        shift = 0
        l_offset += 4
        f_l.append(''.join(i for i in f))
    # Create dictionary {'character': 'decimal_value'}
    d = {f_l[-1]: '0'}
    for i, c_val in enumerate(f_l[:-1]):
        d.update({c_val: str(i + 1)})
    # Recognize character
    d_val = ''
    for v in s_l:
        for key in d:
            # Generate list with differences
            if len([i for i in range(len(v)) if v[i] != key[i]]) <= 1:
                d_val += d.get(key)
                break
    return int(d_val)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1,
                     0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1,
                     0]]) == 394, "again 394 but with noise"
