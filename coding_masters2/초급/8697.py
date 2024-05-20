# 유사 소수 분할

n = int(input())

is_prime = [True] * (n + 1)
primes = []
result = set()

for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        tmp = primes[i] * primes[j]
        if tmp > n:
            break
        result.add(tmp)

for x in range(1, n-2):
    for y in range(x+1, n-1):
        for z in range(y+1, n):
            if (n-x-y-z) > z:
                tmp2 = sum([x in result, y in result, z in result, (n-x-y-z) in result])
                if tmp2 > 2:
                    print("possible")
                    exit()
print("impossible")