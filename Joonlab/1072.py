# 2-1-2 배열 단일 업데이트 

n = int(input()) # n : 배열 A의 크기
A = list(map(int, input().split())) # 배열 A
i, j, k = map(int, input().split()) # i번째 원소, j번째 원소, k : 곱할 값

def solution(n, A, i, j, k):
    for index in range(i, j+1): # 범위에서 끝점은 포함 X이므로 +1
        A[index] *= k
    return sum(A)

print(solution(n, A, i, j, k))