def solution(a, b):
    ans1 = str(a) + str(b)
    ans2 = str(b) + str(a)
    if int(ans1 > ans2):
        return int(ans1)
    else:
        return int(ans2)
# 다른 풀이
# return int(max(f'{a}{b}', f'{b}{a}'))
# return max(int(str(a)+str(b)), int(str(b)+str(a)))