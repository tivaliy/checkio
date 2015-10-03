import itertools

__author__ = 'Vitalii K'


class Friends:
    def __init__(self, connections):
        lst = []
        for i in connections:
            if i not in lst:
                lst.append(i)
        self.connections = lst

    def add(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)
            return True
        return False

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        return False

    def names(self):
        return set(itertools.chain(*self.connections))

    def connected(self, name):
        new_set = set()
        for item in self.connections:
            if name in item:
                new_set.update({i for i in item if i is not name})
        return new_set


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
