# 조건에 맞는 정수의 개수

n = int(input())

# 조건 만족하는 양의 정수 A 개수 구하기
# 1. n개의 자릿수 갖는 정수 (자릿수는 0이 아님)
# 2. 이웃한 두 자리의 숫자 차이는 2 이하

def solution(A, n):
    m = len(A) # 현재까지 만든 자릿수 개수

    if m == n: # n자리 정수 만든 경우
        return 1
    # 숫자의 범위 구하기
    if m == 0:
        start, end = 1, 9 # 첫 번째 자릿수는 1~9
    else:
        # 이웃한 두자리 수 차이 2 이하
        start = max(A[m-1]-2, 1)
        end = min(A[m-1]+2, 9)
    cnt = 0 # 조건 만족하는 양의 정수 개수
    # 모두 탐색하면서 답 찾기
    for i in range(start, end+1):
        A.append(i)
        cnt += solution(A, n)
        A.pop()
    return cnt

print(solution([], n))

