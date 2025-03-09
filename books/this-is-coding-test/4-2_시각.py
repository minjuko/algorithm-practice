# 시각
# 00시 00분 00초부터 n시 89분 59초까지 모든 시각 중 3이 포함되는 모든 경우의 수 출력

# -> 3중 반복문으로 시간, 분, 초에 3 포함 여부 체크
n = int(input())
count = 0 # 3이 포함되는 경우의 수 카운트

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 시각 안 3 포함 여부 체크
            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)