# 순환 순열

MOD = 1000000007

def calc(base, exp):
    result = 1
    while exp:
        if exp % 2:
            result = (result * base) % MOD
        base = (base * base) % MOD
        exp //= 2
    return result

n = int(input())
if n == 1:
    print(0)
else:
    fact = 1
    for i in range(2, n+1):
        fact = (fact * i) % MOD
    result = (fact - calc(2, n-1) + MOD) % MOD
    print(result)

