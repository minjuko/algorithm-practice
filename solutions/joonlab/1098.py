# 배열 다중 업데이트 다중 합

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(list(map(int, input().split())) for _ in range(m)) # m개의 질의

def solution(n, m, A, B):
    # 질의 하나씩 확인
    for b in B:
        if b[0] == 1: # 유형 1이면
            for i in range(b[1], b[2]+1):
                A[i] += b[3] # i~j번째 원소에 k 더하기
        else: # 유형 2이면
            sum = 0
            for i in range(b[1], b[2]+1):
                sum += A[i]
            print(sum)
solution(n, m, A, B)