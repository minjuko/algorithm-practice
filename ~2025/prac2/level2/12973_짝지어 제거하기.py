# 짝지어 제거하기
# 같은 알파벳 2개 붙어있는 짝 찾아 제거 ->앞 뒤 이어 붙임
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)  # 알파벳 넣기
        elif stack[-1] == i:  # 연속으로 같은 알파벳 있으면
            stack.pop()  # 꺼내기
        else:  # 연속 없으면
            stack.append(i)  # 알파벳 넣기
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer