# http://www.checkio.org/mission/cipher-map2/
__author__ = 'Vitalii K'


def get_val(pair):
    return [b for a, b in zip(*pair) if a == 'X']


def recall_password(c_grille, c_passwd):
    t = []
    # 4 clockwise rotations
    for _ in range(4):
        t.extend(([''.join(j) for j in map(get_val, zip(c_grille, c_passwd))]))
        # Rotate cipher_grille matrix
        c_grille = tuple(map(lambda *row: ''.join(row), *reversed(c_grille)))
    return ''.join(t)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

