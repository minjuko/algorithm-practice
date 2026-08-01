def solution(my_string, indices):
    answer = ''

    for idx, ch in enumerate(my_string):
        if idx not in indices:
            answer += ch
    return answer