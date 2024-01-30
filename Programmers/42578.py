# 의상

# 서로 다른 옷의 조합 수
# 일부 겹치는 것은 허용

def solution(clothes):
    answer = 1 # 초기값

    # 종류별로 딕셔너리 저장
    dic_clothes = {}
    for name, kind in clothes:
        # 딕셔너리에 종류가 존재하면 해당 종류에 추가 아니면 새로 지정
        if kind in dic_clothes.keys(): # 키 값으로 종류 존재
            dic_clothes[kind] += [name] # 이름 추가
        else:
            dic_clothes[kind] = [name]
    # 경우의 수 구하기
    # a 종류 n개, b 종류 m개 -> (n+1)(m+1)
    for _, value in dic_clothes.items():
        answer *= (len(value)+1)
    return answer - 1 # 모두 안 입는 경우 제외
