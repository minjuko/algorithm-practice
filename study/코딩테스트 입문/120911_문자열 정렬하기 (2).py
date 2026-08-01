def solution(my_string):
    answer = my_string.lower() # 소문자로 변환
    return "".join(sorted(answer)) # 알파벳 순 정렬