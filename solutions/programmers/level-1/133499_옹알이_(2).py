# 옹알이 (2)
# 같은 발음 연속 X
# 발음할 수 있는 단어 수 구하기

def solution(babbling):
    answer = 0
    prons = ["aya", "ye", "woo", "ma"]  # 가능한 발음
    for i in babbling: # 단어 하나씩 판단
        for pron in prons: # 발음 가능한 단어이면 공백으로 대체
            if pron*2 not in i: # 연속 X
                i = i.replace(pron, " ")
        if i.isspace(): # 공백만 있다면
            answer += 1
    return answer
