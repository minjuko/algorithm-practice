# 신입사원 채용
import sys
input = sys.stdin.readline

n = int(input()) # 지원자 수
info = [list(map(int, input().split())) for _ in range(n)] # 각 지원자의 서류 점수, 면접 점수

rank = [1]*n # 등수 리스트 초기화

# 등수 정하기
# 다른 지원자들과 비교하여
# 서류 점수, 면접 점수 모두 높은 경우 높은 등수 (다른 지원자 rank +=1)
# 서류 점수는 같고 면접 점수가 높은 경우 높은 등수 (다른 지원자 rank +=1)
# 서류 점수가 높고 면접 점수가 같은 경우 높은 등수 (다른 지원자 rank +=1)

for i in range(n):
    for j in range(n):
        if i != j:
            if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
                rank[i] += 1
            elif info[i][0] == info[j][0] and info[i][1] < info[j][1]:
                rank[i] += 1
            elif info[i][0] < info[j][0] and info[i][1] == info[j][1]:
                rank[i] += 1

# 같은 등수의 경우 우열을 가릴 수 있는지 검사 -> 가릴 수 없다면 같은 등수로 판정
# ex) 서류 점수는 A가 더 높고 면접 점수는 B가 더 높은 경우

for i in range(n):
    tmp = rank[i] # 현재 지원자 등수
    flag = 0 # 우열 판별 flag

    for j in range(n):
        # 다른 지원자보다 등수가 낮은 경우
        if i != j and tmp > rank[j]:
            # 우열을 가릴 수 없는 경우 flag = 1
            if info[i][0] > info[j][0] or info[i][1] > info[j][1]:
                flag = 1
                tmp = rank[j] # 현재 지원자 등수 갱신

    # 우열을 가릴 수 없는 경우 같은 등수로 재설정정
    if flag == 1:
        for j in range(n):
            if i != j and tmp < rank[j] and rank[j] <= rank[i]:
                rank[j]= tmp
        rank[i] = tmp
print(' '.join(map(str, rank)))