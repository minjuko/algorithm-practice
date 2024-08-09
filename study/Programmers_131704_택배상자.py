# 택배상자

def solution(order):
    answer = 0
    arr = []
    i = 1
    while i != len(order) + 1:
        arr.append(i)
        while arr and arr[-1] == order[answer]:
            answer += 1
            arr.pop()
        i+=1
    return answer