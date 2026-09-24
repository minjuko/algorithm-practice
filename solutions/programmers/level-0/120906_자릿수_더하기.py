def solution(n):
    answer = 0
    for num in str(n): # 각 자리의 숫자
        answer += int(num)
    return answer
# 다른 풀이
# return sum(map(int, str(n)))