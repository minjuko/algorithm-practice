# 두 정수 사이의 합

# a, b 사이 모든 정수의 합 구하기

def solution(a, b):
    answer = 0
    if a >= b:
        start = b
        end = a
    else:
        start = a
        end = b
    for i in range(start, end+1):
        answer += i
    return answer

# 다른 풀이
# return sum(range(a, b + 1)) (대소 관계 정한 후)
