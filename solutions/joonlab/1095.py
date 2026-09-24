# 배열 전체 탐색하기

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(int(input()) for _ in range(m))

def solution(n, m, A, B):
    answer = []
    # 배열 A의 원소 중 k 보다 크거나 같은 개수를 구하기
    for k in B:
        count = 0
        for a in A:
            if a >= k:
                count += 1
        answer.append(count)
    for ans in answer:
        print(ans)
solution(n, m, A, B)