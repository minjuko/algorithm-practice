def solution(quiz):
    answer = []
    tmp = 0 # 연산 결과 저장
    for i in quiz:
        # 각 문자 분리
        x, op, y, _, z = i.split()
        if op == "+":
            tmp = int(x) + int(y)
        else:
            tmp = int(x) - int(y)
        if tmp == int(z):
            answer.append("O")
        else:
            answer.append("X")
    return answer