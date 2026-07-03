# 피로도

# 최소 피로도, 소모 피로도
# 유저가 탐험할 수 있는 최대 던전 수

# 던전의 가능한 순열의 결과를 구하여 탐험 가능한지 판단

from itertools import permutations

def solution(k, dungeons):
    answer = []
    case = list(permutations(dungeons))
    # 하나씩 판별
    for i in case:
        cur = k
        cnt = 0
        for j in i:
            if j[0] <= cur: # 현재 피로도가 최소 필요도를 충족하면
                # 해당 던전 탐험
                cur -= j[1]
                cnt += 1
        answer.append(cnt)
    return max(answer)