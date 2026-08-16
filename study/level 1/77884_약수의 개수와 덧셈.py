def count_divisor(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return len(divisors)


def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        if count_divisor(i) % 2 == 0:
            result += i
        else:
            result -= i
    return result