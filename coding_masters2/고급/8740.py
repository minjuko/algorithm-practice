# 곰팡이

n = int(input())
MOD = 1000000007

def mul_matrix(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

if n == 0:
    print(1)
    exit()
elif n == 1:
    print(1)
    exit()

fact = [[1, 1], [1, 0]]
result = [[1, 0], [0, 1]]
base = fact

while n > 0:
    if n % 2 == 1:
        result = mul_matrix(result, base)
    base = mul_matrix(base, base)
    n //= 2

print(result[0][0])

