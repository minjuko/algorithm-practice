# 약수의 개수와 덧셈

# 두 정수 사이의 수 중 약수의 개수가 짝수이면 덧셈, 홀수이면 뺄셈

def solution(left, right):
    def a(x):
        cnt = 1
        for i in range(1, x):
            if x % i == 0:
                cnt += 1
        return cnt

    answer = 0
    for i in range(left, right + 1):
        if a(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer