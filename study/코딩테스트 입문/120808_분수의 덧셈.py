import math

def solution(numer1, denom1, numer2, denom2):
    a = (numer1 * denom2) + (numer2 * denom1)  # 분자
    b = denom1 * denom2  # 분모

    # 기약분수 만들기
    answer = [a // (math.gcd(a, b)), b // (math.gcd(a, b))]
    return answer