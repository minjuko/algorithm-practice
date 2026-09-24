def solution(my_string):
    answer = ''
    for str in my_string:
        if str.isupper(): # 대문자
            answer += str.lower()
        else: # 소문자
            answer += str.upper()
    return answer