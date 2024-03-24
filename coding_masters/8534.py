# 자리 바꾸기

# nx2 형태의 교실에 2n명 학생 앉히기
# i번째 행에 앉은 두학생의 관계가 좋으면 +1, 보통이면 0, 나쁘면 -1 분위기 점수에 추가 (초기값은 0)
# 학생을 배치하여 얻을 수 있는 분위기 점수 최댓값
n = int(input())  # 교실 행의 개수
k = int(input())  # 학생 관계의 개수

relations = {}
for _ in range(k):
    a, b, c = map(int, input().split())
    if b < c:
        if a == 1:
            relations[(b, c)] = a
        else:
            relations[(b, c)] = -1
    else:
        if a == 1:
            relations[(c, b)] = a
        else:
            relations[(c, b)] = -1

tmp = list(range(1, 2 * n + 1))


def dfs(n, relations, tmp, row, w):
    if n == w:
        score = 0
        for r in row:
            score += relations.get(r, 0)
        return score

    answer = float('-inf')
    for i, j in enumerate(tmp):
        for k, l in enumerate(tmp[:i]):
            new_row = row + [(l, j)]
            cnt = dfs(n, relations, tmp[:k] + tmp[k + 1:i] + tmp[i + 1:], new_row, w + 1)
            answer = max(answer, cnt)

    return answer


print(dfs(n, relations, tmp, [], 0))
