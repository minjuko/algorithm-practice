# 큰 원소의 수

from bisect import bisect_right
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(int(input()) for _ in range(m)) # 질의

# k : k보다 큰 원소의 개수 출력
def solution(n, m, A, B):
    A.sort()
    answer = []
    for b in B:
        answer.append(n - bisect_right(A, b))
    for ans in answer:
        print(ans)

solution(n, m, A, B)