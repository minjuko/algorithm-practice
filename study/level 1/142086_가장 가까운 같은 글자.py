def solution(s):
    # 각 문자 마지막 등장 인덱스 저장하기

    result = []
    dict = {}  # 문자의 마지막 위치 저장

    for idx, ch in enumerate(s):
        # 1. 현재 문자가 이전에 등장했던 문자이면 거리 계산
        if ch in dict:
            result.append(idx - dict[ch])
        # 2. 처음 이면 -1 
        else:
            result.append(-1)
        # 현재 문자의 인덱스로 위치 갱신
        dict[ch] = idx

    return result