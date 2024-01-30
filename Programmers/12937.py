# 짝수와 홀수

def solution(num):
    answer = ''
    if num % 2 == 0: # 짝수
        answer = "Even"
    else:
        answer = "Odd"
    return answer