import math

def solution(a, b):
    answer = 0
    b //= math.gcd(a, b)  # 기약 분수 (최대공약수로 분모 나누기)

    # 분모의 소인수 중 2, 5 제거 -> 1이 되면 유한소수
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    if b == 1:
        return 1
    else:
        return 2

    return answer