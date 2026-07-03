# 숫자의 표현

# n을 연속된 자연수로 표현하는 방법의 수

def solution(n):
    answer = 0
    for i in range(1, n+1): # 1부터 최대 n까지
        sum = 0
        while sum < n: # 합이 n보다 작으면
            sum += i # 합산
            i += 1
        if sum == n:
            answer += 1
    return answer