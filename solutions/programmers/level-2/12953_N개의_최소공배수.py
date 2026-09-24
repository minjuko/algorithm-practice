# N개의 최소공배수

# n개의 수의 최소공배수 구하기
import math
# 최소 공배수
def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    answer = arr[0] # 첫번째 수부터 시작
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer
