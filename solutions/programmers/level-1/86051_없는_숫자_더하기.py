# 없는 숫자 더하기

# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수 구하기

def solution(numbers):
    answer = 0
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer

# 다른 풀이
# solution = lambda x: sum(range(10)) - sum(x)