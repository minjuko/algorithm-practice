# 구간 안에 있는 원소의 수
from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(list(map(int, input().split())) for _ in range(m)) # 질의

def solution(n, m, A, B):
    A.sort()
    answer = []
    for i, j in B:
        x, y = bisect_left(A, i), bisect_right(A, j)
        answer.append(y - x)
    for ans in answer:
        print(ans)

solution(n, m, A, B)

# 오류 원인을 알 수 없음,,,
# 보류
