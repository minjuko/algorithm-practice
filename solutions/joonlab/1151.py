# k진수 정수 뒤집기

n, k = map(int, input().split())
# n을 k진수로 변환한 수 a
# a를 뒤집은 수 b
# k진수 b를 10진수로 출력하기
# 맨 앞 0은 제거

def solution(n, k):
    b = 0
    while n > 0:
        d = n % k  # 가장 낮은 자릿수 (k진수)
        n = n // k  # d 제거
        b = b * k + d
    return b

print(solution(n, k))


