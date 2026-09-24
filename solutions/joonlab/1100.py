# 문자열 끝에 문자 삽입

A = input().rstrip()
k = int(input())

# 문자열 A의 길이가 k가 될 때까지 A의 끝에 마지막 문자 삽입하는 동작 반복 -> 문자열 출력

def solution(A, k):
    while len(A) < k: # k가 될 때까지 반복
        A += A[-1] # 마지막 문자 삽입
    print(A)

solution(A, k)