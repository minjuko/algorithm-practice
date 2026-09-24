def solution(str_list, ex):
    answer = ''
    for c in str_list:
        if not ex in c:
            answer += c

    return answer