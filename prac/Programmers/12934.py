# 정수 제곱근 판별

# n이 양의 정수 x의 제곱인지 판별
# 제곱이면 x+1의 제곱 리턴 아니면 -1

def solution(n):
    if int(n ** 0.5) == n ** 0.5:  # 어떤 수의 제곱인지 판별
        answer = (n ** 0.5 + 1) ** 2
    else:
        answer = -1
    return answer