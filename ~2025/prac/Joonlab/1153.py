# 소수들의 합 구하기
A = list(map(int, input().split()))

# A의 원소 중 소수들의 합

def isPrime(x):
    if x < 2:
        return False
    # 2~루트x 사이 약수가 있으면 소수가 아님
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

def solution(A):
    answer = 0
    for a in A:
        if isPrime(a):
            answer += a
    return answer

print(solution(A))