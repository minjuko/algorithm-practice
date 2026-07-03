# 추억 점수

def solution(name, yearning, photo):
    answer = [] # 추억 점수 저장
    dic = dict(zip(name, yearning)) # 이름: 그리움 점수

    for i in photo:
        score = 0 # 점수 초기화
        for j in i: # 사진의 각 이름에 대해
            if j in dic.keys(): # 딕셔너리에 존재하면
                score += dic[j] # 추억 점수에 갱신
        answer.append(score) # 추억 점수 저장

    return answer