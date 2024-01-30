# 구명보트

# 최대 2명 + 무게 제한
# 모든 사람을 구출하는 최소 구명보트 수 구하기

def solution(people, limit):
    answer = 0 # 최소 구명보트 수
    people.sort()

    start = 0
    end = len(people) - 1
    # 몸무게 가장 작은, 큰 사람 먼저 확인 -> 무게 제한 걸리면 큰 사람 혼자 구출
    while (start <= end):
        if(people[start]+ people[end] <= limit):
            start += 1
            end -= 1
        else: # 제한 걸리면 몸무게 큰 사람 먼저 혼자 구출
            end -= 1
        answer += 1
    return answer


