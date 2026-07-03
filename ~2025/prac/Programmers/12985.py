# 예상 대진표

# num번 참가자의 다음 라운드 번호는 num - num // 2
def solution(n,a,b):
    answer = 0
    while a != b:
        a -= a // 2
        b -= b // 2
        answer += 1
    return answer