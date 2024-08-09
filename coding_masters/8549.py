# 무차별 대입 공격

n, k = map(int, input().split())
words = sorted(list(input()))
answer = ''

def dfs(answer):
    if len(answer) == k:
        print(answer)
        return
    for word in words:
        dfs(answer + word)

dfs(answer)
