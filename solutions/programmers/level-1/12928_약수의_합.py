def solution(n):
    # 제곱근 활용하여 약수 구하기
    if n == 0: return 0

    divisors = set()  # 중복 및 제곱 수 처리 ex. 4*4
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors)