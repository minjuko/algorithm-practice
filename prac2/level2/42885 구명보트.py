# 구명보트

# 최대 2명, 무게 제한
# 최소 구명보트 수

# 가장 작은 사람 + 큰 사람 -> 무게 제한 안넘으면 같이 태움
# 무게 제한 넘으면 큰 사람만 태움

def solution(people, limit):
    answer = 0  # 최소 구명보트 수
    people.sort()
    start = 0
    end = len(people) - 1
    # 제일 작은 사람 + 큰 사람 해서 안들어가면 큰 사람만 태우기
    while (start <= end):
        if (people[start] + people[end] > limit):  # 초과하면
            end -= 1  # 큰 사람만 태우기
            answer += 1
        else:  # 초과하지 않으면 둘 다 태우기
            start += 1
            end -= 1
            answer += 1

    return answer