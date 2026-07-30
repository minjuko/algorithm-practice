def solution(strArr):
    cnt = {}  # key:문자열의 길이, value:해당 길이의 개수

    for s in strArr:
        # 해당 길이가 이미 있으면 +1, 없으면 0 + 1
        cnt[len(s)] = cnt.get(len(s), 0) + 1

    return max(cnt.values())