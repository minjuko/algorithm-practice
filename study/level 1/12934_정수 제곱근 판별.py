def solution(n):
    # n의 제곱근이 양의 정수인지 확인
    if (n ** 0.5) % 1 == 0:
        return int(n ** 0.5 + 1)**2
    else:
        return -1ㅎ