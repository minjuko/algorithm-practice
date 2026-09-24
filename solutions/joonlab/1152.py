# k진수 정수의 자릿수 합

n, k = map(int, input().split())

def solution(n, k):
    a = 0
    # 각 자릿수 합 저장
    while n > 0:
        d = n % k
        n = n // k
        a += d

    # a를 k진수로 변환한 수 b
    b = ''
    while a > 0:
        d = a % k
        a = a // k
        b = str(d) + b
    return int(b)

print(solution(n, k))
