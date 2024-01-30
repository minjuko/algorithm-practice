# 콜라츠 추측

# 수가 짝수이면 2로 나누기
# 수가 홀수라면 3을 곱하고 1 더하기
# 수가 1이 될때까지 반복

def solution(num):
    cnt = 0
    while (True):
        if num == 1:
            break
        if cnt == 500:
            cnt = -1
            break

        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        cnt += 1
    return cnt

# 다른 풀이
# def solution(num):
#     for cnt in range(500):
#         if num == 1:
#             return cnt
#         num = num // 2 if num % 2 == 0 else num * 3 + 1
#     return -1
