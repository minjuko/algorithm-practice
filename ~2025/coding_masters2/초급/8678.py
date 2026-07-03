# 소수 판별

a = int(input())

# 소수 판별
def is_prime(n):

    # 1은 소수 X
    if n < 2:
        return False

    # 2부터 n의 제곱근까지 나누어 떨어지는 수가 있는지 확인
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 소수 판별 결과 출력
if is_prime(a):
    print(1)
else:
    print(0)