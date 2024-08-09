# 주사위

def solve(matrix, n):
    result = [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
    base = matrix
    while n:
        if n % 2:
            result = [[sum(x * y % MOD for x, y in zip(row, col)) % MOD for col in zip(*base)] for row in result]
        base = [[sum(x * y % MOD for x, y in zip(row, col)) % MOD for col in zip(*base)] for row in base]
        n //= 2
    return result

n = int(input())

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()
elif n == 3:
    print(4)
    exit()

MOD = 1000000007
matrix = [
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ]
start = [4, 2, 1, 1]
tmp = solve(matrix, n-3)
result = sum(tmp[0][i] * start[i] % MOD for i in range(4)) % MOD
print(result)