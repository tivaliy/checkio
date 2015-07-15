__author__ = 'Vitalii K'


def checkio(pattern, image):
    # Use to count the number of "matching rows" of pattern and image
    cnt_match = 0
    # Horizontal and vertical offset calculation
    h_cnt = len(image) - len(pattern)
    v_cnt = len(image[0]) - len(pattern[0])
    # Shift pattern through the image ()
    for offset_x in range(h_cnt + 1):
        for offset_y in range(v_cnt + 1):
            # Pattern and image compare LOOP
            for i in range(len(pattern)):
                for j in range(len(pattern[0])):
                    # Uncomment to debug
                    # print('Current index to compare = ', i + offset_x, j + offset_y)
                    # print('Comparable values: ', pattern[i][j], image[i + offset_x][j + offset_y])
                    # If some value of the pattern and image is not equal then shift pattern
                    if pattern[i][j] != image[i + offset_x][j + offset_y]:
                        break
                else:
                    cnt_match += 1
                    # If all rows of the pattern equal to respective rows of the image then make replacement
                    if cnt_match == len(pattern):
                        for n in range(len(pattern)):
                            for m in range(len(pattern[0])):
                                image[n + offset_x][m + offset_y] = 2 if image[n + offset_x][m + offset_y] == 0 \
                                    else 3
                        cnt_match = 0
                    continue
                cnt_match = 0
                break
    # Uncomment to see the output image result
    # for item in image:
    #     print(', '.join(map(str, item[:])))
    return image


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 0], [1, 1]],
                   [[0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                          [0, 3, 3, 0, 0],
                                          [3, 2, 1, 3, 2],
                                          [3, 3, 0, 3, 3],
                                          [0, 1, 1, 0, 0]]
    assert checkio([[1, 1], [1, 1]],
                   [[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]]) == [[3, 3, 1],
                                    [3, 3, 1],
                                    [1, 1, 1]]
    assert checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                         [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                         [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                         [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                         [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                         [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                         [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
