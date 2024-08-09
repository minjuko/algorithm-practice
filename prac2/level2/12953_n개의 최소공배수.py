# N개의 최소공배수

# 최대공약수
# math 함수 gcd 사용도 가능함
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)


# 최소 공배수 구하기
def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer
