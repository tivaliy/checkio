# http://www.checkio.org/mission/radiation-search/solve/
__author__ = 'Vitalii K'

import itertools

# Different kinds of spare parts
SPARE_PARTS = [1, 2, 3, 4, 5]


def checkio(matrix):
    # Create list of indices (tuples) for each SPARE_PARTS
    indices = []
    for s_part in SPARE_PARTS:
        indices_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if s_part == matrix[i][j]:
                    indices_list.append((i, j))
        indices.append(indices_list)
    # Find set with max len
    result = []
    for item_list in indices:
        indices_set = set()
        # Get all possible indices pairs to compare them
        for val in itertools.combinations(item_list, 2):
            # Find neighbors, i.e. (0, 0) <--> (0, 1)
            curr_indices = val[0][0] - val[1][0], val[0][1] - val[1][1]
            if curr_indices == (-1, 0) or curr_indices == (0, -1):
                indices_set.add(frozenset(val))
        # Standard "Union Search"
        result.append(list(map(len, union(indices_set))))
    # Get max elements (cardinality) of each of the sets
    max_val = max([max(x) for x in result if x])
    # Get type of "spare part"
    s_type = [i + 1 for i, val in enumerate(result) if max_val in val].pop(0)
    return [max_val, s_type]


# "Union Search"
def union(superset):
    parent = {}

    def make_set(a):
        if a not in parent:
            parent[a] = a

    def find_set(a):
        if parent[a] == a:
            return a
        parent[a] = find_set(parent[a])
        return parent[a]

    def union_sets(a, b):
        a = find_set(a)
        b = find_set(b)
        if a != b:
            parent[a] = b

    for subset in superset:
        prev = None
        for v in subset:
            make_set(v)
            if prev:
                union_sets(prev, v)
            prev = v

    lists = {}
    for uid in parent.keys():
        pr = find_set(uid)
        if pr not in lists:
            lists[pr] = []
        lists[pr].append(uid)

    return set([frozenset(l) for l in lists.values()])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'
