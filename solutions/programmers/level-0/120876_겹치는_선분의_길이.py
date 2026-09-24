def solution(lines):
    dict = {}
    answer = 0

    for start, end in lines:
        for i in range(start, end):
            dict[i] = dict.get(i, 0) + 1

    for num in dict.values():
        if num >= 2:
            answer += 1
    return answer