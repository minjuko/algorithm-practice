# Trailing Zero - 1

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

p, n = map(int, input().split())
fac_n = factorial(n)
answer = 0

while fac_n % p == 0:
    answer += 1
    fac_n //= p

print(answer)