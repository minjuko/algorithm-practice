# 삼총사

# 세 학생 번호 합이 0이 되는 경우의 수
from itertools import combinations

# 조합 구해서 0이 되는지 판별
def solution(number):
    answer = 0
    arr = list(combinations(number, 3))
    for case in arr:
        if sum(case) == 0:
            answer += 1
    return answer

# 라이브러리 사용하지 않은 다른 풀이
# def solution(number):
#     answer = 0
#     l = len(number)
#     for i in range(l-2):
#         for j in range(i+1, l-1):
#             for k in range(j+1, l):
#                 # print(number[i],number[j],number[k])
#                 if number[i]+number[j]+number[k] == 0:
#                     answer += 1
#     return answer