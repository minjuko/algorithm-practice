# 내적

def solution(a, b):
    answer = 0
    for i in range(0, len(a)):
        answer += a[i]*b[i]
    return answer

# 다른 풀이
#  return sum([x*y for x, y in zip(a,b)])