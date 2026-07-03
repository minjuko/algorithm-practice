# 쌍둥이의 대결

def get_score(n, nums, m):
    score = [0] * (int(n*(n+1)/2)+1)
    idx = 0

    for i in range(n):
        for j in range(i, n):
            idx += 1
            if j == i:
                score[idx] = nums[j] % m
            else:
                score[idx] = (score[idx-1] * nums[j]) % m
    score = sorted(score, reverse=True)
    return score

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

score = get_score(n, nums, m)
result = 0
for i in range(len(score)):
    if i % 2 == 0:
        result += score[i]
    else:
        result -= score[i]
print(result % m)