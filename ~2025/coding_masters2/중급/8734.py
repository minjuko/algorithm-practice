# 가게입점

l, r = map(int, input().split())
cnt = 0

for i in range(l, r+1):
    cnt += max(0, min(r, i-l)-max(l, i-r)+1)

print(cnt)