# https://www.checkio.org/mission/letter-queue/
__author__ = 'Vitalii K'

from collections import deque


def letter_queue(commands):
    fifo = deque([])
    for command in commands:
        if 'PUSH' in command:
            fifo.append(command.split(' ')[1])
        elif fifo:
            fifo.popleft()
    return ''.join(fifo)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"