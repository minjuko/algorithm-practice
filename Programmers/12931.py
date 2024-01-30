# 자릿수 더하기

# n의 각 자릿수의 합 구하기

def solution(n):
    answer = 0
    while n>0:
        answer += n % 10 # 10으로 나눈 나머지 (낮은 자릿수)
        n = n // 10
    return answer