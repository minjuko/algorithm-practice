# 수 정렬하기
# n개의 수 오름차순 정렬

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)

