# 학생 이름 출현 횟수 

S = input().split() # 학생 이름 목록 문자열 

def solution(S):
    D = {} # 딕셔너리 설정 (key : 학생 이름, value : 출현 횟수)
    for s in S:
        if s in D:
            D[s] += 1
        else:
            D[s] = 1 
    answer = list(D.items()) # 딕셔너리를 리스트로 변환 [학생 이름, 출현 횟수] 원소인 1차원 배열 
    answer.sort(key=lambda x: x[0]) # 학생 이름 기준 오름차순 
    for name, value in answer:
        print(name, value)

solution(S)
