# 올바른 괄호

# 괄호 올바르게 짝지어져 있으면 true

def solution(s):
    answer = True
    arr = []

    for i in s:
        if i == '(':
            arr.append(i)  # 괄호 시작 부분 추가
        else:
            if arr == []:  # 닫는 괄호 왔는데 arr에 아무것도 없으면 짝지어지지 않음 -> false
                answer = False
                break
            else:  # 짝지어지면 꺼내기
                arr.pop()

    if arr != []:
        answer = False

    return answer