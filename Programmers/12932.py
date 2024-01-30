# 자연수 뒤집어 배열로 만들기

# n을 뒤집어 배열 형태로 반환

def solution(n):
    answer = []
    while n>0:
        answer.append(n%10)
        n = n//10
    return answer

# 다른 풀이
# return list(map(int, reversed(str(n))))