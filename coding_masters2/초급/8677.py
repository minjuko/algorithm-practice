# 볼펜 숫자의 곱

n = int(input())
pens = list(map(int, input().split()))
answer2 = []
answer3 = []

for i in range(n):
    for j in range(i+1, n):
        tmp = pens[i] * pens[j]
        answer2.append(tmp)

        for k in range(j+1, n):
            tmp2 = tmp * pens[k]
            answer3.append(tmp2)
if max(answer3) > max(answer2):
    print(max(answer3))
else:
    print(max(answer2))