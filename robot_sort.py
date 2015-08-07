# http://www.checkio.org/mission/robot-sort/
__author__ = 'Vitalii K'


def swapsort(array):
    result = ''
    array = list(array)
    for p_left in range(len(array)-1, 0, -1):
        for index in range(p_left):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                result += str(index) + str(index + 1) + ','
    return result[:-1]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_solution(f, indata):
        result = f(indata)
        array = list(indata[:])
        la = len(array)
        if not isinstance(result, str):
            print("The result should be a string")
            return False
        actions = result.split(",") if result else []
        for act in actions:
            if len(act) != 2 or not act.isdigit():
                print("The wrong action: {}".format(act))
                return False
            i, j = int(act[0]), int(act[1])
            if i >= la or j >= la:
                print("Index error: {}".format(act))
                return False
            if abs(i - j) != 1:
                print("The wrong action: {}".format(act))
                return False
            array[i], array[j] = array[j], array[i]
        if len(actions) > (la * (la - 1)) // 2:
            print("Too many actions. BOOM!")
            return False
        if array != sorted(indata):
            print("The array is not sorted. BOOM!")
            return False
        return True


    assert check_solution(swapsort, (6, 4, 2)), "Reverse simple"
    assert check_solution(swapsort, (1, 2, 3, 4, 5)), "All right!"
    assert check_solution(swapsort, (1, 2, 3, 5, 3)), "One move"
