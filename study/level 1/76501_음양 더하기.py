def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        # 양수
        if signs[i]:
            answer += absolutes[i]
        # 음수
        else:
            answer -= absolutes[i]

    return answer

# 한 줄로 쓰기 (조건부 표현식 | 삼항 연산자)
# answer += absolutes[i] if signs[i] else -absolutes[i]