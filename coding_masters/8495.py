# 누적 합

n = int(input())
k = list(map(int, input().split()))

if n == 1:
    print(k[0])
    exit()

k += [0] * (2**(len(format(n, 'b')))-n)
answer = [k]

while True:
    tmp = []
    for i in range(0, len(k), 2):
        tmp.append(k[i] + k[i + 1])
    k = tmp
    n = len(k)
    answer.append(k)
    if n == 1:
        break

for i in range(len(answer)-1, -1, -1):
    print(*answer[i])

