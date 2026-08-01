def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if not stk or stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()  # stk 마지막 원소를 제거
    return stk