# 2-1-3 두 배열 원소 크기 비교 

A = list(map(int, input().split())) # 배열 A
B = list(map(int, input().split())) # 배열 B

# def solution(A, B):
#     # A, B 원소가 더 큰 경우의 수
#     a = 0
#     b = 0
#     for i in range(len(A)):
#         if A[i] > B[i]:
#             a += 1
#         elif A[i] < B[i]:
#             b += 1 
#     if a > b:
#         return '1'
#     else:
#         return '0'

def solution(A, B):
    a, b = 0, 0
    for x, y in zip(A, B):
        if x > y:
            a += 1
        elif x < y:
            b += 1
    return int(a > b)

print(solution(A, B))