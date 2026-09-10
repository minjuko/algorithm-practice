def solution(n, m):
    # 1. [GCD] 최대공약수 구하기 (유클리드 호제법)
    a, b = n, m
    while b > 0:
        a, b = b, a % b
    gcd = a

    # 2. [LCM] 최소공배수 구하기
    lcm = (n * m) // gcd

    return [gcd, lcm]

    # math 라이브러리 함수
    # gcd = math.gcd(n, m) : 최대공약수
    # lcm = math.lcm(n, m) : 최소공배수 [python 3.9 이상 지원]