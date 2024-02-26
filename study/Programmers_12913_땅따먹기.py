# 땅따먹기

# 내려오면서 자신의 열을 제외한 나머지 중 최댓값 더하기

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # 같은 열을 제외하여 합친 후 최댓값 원소를 찾아 합산
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    answer = max(land[len(land) - 1])  # 마지막 줄의 최댓값 출력
    return answer