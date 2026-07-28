def solution(my_string, m, c):
    # c번째열 문자부터 m칸씩 이동
    return my_string[c-1::m]