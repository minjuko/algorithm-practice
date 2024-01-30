# 조건에 맞는 정수의 개수

n = int(input())

# 조건을 만족하는 양의 정수 A 개수 구하기
# 1. n개의 자릿수를 갖는 정수 (자릿수는 0이 아님)
# 2. 이웃한 두 자리의 숫자 차이는 2 이하

def solution(n):
    answer = 0
    for i in range(10**(n-1), 10**n): # n자리 정수 모두 탐색
        if is_valid(i):
            answer += 1
    print(answer)

def is_valid(i): # 조건 탐색
    # 낮은 자릿수부터 탐색
    prev = i % 10 # 이전 자릿수
    i //= 10
    if prev == 0: # 0이면 조건 만족 X
        return False
    while i > 0:
        cur = i % 10 # 현재 자릿수
        i //= 10

        if cur == 0 or abs(prev- cur) > 2: # 이웃한 두 자리의 수 차이가 2 초과이면 조건 만족 X
            return False
        prev = cur
    return True

solution(n)