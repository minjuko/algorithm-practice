def solution(my_string):
    answer = []
    # isdigit() : 숫자 확인
    # isalpha() : 문자 확인
    # isalnum() : 문자 또는 숫자인지 확인
    # isspace() : 공백인지 확인
    for str in my_string:
        if str.isdigit():
            answer.append(int(str))
    answer.sort()
    return answer