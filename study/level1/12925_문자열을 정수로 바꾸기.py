def solution(s):
    if "+" in s:
        return int(s[1:])
    elif "-" in s:
        return int(s[1:]) * (-1)
    else:
        return int(s)
# 그냥 return int(s) 하면 자동 부호 처리