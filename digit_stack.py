# http://www.checkio.org/mission/digit-stack
__author__ = 'Vitalii K'


def digit_stack(commands):
    summary, stack = 0, []
    for c in commands:
        if 'PUSH' in c:
            stack.append(int(c.split()[1]))
        elif 'POP' in c:
            summary += stack.pop() if stack else 0
        else:
            summary += stack[-1] if stack else 0
    return summary

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"