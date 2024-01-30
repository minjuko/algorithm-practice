# 2차원 배열 다중 업데이트 다중 합

n, m = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n)) # 4*4 배열
B = list(list(map(int, input().split())) for _ in range(m)) # m개의 질의

def solution(n, m, A, B):
    for b in B:
        if b[0] == 1: # 유형 1이면
            for i in range(b[1], b[3]+1):
                for j in range(b[2], b[4]+1):
                    A[i][j] += b[5] # i1~-i2, j1~-j2번째 원소에 k 더하기
        else: # 유형 2이면
            sum = 0
            for i in range(b[1], b[3]+1):
                for j in range(b[2], b[4]+1):
                    sum += A[i][j]
            print(sum)
solution(n, m, A, B)