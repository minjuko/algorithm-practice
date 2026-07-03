def solution(clothes):
    answer = 1

    dic = {}  # {종류: 이름}

    # 딕셔너리에 종류별로 저장
    for name, kind in clothes:
        if kind in dic:
            dic[kind] += [name]
        else:
            dic[kind] = [name]

    print(dic)

    # 서로 다른 옷의 조합 수
    # 1번 종류가 n개, 2번 종류가 m개 있다면 조합 수는 (n+1)(m+1)

    for val in dic.values():
        answer *= (len(val) + 1)
    return answer - 1  # 최소 한 개의 의상을 입어야 하므로 안입는 경우 제외