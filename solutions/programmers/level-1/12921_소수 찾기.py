def solution(n):
    # 에라토스테네스의 체
    # n의 제곱근 이하의 수까지만 배수를 지우면 n 이하의 모든 소수 판별 가능 (약수의 대칭성)
    num = set(range(2, n+1))

    for i in range(2, int(n ** 0.5) + 1):
        if i in num:
            # i 배수들을 집합에서 제거 (i 제외)
            num -= set(range(i * 2, n + 1, i))

    return len(num)