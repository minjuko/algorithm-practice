# 멀리 뛰기

# 한 번에 1칸 또는 2칸

# n칸을 뛰는 방법의 수를 1234567로 나눈 나머지 반환
# 피보나치 이용

def solution(n):
    dp = [0] * (n+1) # n칸을 뛰는 방법 저장
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[n-1] % 1234567
    return answer
