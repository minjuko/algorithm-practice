def solution(s, n):
    result = []

    for ch in s:
        # 대문자:'A'기준 0~25범위에서 n을 더하고 26을 나눈 나머지 계산
        if ch.isupper():
            tmp = chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
            result.append(tmp)
        # 소문자:'a'기준
        elif ch.islower():
            tmp = chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
            result.append(tmp)
        # 공백
        else:
            result.append(ch)

    return "".join(result)