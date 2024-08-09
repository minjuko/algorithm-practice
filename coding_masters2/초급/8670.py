# 전투력

# 전투력의 합 최대
# 가장 전투력 높은 용벙부터 팀에 넣기
# 전투력이 동화 -> 여러 명 있을 때 가장 낮은 전투력의 용벙과 동일하게 나머지 조정

n = int(input()) # 용병 수
power = list(map(int, input().split())) # 전투력
power.sort(reverse = True) # 내림차순 정렬

answer = []
for i in range(n):
    answer.append(power[i] * (i + 1))

print(max(answer)) # 최대  출력
