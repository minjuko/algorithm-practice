# 조삼모사

n = int(input()) # 원숭이 수
arr = list(map(int, input().split())) # 원숭이 요청 도토리량
m = int(input()) # 병규가 줄 수 있는 도토리 총량

def req(mid):
    sum = 0
    for i in arr:
        sum += min(i, mid)
    return sum

start, end = 0, max(arr)
answer = 0

while start <= end:
    mid = (start + end) // 2
    if req(mid) <= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)