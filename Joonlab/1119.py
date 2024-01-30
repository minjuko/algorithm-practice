# 피보나치 수를 재귀로

n = int(input())

# n번째 피보나치 수 출력
# 피보나치 F(n) = F(n-1) + F(n-2) (n>=3)
# F(1) = 1, F(2) = 1

def solution(n):
    if n == 1 or n == 2:
        return 1
    return solution(n-1) + solution(n-2)

print(solution(n))
