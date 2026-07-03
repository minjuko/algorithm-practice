# 게시판 관리자

n = int(input())
first = list(input().split())
second = list(input().split())

cnt = 0
for i in range(n):
    if first[i] != second[i]:
        cnt += 1

if cnt == 3:
    print(3)
elif cnt == 2:
    print(0)
else:
    print(2)