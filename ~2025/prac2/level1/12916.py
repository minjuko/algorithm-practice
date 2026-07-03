# 문자열 내 p와 y의 개수
# 개수가 같으면 True
def solution(s):
    s = s.lower()  # 대소문자 구별 X
    if s.count('p') == s.count('y'):
        answer = True
    else:
        answer = False

    return answer