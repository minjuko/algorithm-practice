# 뒤에 있는 큰 수 찾기

# 뒷 큰 수 : 자신보다 뒤에 있는 숫자 중 자신보다 크면서 가장 가까이 있는 수

def solution(numbers):
    answer = [-1] * len(numbers)  # default:존재하지 않으면 -1
    stack = []

    for i in range(len(numbers)):
        # 스택의 마지막 인덱스가 더 작으면 뒷큰수가 존재하지 않는다.
        # -> 꺼내서 저장
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer