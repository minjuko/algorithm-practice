# 음양 더하기

# 정수들의 절댓값 배열 + 부호 배열 -> 실제 정수들의 합 구하기

def solution(absolutes, signs):
    answer = 0
    print(signs)

    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer