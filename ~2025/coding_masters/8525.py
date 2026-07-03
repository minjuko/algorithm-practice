# 타격왕 정우성

# 타석에 나가기만 하면 안타
# 타석에 최대 1000000000번 나갈 수 있음
# 앞으로 타석에 몇 번 나가야 타율이 오르는 지 구하기
# 타율 단위 할, 푼까지
# 0.325 -> 3할 2푼

x, y = map(int, input().split()) # 타석 횟수, 안타 횟수
k = 1000000000
avg_target = int((y/x)*100) / 100
addition = int(((y+k)/(x+k))*100) / 100

if avg_target >= addition or x == y:
    print(-1)
else:
    answer = k
    start, end = 1, k

    while start <= end:
        mid = (start + end) // 2
        if int(((y+mid)/(x+mid))*100) / 100 > avg_target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)
