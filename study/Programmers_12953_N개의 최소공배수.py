# N개의 최소공배수

# 최대공약수
# math 함수 gcd 사용도 가능함
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소 공약수
def lcm(a, b):
    return a * b // gcd(a, b)


def solution(arr):
    answer = arr[0]  # 시작점
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer