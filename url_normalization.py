#!/usr/bin/env python
# -*- coding:utf8 -*-
import re


def decode_percent_encoded(data):
    char = chr(int(data.group()[1:], 16))
    res = re.findall('[._a-zA-Z0-9~-]', char)
    return data.group() if not res else res[0].lower()


def checkio(url):
    url = url.lower()
    url = re.sub(r':80$', '', url)          # ':80'   --> ''
    url = re.sub(r':80\/', '/', url)        # ':80/'  --> '/'
    url = re.sub(r'\/(\.\/)+', '/', url)    # '/./././' --> '/'
    url = re.sub(r'%[\w].', lambda pat: pat.group().upper(), url)
    url = re.sub(r'%[\w].', decode_percent_encoded, url)
    url = re.sub(r'\/[\w]*\/(\.\.)', '', url)
    return url

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio("http://www.checkio.org/%cc%b1bac") == \
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio("http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio("http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio("http://www.checkio.org:8080/home/") == \
        "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio("http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')
