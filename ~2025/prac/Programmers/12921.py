# 소수 찾기

# 1-n 사이 소수 개수 반환
# 에라토스테네스의 체
# 1. 2부터 현재 수의 배수 모두 지우기 (자신 제외)
# 2. 남은 수 중 가장 작은 수에서 1번 반복

def solution(n):
    num = [True] * (n+1) # 0~n까지의 수 저장 배열
    num[0] = num[1] = False # 0, 1은 소수가 아님

    for i in range(2, int(n**0.5)+1): # 2~루트n까지 반복
        if num[i]:
            for j in range(i*2, n+1, i): # i의 배수 지우기
                num[j] = False
    return sum(num)

# 다른 풀이
# def solution(n):
#     num=set(range(2,n+1)) # 2~n 집합
#
#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i)) # i의 배수들을 집합에서 제거
#     return len(num)
