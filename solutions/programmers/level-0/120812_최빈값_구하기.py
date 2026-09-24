from collections import Counter


def solution(array):
    counter = Counter(array)
    freq = counter.most_common()
    if len(freq) > 1:
        if freq[0][1] == freq[1][1]:
            return -1

    return freq[0][0]