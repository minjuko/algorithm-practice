# 삼각형 만들기

n = int(input())
a = list(map(int, input().split()))
a.sort()
answer = 3

for i in range(n-2):
    cnt = 2
    x, y = a[i], a[i+1]
    for j in range(i+2, n):
        if x + y > a[j]:
            cnt += 1
        else:
            break
    answer = max(answer, cnt)

print(answer)