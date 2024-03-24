# 영화제

def can_defeat(score1, score2):
    return score1[0] >= score2[0] and score1[1] >= score2[1] and score1[2] >= score2[2]


def find_max_independent_set(scores):
    n = len(scores)
    defeated = [0] * n

    for i in range(n):
        for j in range(n):
            if i != j and can_defeat(scores[i], scores[j]):
                defeated[j] += 1

    independent_set = []
    for i in range(n):
        if defeated[i] <= 2:
            independent_set.append(i)

    return len(independent_set)


N = int(input())
scores = []
for _ in range(N):
    scores.append(list(map(int, input().split())))

print(find_max_independent_set(scores))
