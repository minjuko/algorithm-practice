def solution(balls, share):
    import math
    answer = math.comb(balls, share)
    return answer
# +a 조합 직접 계산하기 n! / r!(n-r)!