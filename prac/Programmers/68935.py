# 3진법 뒤집기

# n을 3진법에서 뒤집기 -> 10진법 표현

def solution(n):
    answer = ''
    while (n > 0):
        n, r = divmod(n, 3)  # 3진법
        answer += str(r)

    return int(answer, 3)  # 10진법 변환