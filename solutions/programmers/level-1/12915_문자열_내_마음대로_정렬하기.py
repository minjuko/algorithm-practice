def solution(strings, n):
    #정렬 기준 : n번째 글자 -> 사전순 (x[n], x)
    return sorted(strings, key=lambda x: (x[n], x))