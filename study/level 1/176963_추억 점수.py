def solution(name, yearning, photo):
    # 이름 - 그리움 점수 딕셔너리로 저장
    score_dict = dict(zip(name, yearning))
    result = []

    # 사진을 돌면서 점수 계산
    for p in photo:
        p_score = 0
        for k in p:
            p_score += score_dict.get(k, 0) # 이름이 없으면 0
        result.append(p_score)

    return result
