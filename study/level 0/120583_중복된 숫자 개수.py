def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer
# 간단한 풀이
# return array.count(n)