#!/usr/bin/env python
# -*- coding:utf8 -*-


def convert(numerator, denominator):
    v = numerator // denominator
    numerator = 10 * (numerator - v * denominator)
    answer = str(v) + '.'
    if numerator == 0:
        return answer
    results = {}
    while numerator > 0:
        history_state = results.get(numerator, None)
        if history_state:
            start_repeat_index = history_state
            non_repeating = answer[:start_repeat_index]
            repeating = answer[start_repeat_index:]
            return non_repeating + '(' + repeating + ')'
        results[numerator] = len(answer)
        v = numerator // denominator
        answer += str(v)
        numerator -= v * denominator
        numerator *= 10
    return answer


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
