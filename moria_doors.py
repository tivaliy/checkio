# http://www.checkio.org/mission/gate-puzzles/
__author__ = 'Vitalii K'


import string


def find_word(message):
    # Remove extra symbols
    s = ''.join([x.lower() for x in message if x in string.ascii_letters + ' '])
    # Store "comparison matrix" column result (median value)
    result = []
    # Iterate over all possible words pairs
    for i, word1 in enumerate(s.split()):
        # Store single word pair comparison result
        values = []
        for j, word2 in enumerate(s.split()):
            curr_val = 0
            # Zero diagonal in "comparison matrix"
            if i != j:
                if word1 == word2:
                    curr_val = 1
                else:
                    if word1[0] == word2[0]:
                        curr_val += 0.1
                    if word1[-1] == word2[-1]:
                        curr_val += 0.1
                    if len(word1) <= len(word2):
                        curr_val += (len(word1) / len(word2)) * 0.3
                    else:
                        curr_val += (len(word2) / len(word1)) * 0.3
                    # Find common and unique letters in pair of word
                    common_letters_num = len(set(word1) & set(word2))
                    unique_letters_num = len(set(word1) | set(word2))
                    curr_val += (common_letters_num / unique_letters_num) * 0.5
            values.append(round(curr_val * 100, 3))
        result.append(sum(values) / (len(values) - 1))
    # Find max value from result
    max_val = max(result)
    # Find all indices, that store max value
    indices = [i for i, v in enumerate(result) if v == max_val]
    # Return word on the same right max value index position
    return s.split(' ')[indices[-1]]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"