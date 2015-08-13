# http://www.checkio.org/mission/vigenere-cipher/
__author__ = 'Vitalii K'

import itertools
import collections

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    vigenere_table = gen_vigenere_table()
    secret_key = get_key(vigenere_table, old_decrypted, old_encrypted)
    return decrypt(vigenere_table, secret_key, new_encrypted)


# Generate Vigenère square
def gen_vigenere_table():
    l = collections.deque(list(ALPHABET))
    vigenere_dict = {}
    cnt = 0
    for p in itertools.product(ALPHABET, repeat=2):
        vigenere_dict[''.join(p)] = l[cnt]
        if cnt == len(ALPHABET) - 1:
            cnt = 0
            l.rotate(-1)
        else:
            cnt += 1
    return vigenere_dict


# Get secret key from old_decrypted and old_encrypted
def get_key(vigenere_table, old_decrypted, old_encrypted):
    key_string = ''.join([''.join([k[1] for k, v in vigenere_table.items()
                                   if i[0] == k[0] and i[1] == v])
                          for i in zip(old_decrypted, old_encrypted)])
    for i in range(1, len(key_string) + 1):
        sub_keys = [key_string[j:j + i] for j in range(0, len(key_string), i)]
        if len(sub_keys) == 1:
            return sub_keys[0]
        elif (len(list(map(list, set(map(tuple, sub_keys[:-1]))))) == 1
              and sub_keys[-1] == sub_keys[0][:len(sub_keys[-1])]):
            return sub_keys[0]


# Decrypt Vigenère cipher
def decrypt(vigenere_table, secret_key, encrypted):
    length = len(encrypted) // len(secret_key) + 1
    return ''.join([''.join([k[0] for k, v in vigenere_table.items()
                             if i[0] == k[1] and i[1] == v])
                    for i in zip(secret_key * length, encrypted)])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
