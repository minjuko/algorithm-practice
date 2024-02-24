# 햄버거 만들기
# 빵-야채-고기-빵 순서여야 햄버거 1개 포장 가능 (1-2-3-1)

def solution(ingredient):
    answer = 0  # 햄버거 수
    stack = []

    for i in ingredient:
        stack.append(i)  # 재료를 스택에 추가
        # 스택 마지막 4개 순서가 일치하면 (1-2-3-1) 포장 가능
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1  # 햄버거 수 업데이트
            for _ in range(4):
                stack.pop()  # 스택에서 제거
    return answer