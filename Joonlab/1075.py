# 2-1-5 2차원 배열 단일 업데이트 

n = int(input()) # nxn 배열 A의 크기
A = list(list(map(int, input().split())) for _ in range(n)) # nxn 배열 A
i1, j1, i2, j2, k = map(int, input().split()) # i1, i2 : 행 번호, j1, j2 : 열 번호, k : 곱할 값

def solution(n, A, i1, j1, i2, j2, k):
    for i_index in range(i1, i2+1): # 행부터 
        for j_index in range(j1, j2+1): # 열까지
            A[i_index][j_index] *= k
    # 2차원 배열의 모든 원소의 합 구하기
    answer = 0 
    for i in range(n):
        answer += sum(A[i]) # 각 행 합을 더해준다 
    return answer

print(solution(n, A, i1, j1, i2, j2, k))
