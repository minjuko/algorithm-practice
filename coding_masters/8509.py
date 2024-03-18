n, k = map(int, input().split())
scores = list(map(int, input().split()))

answer = []
tmp = -1

for i in range(n):
    cnt = 0
    tmp = scores[i]

    for j in range(n):
        if (j == 0 and scores[j] >= tmp) or (j == 0 and scores[j + 1] >= tmp):
            cnt+=1
        elif (j == n - 1 and scores[j] >= tmp) or (j == n - 1 and scores[j - 1] >= tmp):
            cnt+=1
        elif 1<=j<n-1 and ((scores[j] >= tmp) or (scores[j - 1] >= tmp or scores[j + 1] >= tmp)):
            cnt+=1
    if cnt<=k:
        answer.append([tmp, cnt])

if not answer:
    print(min(scores) - 1)

else:
    answer.sort(key= lambda x:(-x[1], -x[0]))
    print(answer[0][0])