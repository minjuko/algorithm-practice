# 연속 부분 수열 합의 개수

# 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 경우의 수 구하기

def solution(elements):
    answer = set()
    len_elements = len(elements)
    elements = elements*2 # 수열 길이 두 배로

    for i in range(len_elements): # 부분 수열의 길이
        for j in range(len_elements): # 부분 수열의 시작 위치
            answer.add(sum(elements[j:j+i+1])) # 부분 수열의 합
    return len(answer)
