# 정수 합을 재귀로
import sys
sys.setrecursionlimit(1000000) # 재귀 제한을 늘려줌 보통 10**6
n = int(input())

# 1부터 n까지 정수 합을 재귀 함수로 출력

def solution(n):
    # n=1인 경우
    if n == 1:
        return 1
    return n + solution(n-1) # 재귀로 계쏙 더해줌

print(solution(n))