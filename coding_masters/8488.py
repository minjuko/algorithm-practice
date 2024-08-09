# 소수 구하기

# n 이하의 소수 개수 구하기

n = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

answer = 0
for i in range(2, n + 1):
    if is_prime(i):
        answer += 1

print(answer)