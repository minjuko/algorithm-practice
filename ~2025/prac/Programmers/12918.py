# 문자열 다루기 기본

# 문자열 길이가 4 또는 6 + 숫자로 구성인지 판단

def solution(s):
    answer = False

    # 길이 확인
    if len(s) == 4 or len(s) == 6:
        # 숫자 확인
        if s.isdigit():
            answer = True
    return answer