import re

__author__ = 'Vitalii K'


def replace(m):
    data = m.group(1)
    if len(data) > 3:
        if data[-3] == ',' or data[-4] == '.':
            data = data.translate(str.maketrans(',.', '.,'))
    return data


def checkio(text):
    return re.sub(r'(\$[\d\.,]*\d+)', replace, text)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"
    assert checkio("$0,89") == "$0.89", "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
           "Euro Style = $12,345.67, US Style = $12,345.67", "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
           "Us Style = $12,345.67, Euro Style = $12,345.67", "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
           "$1,234, $5,678 and $9", "Dollars without cents"
