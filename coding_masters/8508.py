# 신입사원 채용
import sys
import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

rank = [1]*n

for i in range(n):
    for j in range(n):
        if i != j:
            if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
                rank[i] += 1
            elif info[i][0] == info[j][0] and info[i][1] < info[j][1]:
                rank[i] += 1
            elif info[i][0] < info[j][0] and info[i][1] == info[j][1]:
                rank[i] += 1

for i in range(n):
    tmp = rank[i]
    flag = 0
    for j in range(n):
        if i != j and tmp > rank[j]:
            if info[i][0] > info[j][0] or info[i][1] > info[j][1]:
                flag = 1
                tmp = rank[j]
    if flag == 1:
        for j in range(n):
            if i != j and tmp < rank[j] and rank[j] <= rank[i]:
                rank[j]= tmp
        rank[i] = tmp
print(' '.join(map(str, rank)))