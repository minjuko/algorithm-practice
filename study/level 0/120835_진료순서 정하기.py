def solution(emergency):
    answer = []
    tmp = sorted(emergency, reverse=True)

    for i in emergency:
        rank = tmp.index(i) + 1  # 순서는 1부터
        answer.append(rank)
    return answer