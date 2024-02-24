# 2-1-4 2차원 배열 원소 개수 구하기 

n, k = map(int, input().split()) # n : 배열 A의 크기, k : 구하려는 원소의 값
# 2차원 배열 입력 받기 
A = list(list(map(int, input().split())) for _ in range(n)) # nxn 배열 A

def solution(n, A, k):
    count = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] == k:
                count += 1
    return count 

print(solution(n, A, k ))