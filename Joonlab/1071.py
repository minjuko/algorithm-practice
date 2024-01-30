# 2-1-1 배열 원소 개수 구하기 

n,  k = map(int, input().split()) # n : 배열 A의 크기, k : 구하려는 원소의 값 
A = list(map(int, input().split())) # 배열 A 

def solution(n, A, k):
    count = 0
    for a in A:
        if a == k:
            count += 1
    return count 

print(solution(n, A, k))